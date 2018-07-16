"""
this script trains an LSTM model on one of the data files in the data folder of
this repository. the input file can be changed to another file from the data folder
by changing its name in line 46.

it is recommended to run this script on GPU, as recurrent networks are quite
computationally intensive.

Author: Niek Tax
"""

from __future__ import print_function, division
from keras.models import Model
from keras.layers.core import Dense
from keras.layers.recurrent import LSTM
from keras.layers import Input
from keras.optimizers import Nadam
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from keras.layers.normalization import BatchNormalization
import numpy as np
import copy
import csv
import time
from datetime import datetime
from shared_variables import get_unicode_from_int, eventlog


# this part of the src opens the file, reads it into three following variables

where_to_look_for_dataset = "../data/July2018"

def train():
    lines = []  # list of all the activity sequences
    timeseqs = []  # time sequences (differences between two events)
    timeseqs2 = []  # time sequences (differences between the current and first)

    # helper variables
    lastcase = ''
    line = ''  # sequence of activities for one case
    firstline = True
    times = []
    times2 = []
    numlines = 0
    casestarttime = None
    lasteventtime = None

    csvfile = open((where_to_look_for_dataset + '/%s') % eventlog, 'r')
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(spamreader, None)  # skip the headers

    for row in spamreader:  # the rows are "CaseID,ActivityID,CompleteTimestamp"
        try:
            t = time.strptime(row[2], "%Y-%m-%d %H:%M:%S")  # creates a datetime object from row[2]

        except ValueError as e:
            t = time.strptime(row[2], "%Y/%m/%d %H:%M:%S")  # creates a datetime object from row[2]
        if row[0] != lastcase:  # 'lastcase' is to save the last executed case for the loop
            casestarttime = t
            lasteventtime = t
            lastcase = row[0]
            if not firstline:  # here we actually add thesequences to the lists
                lines.append(line)
                timeseqs.append(times)
                timeseqs2.append(times2)
            line = ''
            times = []
            times2 = []
            numlines += 1
        line += get_unicode_from_int(row[1])
        timesincelastevent = datetime.fromtimestamp(time.mktime(t))-datetime.fromtimestamp(time.mktime(lasteventtime))
        timesincecasestart = datetime.fromtimestamp(time.mktime(t))-datetime.fromtimestamp(time.mktime(casestarttime))
        timediff = 86400 * timesincelastevent.days + timesincelastevent.seconds
        timediff2 = 86400 * timesincecasestart.days + timesincecasestart.seconds
        times.append(timediff)
        times2.append(timediff2)
        lasteventtime = t
        firstline = False

    # add last case
    lines.append(line)
    timeseqs.append(times)
    timeseqs2.append(times2)
    numlines += 1

    divisor = np.mean([item for sublist in timeseqs for item in sublist])  # average time between events
    print('divisor: {}'.format(divisor))
    divisor2 = np.mean([item for sublist in timeseqs2 for item in sublist])  # average time between current and
    # first events
    print('divisor2: {}'.format(divisor2))

    # separate training data into 2(out of 3) parts
    elems_per_fold = int(round(numlines/3))

    many = 0
    for i in range(len(lines)):
        many = many + len(lines[i])

    print ("average length of the trace: ", many / len(lines))
    print ("number of traces: ", len(lines))

    fold1 = lines[:elems_per_fold]
    fold2 = lines[elems_per_fold:2*elems_per_fold]
    lines = fold1 + fold2

    lines = [x+"!" for x in lines]  # put delimiter symbol
    maxlen = max([len(x) for x in  lines])  # find maximum line size

    # next lines here to get all possible characters for events and annotate them with numbers
    chars = [set(x) for x in lines] # remove duplicate activities from each separate case
    chars = list(set().union(*chars))  # creates a list of all the unique activities in the data set
    chars.sort()  # sorts the chars in alphabetical order
    target_chars = copy.copy(chars)
    chars.remove('!')
    print('total chars: {}, target chars: {}'.format(len(chars), len(target_chars)))
    char_indices = dict((c, i) for i, c in enumerate(chars))
    target_char_indices = dict((c, i) for i, c in enumerate(target_chars))

    csvfile = open(where_to_look_for_dataset + '/%s' % eventlog, 'r')
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(spamreader, None)  # skip the headers
    lastcase = ''
    line = ''
    firstline = True
    lines = []
    timeseqs = []
    timeseqs2 = []
    timeseqs3 = []
    timeseqs4 = []
    times = []
    times2 = []
    times3 = []
    times4 = []
    numlines = 0
    casestarttime = None
    lasteventtime = None
    for row in spamreader:
        try:
            t = time.strptime(row[2], "%Y-%m-%d %H:%M:%S")  # creates a datetime object from row[2]

        except ValueError as e:
            t = time.strptime(row[2], "%Y/%m/%d %H:%M:%S")  # creates a datetime object from row[2]
        # new case starts
        if row[0] != lastcase:
            casestarttime = t
            lasteventtime = t
            lastcase = row[0]
            if not firstline:
                lines.append(line)
                timeseqs.append(times)
                timeseqs2.append(times2)
                timeseqs3.append(times3)
                timeseqs4.append(times4)
            line = ''
            times = []
            times2 = []
            times3 = []
            times4 = []
            numlines += 1
        line += get_unicode_from_int(row[1])
        timesincelastevent = datetime.fromtimestamp(time.mktime(t))-datetime.fromtimestamp(time.mktime(lasteventtime))
        timesincecasestart = datetime.fromtimestamp(time.mktime(t))-datetime.fromtimestamp(time.mktime(casestarttime))
        midnight = datetime.fromtimestamp(time.mktime(t)).replace(hour=0, minute=0, second=0, microsecond=0)
        timesincemidnight = datetime.fromtimestamp(time.mktime(t))-midnight
        timediff = 86400 * timesincelastevent.days + timesincelastevent.seconds
        timediff2 = 86400 * timesincecasestart.days + timesincecasestart.seconds
        timediff3 = timesincemidnight.seconds  # this leaves only time even occured after midnight
        timediff4 = datetime.fromtimestamp(time.mktime(t)).weekday()  # day of the week
        times.append(timediff)
        times2.append(timediff2)
        times3.append(timediff3)
        times4.append(timediff4)
        lasteventtime = t
        firstline = False

    # add last case
    lines.append(line)
    timeseqs.append(times)
    timeseqs2.append(times2)
    timeseqs3.append(times3)
    timeseqs4.append(times4)
    numlines += 1

    elems_per_fold = int(round(numlines/3))
    fold1 = lines[:elems_per_fold]
    fold1_t = timeseqs[:elems_per_fold]
    fold1_t2 = timeseqs2[:elems_per_fold]
    fold1_t3 = timeseqs3[:elems_per_fold]
    fold1_t4 = timeseqs4[:elems_per_fold]

    spamwriter = csv.writer(open('output_files/folds/fold1.csv', 'w'))
    for row, timeseq in zip(fold1, fold1_t):
        spamwriter.writerow([s + '#{}'.format(t) for s, t in zip(row, timeseq)])

    fold2 = lines[elems_per_fold:2*elems_per_fold]
    fold2_t = timeseqs[elems_per_fold:2*elems_per_fold]
    fold2_t2 = timeseqs2[elems_per_fold:2*elems_per_fold]
    fold2_t3 = timeseqs3[elems_per_fold:2*elems_per_fold]
    fold2_t4 = timeseqs4[elems_per_fold:2*elems_per_fold]
    spamwriter = csv.writer(open('output_files/folds/fold2.csv', 'w'))
    for row, timeseq in zip(fold2, fold2_t):
        spamwriter.writerow([s+ '#{}'.format(t) for s, t in zip(row, timeseq)])

    fold3 = lines[2*elems_per_fold:]
    fold3_t = timeseqs[2*elems_per_fold:]
    spamwriter = csv.writer(open('output_files/folds/fold3.csv', 'w'))
    for row, timeseq in zip(fold3, fold3_t):
        spamwriter.writerow([s + '#{}'.format(t) for s, t in zip(row, timeseq)])

    lines = fold1 + fold2
    lines_t = fold1_t + fold2_t
    lines_t2 = fold1_t2 + fold2_t2
    lines_t3 = fold1_t3 + fold2_t3
    lines_t4 = fold1_t4 + fold2_t4

    step = 1
    sentences = []
    softness = 0
    next_chars = []
    lines = [x+"!" for x in lines]

    sentences_t = []
    sentences_t2 = []
    sentences_t3 = []
    sentences_t4 = []
    next_chars_t = []
    next_chars_t2 = []
    next_chars_t3 = []
    next_chars_t4 = []
    for line, line_t, line_t2, line_t3, line_t4 in zip(lines, lines_t, lines_t2, lines_t3, lines_t4):
        for i in range(0, len(line), step):
            if i == 0:
                continue

            # we add iteratively, first symbol of the line, then two first, three...
            sentences.append(line[0: i])
            sentences_t.append(line_t[0:i])
            sentences_t2.append(line_t2[0:i])
            sentences_t3.append(line_t3[0:i])
            sentences_t4.append(line_t4[0:i])
            next_chars.append(line[i])
            if i == len(line)-1:  # special case to deal time of end character
                next_chars_t.append(0)
                next_chars_t2.append(0)
                next_chars_t3.append(0)
                next_chars_t4.append(0)
            else:
                next_chars_t.append(line_t[i])
                next_chars_t2.append(line_t2[i])
                next_chars_t3.append(line_t3[i])
                next_chars_t4.append(line_t4[i])
    print('nb sequences:', len(sentences))

    print('Vectorization...')
    num_features = len(chars)+5
    print('num features: {}'.format(num_features))
    X = np.zeros((len(sentences), maxlen, num_features), dtype=np.float32)
    y_a = np.zeros((len(sentences), len(target_chars)), dtype=np.float32)
    y_t = np.zeros((len(sentences)), dtype=np.float32)
    for i, sentence in enumerate(sentences):
        leftpad = maxlen-len(sentence)
        next_t = next_chars_t[i]
        sentence_t = sentences_t[i]
        sentence_t2 = sentences_t2[i]
        sentence_t3 = sentences_t3[i]
        sentence_t4 = sentences_t4[i]
        for t, char in enumerate(sentence):
            # multiset_abstraction = Counter(sentence[:t+1])
            for c in chars:
                if c == char:  # this will encode present events to the right places
                    X[i, t+leftpad, char_indices[c]] = 1
            X[i, t+leftpad, len(chars)] = t+1
            X[i, t+leftpad, len(chars)+1] = sentence_t[t]/divisor
            X[i, t+leftpad, len(chars)+2] = sentence_t2[t]/divisor2
            X[i, t+leftpad, len(chars)+3] = sentence_t3[t]/86400
            X[i, t+leftpad, len(chars)+4] = sentence_t4[t]/7
        for c in target_chars:
            if c == next_chars[i]:
                y_a[i, target_char_indices[c]] = 1-softness
            else:
                y_a[i, target_char_indices[c]] = softness/(len(target_chars)-1)
        y_t[i] = next_t/divisor
        np.set_printoptions(threshold=np.nan)

    import tensorflow as tf
    from keras.backend.tensorflow_backend import set_session
    config = tf.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 0.5
    set_session(tf.Session(config=config))

    # build the model:
    print('Build model...')
    main_input = Input(shape=(maxlen, num_features), name='main_input')
    # train a 2-layer LSTM with one shared layer
    # the shared layer
    l1 = LSTM(100, consume_less='gpu', init='glorot_uniform', return_sequences=True, dropout_W=0.2)(main_input)
    b1 = BatchNormalization()(l1)
    # the layer specialized in activity prediction
    l2_1 = LSTM(100, consume_less='gpu', init='glorot_uniform', return_sequences=False, dropout_W=0.2)(b1)
    b2_1 = BatchNormalization()(l2_1)
    # the layer specialized in time prediction
    l2_2 = LSTM(100, consume_less='gpu', init='glorot_uniform', return_sequences=False, dropout_W=0.2)(b1)
    b2_2 = BatchNormalization()(l2_2)
    act_output = Dense(len(target_chars), activation='softmax', init='glorot_uniform', name='act_output')(b2_1)
    time_output = Dense(1, init='glorot_uniform', name='time_output')(b2_2)

    model = Model(input=[main_input], output=[act_output, time_output])

    opt = Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=1e-08, schedule_decay=0.004, clipvalue=3)

    model.compile(loss={'act_output': 'categorical_crossentropy', 'time_output': 'mae'}, optimizer=opt)
    early_stopping = EarlyStopping(monitor='val_loss', patience=42)
    path_to_model = 'output_files/final_experiments/models/CF/' + eventlog[:-4] + '/model_{epoch:02d}-{val_loss:.2f}.h5'
    model_checkpoint = ModelCheckpoint(path_to_model, monitor='val_loss', verbose=0, save_best_only=True,
                                       save_weights_only=False, mode='auto')
    lr_reducer = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=10, verbose=0, mode='auto', epsilon=0.0001,
                                   cooldown=0, min_lr=0)

    model.fit(X, {'act_output': y_a, 'time_output': y_t}, validation_split=0.2, verbose=2, callbacks=[early_stopping,
                                                                                                      model_checkpoint,
                                                                                                      lr_reducer],
              batch_size=maxlen, nb_epoch=300)
