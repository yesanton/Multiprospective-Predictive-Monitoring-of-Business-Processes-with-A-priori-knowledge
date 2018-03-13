"""
this file is build based on the code found in evaluate_suffix_and_remaining_time.py

here the beam search (with breath-first-search) is implemented, to find compliant prediction

Author: Anton Yeshchenko
"""
from __future__ import division
from Queue import Queue, PriorityQueue
from datetime import timedelta
from itertools import izip
from jellyfish._jellyfish import damerau_levenshtein_distance
from keras.models import load_model
from sklearn import metrics
from inspect import getsourcefile
from datetime import datetime, timedelta
from shared_variables import activateSettings, path_to_declare_model_file
from formula_verificator import verify_formula_as_compliant, verify_with_data
from support_scripts.prepare_data_resource import amplify, getSymbolAmpl, selectFormulaVerifiedTraces, \
                                               encode, prepare_testing_data

import csv
import numpy as np
import time
import distance
import os.path
import sys


current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)


def runExperiments(logIdentificator, formulaType):

    # get variables from the shared variables file
    eventlog, \
        path_to_model_file, \
        beam_size, \
        prefix_size_pred_from, \
        prefix_size_pred_to, \
        formula = activateSettings(logIdentificator, formulaType)

    # prepare the data
    lines, \
        lines_id, \
        lines_group, \
        lines_t, \
        lines_t2, \
        lines_t3, \
        lines_t4, \
        maxlen, \
        chars, \
        chars_group, \
        char_indices, \
        char_indices_group, \
        divisor, \
        divisor2, \
        divisor3, \
        predict_size, \
        target_indices_char, \
        target_indices_char_group,\
        target_char_indices, \
        target_char_indices_group = prepare_testing_data(eventlog)

    # this is the beam stack size, means how many "best" alternatives will be stored
    one_ahead_gt = []
    one_ahead_pred = []

    # find cycles and modify the probability functionality goes here
    stop_symbol_probability_amplifier_current = 1

    # load model, set this to the model generated by train.py
    model = load_model(path_to_model_file)

    # Get the predicted group symbol
    def getSymbolGroup(predictions, ith_best=0):
        i = np.argsort(predictions)[len(predictions) - ith_best - 1]
        return target_indices_char_group[i]

    class NodePrediction:
        def __init__(self, data, trace_id, cropped_line, cropped_line_group, cropped_times,
                     total_predicted_time, probability_of=0):
            self.trace_id = trace_id
            self.data = data
            self.cropped_line = cropped_line
            self.cropped_line_group = cropped_line_group
            self.cropped_times = cropped_times
            self.total_predicted_time = total_predicted_time
            self.probability_of = probability_of

    # make predictions
    with open('output_files/results/'+formulaType+'/suffix_and_remaining_time3_%s' % eventlog, 'wb') as csvfile:

        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # headers for the new file
        spamwriter.writerow(["Prefix length",
                             "Ground truth",
                             "Predicted",
                             "Levenshtein",
                             "Damerau",
                             "Jaccard",
                             "Ground truth times",
                             "Predicted times",
                             "RMSE",
                             "MAE",
                             "Median AE",
                             "Ground Truth Group",
                             "Predicted Group",
                             "Levenshtein Group"])

        # make predictions for different prefix sizes as specified in 'shared variables'
        for prefix_size in range(prefix_size_pred_from, prefix_size_pred_to):

            lines_s, \
                lines_id_s, \
                lines_group_s, \
                lines_t_s, \
                lines_t2_s, \
                lines_t3_s, \
                lines_t4_s = selectFormulaVerifiedTraces(path_to_declare_model_file,
                                                         lines,
                                                         lines_id,
                                                         lines_group,
                                                         lines_t,
                                                         lines_t2,
                                                         lines_t3,
                                                         lines_t4,
                                                         prefix_size)

            for line, line_id, line_group, times, times2, times3, times4 in izip(lines_s,
                                                                                 lines_id_s,
                                                                                 lines_group_s,
                                                                                 lines_t_s,
                                                                                 lines_t2_s,
                                                                                 lines_t3_s,
                                                                                 lines_t4_s):
                times.append(0)
                cropped_line_id = line_id
                cropped_line = ''.join(line[:prefix_size])
                cropped_line_group = ''.join(line_group[:prefix_size])
                cropped_times = times[:prefix_size]
                cropped_times3 = times3[:prefix_size]
                cropped_times4 = times4[:prefix_size]

                if len(times2) < prefix_size:
                    continue  # make no prediction for this case, since this case has ended already

                # initialize root of the tree for beam search
                total_predicted_time_initialization = 0
                search_node_root = NodePrediction(encode(cropped_line, cropped_line_group, cropped_times,
                                                         cropped_times3, maxlen, chars, chars_group,
                                                         char_indices, char_indices_group, divisor, divisor2),
                                                  cropped_line_id,
                                                  cropped_line,
                                                  cropped_line_group,
                                                  cropped_times4,
                                                  total_predicted_time_initialization)

                ground_truth = ''.join(line[prefix_size:prefix_size+predict_size])
                ground_truth_group = ''.join(line_group[prefix_size:prefix_size+predict_size])
                ground_truth_t = times2[prefix_size-1]
                case_end_time = times2[len(times2)-1]
                ground_truth_t = case_end_time-ground_truth_t

                queue_next_steps = PriorityQueue()
                queue_next_steps.put((-search_node_root.probability_of, search_node_root))

                queue_next_steps_future = PriorityQueue()
                start_of_the_cycle_symbol = " "
                found_sattisfying_constraint = False
                current_prediction_premis = None

                for i in range(predict_size):
                    for k in range(beam_size):
                        if queue_next_steps.empty():
                            break

                        _, current_prediction_premis = queue_next_steps.get()

                        if not found_sattisfying_constraint:
                            if verify_with_data(path_to_declare_model_file,
                                                current_prediction_premis.trace_id,
                                                current_prediction_premis.cropped_line,
                                                current_prediction_premis.cropped_line_group,
                                                current_prediction_premis.cropped_times,
                                                prefix_size):
                                # the formula verified and we can just finish the predictions
                                # beam size is 1 because predict only sequence of events
                                beam_size = 1
                                # overwrite new queue
                                queue_next_steps_future = PriorityQueue()
                                found_sattisfying_constraint = True

                        enc = current_prediction_premis.data
                        temp_cropped_line = current_prediction_premis.cropped_line
                        y = model.predict(enc, verbose=0)  # make predictions
                        # split predictions into seperate activity and time predictions
                        y_char = y[0][0]
                        y_group = y[1][0]
                        y_t = y[2][0][0]

                        if y_t < 0:
                            y_t = 0
                        cropped_times.append(y_t)

                        if not i == 0:
                            stop_symbol_probability_amplifier_current, start_of_the_cycle_symbol = \
                                amplify(temp_cropped_line)

                        # in not reached, function :choose_next_top_descendant: will backtrack
                        y_t = y_t * divisor3
                        cropped_times3.append(cropped_times3[-1] + timedelta(seconds=y_t))

                        for j in range(beam_size):
                            temp_prediction = getSymbolAmpl(y_char, target_indices_char,
                                                            target_char_indices, start_of_the_cycle_symbol,
                                                            stop_symbol_probability_amplifier_current, j)

                            temp_prediction_group = getSymbolGroup(y_group)

                            # end of case was just predicted, therefore, stop predicting further into the future
                            if temp_prediction == '!':
                                if verify_formula_as_compliant(temp_cropped_line, formula, prefix_size):
                                    one_ahead_pred.append(current_prediction_premis.total_predicted_time)
                                    one_ahead_gt.append(ground_truth_t)
                                    stop_symbol_probability_amplifier_current = 1
                                    print('! predicted, end case')
                                    queue_next_steps = PriorityQueue()
                                    break
                                else:
                                    continue

                            temp_cropped_line = current_prediction_premis.cropped_line + temp_prediction
                            temp_cropped_line_group = \
                                current_prediction_premis.cropped_line_group + temp_prediction_group

                            # adds a fake timestamp to the list
                            t = time.strptime(cropped_times4[-1], "%Y-%m-%d %H:%M:%S")
                            new_timestamp = datetime.fromtimestamp(time.mktime(t)) + timedelta(0, 2000)
                            cropped_times4.append(new_timestamp.strftime("%Y-%m-%d %H:%M:%S"))

                            temp_total_predicted_time = current_prediction_premis.total_predicted_time + y_t
                            temp_state_data = encode(temp_cropped_line,
                                                     temp_cropped_line_group,
                                                     cropped_times,
                                                     cropped_times3,
                                                     maxlen,
                                                     chars,
                                                     chars_group,
                                                     char_indices,
                                                     char_indices_group,
                                                     divisor,
                                                     divisor2)
                            probability_this = np.sort(y_char)[len(y_char) - 1 - j]

                            temp = NodePrediction(temp_state_data,
                                                  cropped_line_id,
                                                  temp_cropped_line,
                                                  temp_cropped_line_group,
                                                  cropped_times4,
                                                  temp_total_predicted_time,
                                                  current_prediction_premis.probability_of + np.log(probability_this))

                            queue_next_steps_future.put((-temp.probability_of, temp))

                    queue_next_steps = queue_next_steps_future
                    queue_next_steps_future = PriorityQueue()

                if current_prediction_premis is None:
                    print "Cannot find any trace that is compliant with formula given current beam size"
                    break

                output = []

                if current_prediction_premis is None:
                    predicted = u""
                    predicted_group = u""
                    total_predicted_time = 0
                else:
                    predicted = (current_prediction_premis.cropped_line[prefix_size:])
                    predicted_group = (current_prediction_premis.cropped_line_group[prefix_size:])
                    total_predicted_time = current_prediction_premis.total_predicted_time

                if len(ground_truth) > 0:
                    output.append(prefix_size)
                    output.append(unicode(ground_truth).encode("utf-8"))
                    output.append(unicode(predicted).encode("utf-8"))
                    output.append(1 - distance.nlevenshtein(predicted, ground_truth))
                    dls = 1 - (damerau_levenshtein_distance(unicode(predicted),
                                                            unicode(ground_truth)) / max(len(predicted),
                                                                                         len(ground_truth)))
                    # we encountered problems with Damerau-Levenshtein Similarity on some
                    # linux machines where the default character encoding of the operating system
                    # caused it to be negative, this should never be the case
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
