"""
This file was created in order to bring
common variables and functions into one file to make
code more clear

"""

ascii_offset = 161
beam_size = 3
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
        prefix_size_pred_to = 7

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
            formula = "<>(\"6\") /\ <>(\"7\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

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

    elif log_number == 5:
        eventlog = "5x5_1W.csv"
        # path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
        #                      'priori-knowledge/src/output_files/final_experiments/models/CF/5x5_1W/model_23-1.12.h5'
        path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/5x5_1W/model_15-1.69.h5'
        if formula_type == "STRONG":
            formula = " []( ( \"3\" -> <>( \"4\" ) ) )  /\ <>\"3\" "
        if formula_type == "WEAK":
            formula = "<>(\"3\")"

        prefix_size_pred_from = 2
        prefix_size_pred_to = 6

    elif log_number == 6:
        eventlog = "5x5_1S.csv"
        # path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
        #                      'priori-knowledge/src/output_files/final_experiments/models/CF/5x5_1S/model_17-1.16.h5'
        path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/5x5_1S/model_35-1.83.h5'
        if formula_type == "STRONG":
            formula = " []( ( \"3\" -> <>( \"4\" ) ) )  /\ <>\"3\" "
        if formula_type == "WEAK":
            formula = "<>(\"3\")"

        prefix_size_pred_from = 2
        prefix_size_pred_to = 6

    elif log_number == 7:
        eventlog = "5x5_3W.csv"
        # path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
        #                      'priori-knowledge/src/output_files/final_experiments/models/CF/5x5_3W/model_18-1.23.h5'
        path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/5x5_3W/model_10-1.77.h5'
        if formula_type == "STRONG":
            formula = " []( ( \"4\" -> <>( \"3\" ) ) )  /\ <>\"4\" /\ " \
                      " []( ( \"3\" -> <>( \"0\" ) ) )  /\ <>\"3\" /\ "
        if formula_type == "WEAK":
            formula = "<>(\"4\") /\ <>(\"3\")"

        prefix_size_pred_from = 2
        prefix_size_pred_to = 4

    elif log_number == 8:
        eventlog = "5x5_3S.csv"
        # path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
        #                      'priori-knowledge/src/output_files/final_experiments/models/CF/5x5_3S/model_39-1.32.h5'
        path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/5x5_3S/model_31-1.73.h5'
        if formula_type == "STRONG":
            formula = " []( ( \"4\" -> <>( \"3\" ) ) )  /\ <>\"4\" /\ " \
                      " []( ( \"3\" -> <>( \"0\" ) ) )  /\ <>\"3\" /\ "
        if formula_type == "WEAK":
            formula = "<>(\"4\") /\ <>(\"3\")"

        prefix_size_pred_from = 2
        prefix_size_pred_to = 4

    elif log_number == 9:
        eventlog = "10x20_1W.csv"
        # path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
        #                      'priori-knowledge/src/output_files/final_experiments/models/CF/10x20_1W/model_04-1.09.h5'
        path_to_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/10x20_1W/model_03-1.64.h5'
        if formula_type == "STRONG":
            formula = " []( ( \"8\" -> <>( \"9\" ) ) )  /\ <>\"8\" "
        if formula_type == "WEAK":
            formula = "<>(\"9\")"

        prefix_size_pred_from = 2
        prefix_size_pred_to = 6

    elif log_number == 10:
        eventlog = "10x20_1S.csv"
        path_to_model_file_CF = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CF/10x20_1S/model_00-0.99.h5'
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/10x20_1S/model_00-1.55.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/10x20_1S.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"8\" -> <>( \"9\" ) ) )  /\ <>\"8\" "
        if formula_type == "WEAK":
            formula = "<>(\"9\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

    elif log_number == 11:
        eventlog = "10x20_3W.csv"
        path_to_model_file_CF = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CF/10x20_3W/model_06-1.17.h5'
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/10x20_3W/model_05-1.63.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/10x20_3W.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"9\" -> <>( \"7\" ) ) )  /\ <>\"9\" /\ " \
                      " []( ( \"8\" -> <>( \"6\" ) ) )  /\ <>\"8\" /\ " \
                      " []( ( \"7\" -> <>( \"5\" ) ) )  /\ <>\"7\""
        if formula_type == "WEAK":
            formula = "<>(\"9\") /\ <>(\"6\") /\ <>(\"8\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

    elif log_number == 12:
        eventlog = "10x20_3S.csv"
        path_to_model_file_CF = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CF/10x20_3S/model_24-1.09.h5'
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                             'priori-knowledge/src/output_files/final_experiments/models/CFR/10x20_3S/model_06-1.54.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/10x20_3S.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"9\" -> <>( \"7\" ) ) )  /\ <>\"9\" /\ " \
                      " []( ( \"8\" -> <>( \"6\" ) ) )  /\ <>\"8\" /\ " \
                      " []( ( \"7\" -> <>( \"5\" ) ) )  /\ <>\"7\""
        if formula_type == "WEAK":
            formula = "<>(\"9\") /\ <>(\"6\") /\ <>(\"8\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

    elif log_number == 13:
        eventlog = "10x2_1W.csv"
        path_to_model_file_CF = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                                'priori-knowledge/src/output_files/final_experiments/models/CF/10x2_1W/model_70-1.14.h5'
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                                 'priori-knowledge/src/output_files/final_experiments/models/CFR/10x2_1W/model_21-1.77.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/10x2_1W.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"6\" -> <>( \"2\" ) ) )  /\ <>\"6\""
        if formula_type == "WEAK":
            formula = "<>(\"2\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

    elif log_number == 14:
        eventlog = "10x2_1S.csv"
        path_to_model_file_CF = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                                'priori-knowledge/src/output_files/final_experiments/models/CF/10x2_1S/model_02-1.83.h5'
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A' \
                                 '-priori-knowledge/src/output_files/final_experiments/models/CFR/10x2_1S/model_01-1.94.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/10x2_1S.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"6\" -> <>( \"2\" ) ) )  /\ <>\"6\""
        if formula_type == "WEAK":
            formula = "<>(\"2\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

    elif log_number == 15:
        eventlog = "10x2_3W.csv"
        path_to_model_file_CF = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                                'priori-knowledge/src/output_files/final_experiments/models/CF/10x2_3W/model_19-1.12.h5'
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A' \
                                 '-priori-knowledge/src/output_files/final_experiments/models/CFR/10x2_3W/model_24-1.54.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/10x2_3W.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"9\" -> <>( \"3\" ) ) )  /\ <>\"9\" /\ " \
                      " []( ( \"7\" -> <>( \"3\" ) ) )  /\ <>\"7\""
        if formula_type == "WEAK":
            formula = "<>(\"8\") /\ <>(\"7\")"

        prefix_size_pred_from = 5
        prefix_size_pred_to = 7

    elif log_number == 16:
        eventlog = "10x2_3S.csv"
        path_to_model_file_CF = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                                'priori-knowledge/src/output_files/final_experiments/models/CF/10x2_3S/model_09-1.56.h5'
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A' \
                                 '-priori-knowledge/src/output_files/final_experiments/models/CFR/10x2_3S/model_03-1.78.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/10x2_3S.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"9\" -> <>( \"3\" ) ) )  /\ <>\"9\" /\ " \
                      " []( ( \"7\" -> <>( \"3\" ) ) )  /\ <>\"7\""
        if formula_type == "WEAK":
            formula = "<>(\"8\") /\ <>(\"7\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

    elif log_number == 17:
        eventlog = "50x5_1W.csv"
        path_to_model_file_CF = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                                'priori-knowledge/src/output_files/final_experiments/models/CF/50x5_1W/model_01-1.25.h5'
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A' \
                                 '-priori-knowledge/src/output_files/final_experiments/models/CFR/50x5_1W/model_01-1.58.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/50x5_1W.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"7\" -> <>( \"8\" ) ) )  /\ <>\"7\""
        if formula_type == "WEAK":
            formula = "<>(\"7\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

    elif log_number == 18:
        eventlog = "50x5_1S.csv"
        path_to_model_file_CF = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                                'priori-knowledge/src/output_files/final_experiments/models/CF/50x5_1S/model_01-1.21.h5'
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A' \
                                 '-priori-knowledge/src/output_files/final_experiments/models/CFR/50x5_1S/model_01-1.45.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/50x5_1S.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"7\" -> <>( \"8\" ) ) )  /\ <>\"7\""
        if formula_type == "WEAK":
            formula = "<>(\"7\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

    elif log_number == 19:
        eventlog = "50x5_3W.csv"
        path_to_model_file_CF = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                                'priori-knowledge/src/output_files/final_experiments/models/CF/50x5_3W/model_09-1.07.h5'
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A' \
                                 '-priori-knowledge/src/output_files/final_experiments/models/CFR/50x5_3W/model_02-1.28.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/50x5_3W.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"9\" -> <>( \"7\" ) ) )  /\ <>\"9\" /\ " \
                      " []( ( \"8\" -> <>( \"7\" ) ) )  /\ <>\"8\""
        if formula_type == "WEAK":
            formula = "<>(\"9\") /\ <>(\"7\")"

        prefix_size_pred_from = 3
        prefix_size_pred_to = 7

    elif log_number == 20:
        eventlog = "50x5_3S.csv"
        path_to_model_file_CF = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
                                'priori-knowledge/src/output_files/final_experiments/models/CF/50x5_3S/model_04-1.38.h5'
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A' \
                                 '-priori-knowledge/src/output_files/final_experiments/models/CFR/50x5_3S/model_07-1.52.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/50x5_3S.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"9\" -> <>( \"7\" ) ) )  /\ <>\"9\" /\ " \
                      " []( ( \"8\" -> <>( \"7\" ) ) )  /\ <>\"8\""
        if formula_type == "WEAK":
            formula = "<>(\"9\") /\ <>(\"7\")"

        prefix_size_pred_from = 6
        prefix_size_pred_to = 7

    elif log_number == 21:
        eventlog = "BPI2017_50k.csv"
        path_to_model_file_CF = ''
        path_to_model_file_CFR = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A' \
                                 '-priori-knowledge/src/output_files/final_experiments/models/CFR/BPI2017_50k/' \
                                 'model_14-2.26.h5'
        path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-' \
                                     'with-A-priori-knowledge/src/declare_models/final_experiments/BPI2017_STRONG.xml'
        if formula_type == "STRONG":
            formula = " []( ( \"17\" -> <>( \"18\" ) ) )  /\ <>\"17\""
        if formula_type == "WEAK":
            formula = "<>(\"17\")"

        prefix_size_pred_from = 6
        prefix_size_pred_to = 9

    return eventlog, path_to_model_file_CF, path_to_model_file_CFR, path_to_declare_model_file, \
        beam_size, prefix_size_pred_from, prefix_size_pred_to, formula


eventlog ="BPI2017_50k.csv"
# path_to_declare_model_file = '/home/kaur/Documents/Incremental-Predictive-Monitoring-of-Business-Processes-with-A-' \
#                              'priori-knowledge/src/declare_models/final_experiments/10x20_3W.xml'
