"""
this script takes as input the LSTM or RNN weights found by train.py
change the path in the shared_variables.py to point to the h5 file
with LSTM or RNN weights generated by train.py

Author: Niek Tax
"""

from __future__ import division
from keras.models import load_model
import csv
import copy
import numpy as np
import distance
from itertools import izip
# noinspection PyProtectedMember
from jellyfish._jellyfish import damerau_levenshtein_distance
from sklearn import metrics
import time
from datetime import datetime, timedelta
from collections import Counter
from shared_variables import getUnicode_fromInt, activateSettings
from support_scripts.prepare_data_resource import selectFormulaVerifiedTraces


# noinspection PyShadowingNames,PyUnusedLocal
def runExperiments(logIdentificator, formulaType):
    eventlog, path_to_model_file, beam_size, \
        prefix_size_pred_from, prefix_size_pred_to, formula = activateSettings(logIdentificator, formulaType)

    start_time = time.time()

    csvfile = open('../data/%s' % eventlog, 'r')
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(spamreader, None)  # skip the headers

    lastcase = ''
    line = ''
    line_group = ''
    firstLine = True
    lines = []
    lines_group = []
    timeseqs = []   # relative time since previous event
    timeseqs2 = []  # relative time since case start
    timeseqs3 = []  # absolute time of previous event
    times = []
    times2 = []
    times3 = []
    numlines = 0
    casestarttime = None
    lasteventtime = None

    for row in spamreader:
        t = time.strptime(row[2], "%Y-%m-%d %H:%M:%S")
        if row[0] != lastcase:
            casestarttime = t
            lasteventtime = t
            lastcase = row[0]
            if not firstLine:
                lines.append(line)
                lines_group.append(line_group)
                timeseqs.append(times)
                timeseqs2.append(times2)
                timeseqs3.append(times3)
            line = ''
            line_group = ''
            times = []
            times2 = []
            times3 = []
            numlines += 1
        line += getUnicode_fromInt(row[1])
        line_group += getUnicode_fromInt(row[3])
        timesincelastevent = datetime.fromtimestamp(time.mktime(t))-datetime.fromtimestamp(time.mktime(lasteventtime))
        timesincecasestart = datetime.fromtimestamp(time.mktime(t))-datetime.fromtimestamp(time.mktime(casestarttime))
        midnight = datetime.fromtimestamp(time.mktime(t)).replace(hour=0, minute=0, second=0, microsecond=0)
        # noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
        timesincemidnight = datetime.fromtimestamp(time.mktime(t))-midnight
        timediff = 86400 * timesincelastevent.days + timesincelastevent.seconds
        timediff2 = 86400 * timesincecasestart.days + timesincecasestart.seconds
        times.append(timediff)
        times2.append(timediff2)
        times3.append(datetime.fromtimestamp(time.mktime(t)))
        lasteventtime = t
        firstLine = False

    # add last case
    lines.append(line)
    lines_group.append(line_group)
    timeseqs.append(times)
    timeseqs2.append(times2)
    timeseqs3.append(times3)
    numlines += 1

    divisor = np.mean([item for sublist in timeseqs for item in sublist])
    print('divisor: {}'.format(divisor))
    divisor2 = np.mean([item for sublist in timeseqs2 for item in sublist])
    print('divisor2: {}'.format(divisor2))
    divisor3 = np.mean(map(lambda x: np.mean(map(lambda y: x[len(x)-1]-y, x)), timeseqs2))
    print('divisor3: {}'.format(divisor3))

    elems_per_fold = int(round(numlines/3))

    fold1and2lines = lines[:2*elems_per_fold]
    fold1and2lines_group = lines_group[:2*elems_per_fold]

    step = 1
    sentences = []
    softness = 0
    next_chars = []
    fold1and2lines = map(lambda x: x+'!', fold1and2lines)
    fold1and2lines_group = map(lambda x: x+'!', fold1and2lines_group)
    maxlen = max(map(lambda x: len(x), fold1and2lines))

    chars = map(lambda x: set(x), fold1and2lines)
    chars = list(set().union(*chars))
    chars.sort()
    target_chars = copy.copy(chars)
    chars.remove('!')
    print('total chars: {}, target chars: {}'.format(len(chars), len(target_chars)))
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))
    target_char_indices = dict((c, i) for i, c in enumerate(target_chars))
    target_indices_char = dict((i, c) for i, c in enumerate(target_chars))

    chars_group = map(lambda x: set(x), fold1and2lines_group)
    chars_group = list(set().union(*chars_group))
    chars_group.sort()
    target_chars_group = copy.copy(chars_group)
    chars_group.remove('!')
    print('total groups: {}, target groups: {}'.format(len(chars_group), len(target_chars_group)))
    char_indices_group = dict((c, i) for i, c in enumerate(chars_group))
    indices_char_group = dict((i, c) for i, c in enumerate(chars_group))
    target_char_indices_group = dict((c, i) for i, c in enumerate(target_chars_group))
    target_indices_char_group = dict((i, c) for i, c in enumerate(target_chars_group))

    # we only need the third fold, because first two were used for training
    fold3 = lines[2*elems_per_fold:]
    fold3_group = lines_group[2*elems_per_fold:]
    fold3_t = timeseqs[2*elems_per_fold:]
    fold3_t2 = timeseqs2[2*elems_per_fold:]
    fold3_t3 = timeseqs3[2*elems_per_fold:]

    lines = fold3
    lines_group = fold3_group
    lines_t = fold3_t
    lines_t2 = fold3_t2
    lines_t3 = fold3_t3

    # set parameters
    predict_size = maxlen

    # load model, set this to the model generated by train.py
    model = load_model(path_to_model_file)

    # define helper functions
    # this one encodes the current sentence into the onehot encoding
    # noinspection PyUnusedLocal
    def encode(sentence, sentence_group, times, times3, maxlen=maxlen):
        num_features = len(chars)+len(chars_group)+5
        X = np.zeros((1, maxlen, num_features), dtype=np.float32)
        leftpad = maxlen-len(sentence)
        times2 = np.cumsum(times)
        for t, char in enumerate(sentence):
            midnight = times3[t].replace(hour=0, minute=0, second=0, microsecond=0)
            timesincemidnight = times3[t]-midnight
            multiset_abstraction = Counter(sentence[:t+1])
            for c in chars:
                if c == char:
                    X[0, t+leftpad, char_indices[c]] = 1
            for g in chars_group:
                if g == sentence_group[t]:
                    X[0, t+leftpad, len(char_indices)+char_indices_group[g]] = 1
            X[0, t+leftpad, len(chars)+len(chars_group)] = t+1
            X[0, t+leftpad, len(chars)+len(chars_group)+1] = times[t]/divisor
            X[0, t+leftpad, len(chars)+len(chars_group)+2] = times2[t]/divisor2
            X[0, t+leftpad, len(chars)+len(chars_group)+3] = timesincemidnight.seconds/86400
            X[0, t+leftpad, len(chars)+len(chars_group)+4] = times3[t].weekday()/7
        return X

    # modify to be able to get second best prediction
    def getSymbol(predictions, ith_best=0):
        i = np.argsort(predictions)[len(predictions) - ith_best - 1]
        return target_indices_char[i]

    def getSymbolGroup(predictions, ith_best=0):
        i = np.argsort(predictions)[len(predictions) - ith_best - 1]
        return target_indices_char_group[i]

    one_ahead_gt = []
    one_ahead_gt_group = []
    one_ahead_pred = []

    two_ahead_gt = []
    two_ahead_pred = []

    three_ahead_gt = []
    three_ahead_pred = []

    with open('output_files/results/'+formulaType+'/suffix_and_remaining_time0_%s' % eventlog, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["Prefix length", "Ground truth", "Predicted", "Levenshtein", "Damerau", "Jaccard",
                             "Ground truth times", "Predicted times", "RMSE", "MAE", "Median AE", "Ground Truth Group",
                             "Predicted Group", "Levenshtein Group"])
        for prefix_size in range(prefix_size_pred_from, prefix_size_pred_to):
            lines_s, lines_group_s, lines_t_s, lines_t2_s, lines_t3_s = selectFormulaVerifiedTraces(lines, lines_group,
                                                                                                    lines_t, lines_t2,
                                                                                                    lines_t3, formula,
                                                                                                    prefix_size)
            print(prefix_size)
            print("formulas verified: " + str(len(lines_s)) + " out of : " + str(len(lines)))
            for line, line_group, times, times2, times3 in izip(lines_s, lines_group_s, lines_t_s, lines_t2_s,
                                                                lines_t3_s):
                times.append(0)
                cropped_line = ''.join(line[:prefix_size])
                cropped_line_group = ''.join(line_group[:prefix_size])
                cropped_times = times[:prefix_size]
                cropped_times3 = times3[:prefix_size]
                if len(times2) < prefix_size:
                    continue  # make no prediction for this case, since this case has ended already
                ground_truth = ''.join(line[prefix_size:prefix_size+predict_size])
                ground_truth_group = ''.join(line_group[prefix_size:prefix_size+predict_size])
                ground_truth_t = times2[prefix_size-1]
                case_end_time = times2[len(times2)-1]
                ground_truth_t = case_end_time-ground_truth_t
                predicted = ''
                predicted_group = ''
                total_predicted_time = 0
                for i in range(predict_size):
                    enc = encode(cropped_line, cropped_line_group, cropped_times, cropped_times3)
                    y = model.predict(enc, verbose=0)  # make predictions
                    # split predictions into seperate activity and time predictions
                    y_char = y[0][0]
                    y_group = y[1][0]
                    y_t = y[2][0][0]
                    prediction = getSymbol(y_char)  # undo one-hot encoding
                    prediction_group = getSymbolGroup(y_group)  # undo one-hot encoding
                    cropped_line += prediction
                    cropped_line_group += prediction_group
                    if y_t < 0:
                        y_t = 0
                    cropped_times.append(y_t)
                    # end of case was just predicted, therefore, stop predicting further into the future
                    if prediction == '!':
                        one_ahead_pred.append(total_predicted_time)
                        one_ahead_gt.append(ground_truth_t)
                        print('! predicted, end case')
                        break
                    y_t = y_t * divisor3
                    cropped_times3.append(cropped_times3[-1] + timedelta(seconds=y_t))
                    total_predicted_time = total_predicted_time + y_t
                    predicted += prediction
                    predicted_group += prediction_group
                output = []
                if len(ground_truth) > 0:
                    output.append(prefix_size)
                    print("Ground truth: ", ground_truth)
                    print("Ground truth encoded: ", unicode(ground_truth).encode("utf-8"))
                    output.append(unicode(ground_truth).encode("utf-8"))
                    print("Predicted: ", predicted)
                    print("Predicted encoded: ", unicode(predicted).encode("utf-8"))
                    output.append(unicode(predicted).encode("utf-8"))
                    output.append(1 - distance.nlevenshtein(predicted, ground_truth))
                    dls = 1 - (damerau_levenshtein_distance(unicode(predicted),
                                                            unicode(ground_truth)) / max(len(predicted),
                                                                                         len(ground_truth)))
                    # we encountered problems with Damerau-Levenshtein Similarity on some linux machines where
                    # the default character encoding of the operating system caused it to be negative,
                    # this should never be the case
                    if dls < 0:
                        dls = 0
                    output.append(dls)
                    output.append(1 - distance.jaccard(predicted, ground_truth))
                    output.append(ground_truth_t)
                    output.append(total_predicted_time)
                    output.append('')
                    output.append(metrics.mean_absolute_error([ground_truth_t], [total_predicted_time]))
                    output.append(metrics.median_absolute_error([ground_truth_t], [total_predicted_time]))
                    output.append(unicode(ground_truth_group).encode("utf-8"))
                    output.append(unicode(predicted_group).encode("utf-8"))
                    output.append(1 - distance.nlevenshtein(predicted_group, ground_truth_group))
                    spamwriter.writerow(output)
    print("TIME TO FINISH --- %s seconds ---" % (time.time() - start_time))
