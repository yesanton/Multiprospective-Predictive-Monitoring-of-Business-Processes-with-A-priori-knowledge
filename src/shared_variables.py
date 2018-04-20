"""
This file was created in order to bring
common variables and functions into one file to make
code more clear

Author: Anton Yeshchenko
"""
# evaluate_suffix_start_from = 2
# evaluate_suffix_end = 3

ascii_offset = 161
beam_size = None
prefix_size_pred_to = None
prefix_size_pred_from = None


def getUnicode_fromInt(ch):
    return unichr(int(ch) + ascii_offset)


def getInt_fromUnicode(unch):
    return int(ord(unch)) - ascii_offset


# noinspection PyUnboundLocalVariable,PyShadowingNames,PyUnusedLocal
def activateSettings(logNumber, formulaType):
    if logNumber == 0:
        eventlog = "bpi_11.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_11/' \
                             'model.h5'
        median = 31
        prefix_size_pred_from = median / 2 - 2
        prefix_size_pred_to = median / 2 + 2
        # BPI11_strong
        if formulaType == "STRONG":
            formula = "[]( ( \"7\" -> <>( \"15\" ) ) )  /\  []( ( \"0\" -> <>( \"1\" ) ) ) /\ <>\"0\" /\ <>\"7\" " \
                      "/\  []( ( \"8\" -> <>( \"10\" ) ) ) /\ <>\"8\" "
        # BPI11_weak
        if formulaType == "WEAK":
            formula = "<>(\"0\") /\ <>(\"15\") /\ <>(\"11\")"
    # elif logNumber == 1:
    #     eventlog = "bpi_12_w_no_repeat.csv"
    #     path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/
    #     models_bpi_12_norep/model.h5'
    #     median = 4
    elif logNumber == 2:
        eventlog = "bpi_12_w.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/' \
                             'models_bpi_12_w/model_23-1.67.h5'
        median = 6
        prefix_size_pred_from = 2
        prefix_size_pred_to = 6
        if formulaType == "STRONG":
            formula = " []( ( \"3\" -> <>( \"5\" ) ) ) /\ <>\"3\" "  # /\ []( ( \"1\" -> <>( \"3\" ) ) )
            # /\ <>\"1\" "# /\
        if formulaType == "WEAK":
            formula = "<>(\"3\")"

    elif logNumber == 3:
        eventlog = "bpi_13_incidents.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/' \
                             'models_bpi_13_incidents/model.h5'
        median = 6
        if formulaType == "STRONG":
            formula = " []( ( \"3\" -> <>( \"5\" ) ) ) /\ <>\"3\" /\ []( ( \"1\" -> <>( \"3\" ) ) )  /\ <>\"1\" "  # /\
        if formulaType == "WEAK":
            formula = "<>(\"5\") /\ <>(\"3\")"
        prefix_size_pred_from = 2
        prefix_size_pred_to = 6

    elif logNumber == 4:
        eventlog = "bpi_17_no_group_50k.csv"
        path_to_model_file = '/home/kaur/Documents/FBK/Process-Sequence-Prediction-with-A-priori-knowledge-master/src' \
                             '/output_files/models_bpi_17_group_50k/model_15-2.33.h5'
        median = 17
        if formulaType == "STRONG":
            formula = "[]( ( \"5\" -> <>( \"6\" ) ) )  /\ <>\"5\" "
        if formulaType == "WEAK":
            formula = "<>(\"5\")"
        prefix_size_pred_from = median / 2 - 2
        prefix_size_pred_to = median / 2 + 2

    elif logNumber == 5:
        eventlog = "env_permit.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/' \
                             'models_env_permit/model.h5'
        median = 43
        prefix_size_pred_from = median / 2 - 2
        prefix_size_pred_to = median / 2 + 2
        if formulaType == "STRONG":
            formula = " []( ( \"114\" -> <>( \"131\" ) ) ) /\ <>\"114\" /\  []( ( \"116\" -> <>( \"136\" ) ) ) " \
                      "/\ <>\"116\""  # "[]( ( \"1\" -> <>( \"8\" ) ) )  /\ <>\"1\" "# /\
        if formulaType == "WEAK":
            formula = "<>(\"114\") /\ <>(\"116\")"

    elif logNumber == 6:
        eventlog = "helpdesk.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/' \
                             'models_helpdesk/model.h5'
        median = 4
        if formulaType == "STRONG":
            formula = " []( ( \"8\" -> <>( \"6\" ) ) ) /\ <>\"8\""  # "[]( ( \"1\" -> <>( \"8\" ) ) )  /\ <>\"1\" "# /\
        if formulaType == "WEAK":
            formula = "<>(\"8\")"

        prefix_size_pred_from = 2
        prefix_size_pred_to = 6

    elif logNumber == 7:
        eventlog = "helpdesk_mini_1000_rows.csv"
        path_to_model_file = '/home/kaur/Documents/FBK/Process-Sequence-Prediction-with-A-priori-knowledge-master/' \
                             'src/output_files/models_helpdesk_mini_1000_rows/model_49-1.34.h5'
        median = 4
        if formulaType == "STRONG":
            formula = " []( ( \"8\" -> <>( \"6\" ) ) ) /\ <>\"8\""  # "[]( ( \"1\" -> <>( \"8\" ) ) )  /\ <>\"1\" "# /\
        if formulaType == "WEAK":
            formula = "<>(\"8\")"

        prefix_size_pred_from = 2
        prefix_size_pred_to = 6

    elif logNumber == 8:
        eventlog = "bpi_14_detail_incident_with_group.csv"
        path_to_model_file = '/home/kaur/Documents/FBK/Process-Sequence-Prediction-with-A-priori-knowledge-master/' \
                             'src/output_files/models_group/model_70-837.72.h5'
        median = 4
        if formulaType == "STRONG":
            formula = " []( ( \"8\" -> <>( \"6\" ) ) ) /\ <>\"8\""
        if formulaType == "WEAK":
            formula = "<>(\"8\")"

        prefix_size_pred_from = 2
        prefix_size_pred_to = 6

    elif logNumber == 9:
        eventlog = "test_log7_model2_630_converted.csv"
        path_to_model_file = '/home/kaur/Documents/SharedFolder_Azure/models_no_group/' \
                             'models_test_log7_model2_630_converted/model_13-1.62.h5'
        median = 6
        if formulaType == "STRONG":
            formula = " []( ( \"8\" -> <>( \"6\" ) ) ) /\ <>\"8\""
        if formulaType == "WEAK":
            formula = "<>(\"8\")"

        prefix_size_pred_from = 2
        prefix_size_pred_to = 6

    elif logNumber == 10:
        # experiment 1
        eventlog = "bpi_17_group_50k.csv"
        path_to_model_file = '/media/sf_SharedFolder/fbk/Process-Sequence-Prediction-with-A-priori-knowledge-master/' \
                             'src/output_files/models_bpi_17_group_50k/model_15-2.33.h5'
        median = 7
        if formulaType == "STRONG":
            formula = " []( ( \"12\" -> X( \"13\" ) ) )"
        if formulaType == "WEAK":
            formula = "<>(\"8\")"

        prefix_size_pred_from = 5
        prefix_size_pred_to = 8

    beam_size = 2
    return eventlog, path_to_model_file, beam_size, prefix_size_pred_from, prefix_size_pred_to, formula


eventlog = "bpi_17_group_50k.csv"
path_to_declare_model_file = '/media/sf_SharedFolder/declaremodels/accommodated_models/bpi_2017_50k_experiment_2.xml'
# eventlog = "helpdesk_mini_1000_rows.csv"
# path_to_model_file = "/home/kaur/Documents/FBK/Process-Sequence-Prediction-with-A-priori-knowledge-master/src/" \
#                      "output_files/models/model.h5"
