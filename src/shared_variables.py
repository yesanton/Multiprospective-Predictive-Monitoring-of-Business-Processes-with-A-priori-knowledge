"""
This file was created in order to bring
common variables and functions into one file to make
code more clear

Author: Anton Yeshchenko
"""

ascii_offset = 161
beam_size = 5
prefix_size_pred_to = None
prefix_size_pred_from = None


def get_unicode_from_int(ch):
    return unichr(int(ch) + ascii_offset)


def get_int_from_unicode(unch):
    return int(ord(unch)) - ascii_offset


# noinspection PyUnboundLocalVariable,PyShadowingNames,PyUnusedLocal
def activate_settings(log_number, formula_type):

    if log_number == 1:
        eventlog = "10x5_1S.csv"
        # path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
        #                      'priori-knowledge/src/output_files/final_experiments/models/CF/10x5_1S/model_11-1.23.h5'
        path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/10x5_1S/model_12-1.64.h5'
        if formula_type == "STRONG":
            formula = " []( ( \"6\" -> <>( \"3\" ) ) )  /\ <>\"6\" "
        if formula_type == "WEAK":
            formula = "<>(\"6\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 4

    elif log_number == 2:
        eventlog = "10x5_1W.csv"
        # path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
        #                      'priori-knowledge/src/output_files/final_experiments/models/CF/10x5_1W/model_18-1.07.h5'
        path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/10x5_1W/model_22-1.71.h5'
        if formula_type == "STRONG":
            formula = " []( ( \"6\" -> <>( \"3\" ) ) )  /\ <>\"6\" "
        if formula_type == "WEAK":
            formula = "<>(\"6\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

    elif log_number == 3:
        eventlog = "10x5_3S.csv"
        # path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
        #                      'priori-knowledge/src/output_files/final_experiments/models/CF/10x5_3S/model_04-1.14.h5'
        path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/10x5_3S/model_21-1.44.h5'
        if formula_type == "STRONG":
            formula = " []( ( \"6\" -> <>( \"1\" ) ) )  /\ <>\"6\" /\ " \
                      " []( ( \"8\" -> <>( \"1\" ) ) )  /\ <>\"8\" /\ "
        if formula_type == "WEAK":
            formula = "<>(\"6\") /\ <>(\"8\")"

    elif log_number == 4:
        eventlog = "10x5_3W.csv"
        # path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
        #                      'priori-knowledge/src/output_files/final_experiments/models/CF/10x5_3W/model_05-1.10.h5'
        path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/10x5_3W/model_11-1.55.h5'
        if formula_type == "STRONG":
            formula = " []( ( \"6\" -> <>( \"1\" ) ) )  /\ <>\"6\" /\ " \
                      " []( ( \"8\" -> <>( \"1\" ) ) )  /\ <>\"8\" /\ "
        if formula_type == "WEAK":
            formula = "<>(\"8\") /\ <>(\"7\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

    return eventlog, path_to_model_file, beam_size, prefix_size_pred_from, prefix_size_pred_to, formula


eventlog = "10x5_3W.csv"
path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/declare_models/final_experiments/10x5_3W.xml'
