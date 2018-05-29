"""
This file was created to manage running of experiments.

## settings are in the shared variables file
Author; Anton Yeshchenko
"""


# This will run whole set of experiments
# from inference_algorithms import _6_evaluate_beseline_SUFFIX_only
# from inference_algorithms import _9_cycl_SUFFIX_only
# from inference_algorithms import _10_cycl_back_SUFFIX_only
# from inference_algorithms import _11_cycl_pro_SUFFIX_only
# from inference_algorithms import _11_cycl_pro_SUFFIX_resource_declare

# from inference_algorithms import _6_evaluate_baseline_SUFFIX_only
# from inference_algorithms import _11_cycl_pro_SUFFIX_only
#
from inference_algorithms import _6_evaluate_baseline_SUFFIX_and_group
from inference_algorithms import _11_cycl_pro_SUFFIX_resource_LTL
# from inference_algorithms import _11_cycl_pro_SUFFIX_declare_smart_queue

# from shared_variables import activateSettings, eventlog
# from train import train
# from train_with_data import train_with_data
# from formula_verificator import verify_with_data
# from support_scripts.generate_xeslog import generateXesLog

# formula_used = "WEAK"
# formula_used = "STRONG"
# logNumber = 11

# train()
# train_with_data()
# _6_evaluate_beseline_SUFFIX_only.runExperiments()
# _9_cycl_SUFFIX_only.py.runExperiments()
# _10_cycl_back_SUFFIX_only.runExperiments()
# _6_evaluate_beseline_SUFFIX_only.run_experiments(logNumber, formula_used)
# _9_cycl_SUFFIX_only.runExperiments(logNumber,formula_used)
# _10_cycl_back_SUFFIX_only.runExperiments(logNumber,formula_used)
# _11_cycl_pro_SUFFIX_only.run_experiments(logNumber, formula_used)
# _11_cycl_pro_SUFFIX_resource_declare.run_experiments(logNumber, formula_used)
#
# _6_evaluate_baseline_SUFFIX_only.run_experiments(12, "STRONG", "CF")
# _6_evaluate_baseline_SUFFIX_only.run_experiments(13, "WEAK", "CF")
# _6_evaluate_baseline_SUFFIX_only.run_experiments(14, "STRONG", "CF")
# _6_evaluate_baseline_SUFFIX_only.run_experiments(15, "WEAK", "CF")
# _6_evaluate_baseline_SUFFIX_only.run_experiments(16, "STRONG", "CF")
# _6_evaluate_baseline_SUFFIX_only.run_experiments(17, "WEAK", "CF")
# _6_evaluate_baseline_SUFFIX_only.run_experiments(18, "STRONG", "CF")
# _6_evaluate_baseline_SUFFIX_only.run_experiments(19, "WEAK", "CF")
# _6_evaluate_baseline_SUFFIX_only.run_experiments(20, "STRONG", "CF")

# run again
# _11_cycl_pro_SUFFIX_only.run_experiments(12, "STRONG", "CF")

# _11_cycl_pro_SUFFIX_only.run_experiments(13, "WEAK", "CF")
# _11_cycl_pro_SUFFIX_only.run_experiments(14, "STRONG", "CF")
# _11_cycl_pro_SUFFIX_only.run_experiments(15, "WEAK", "CF")
# _11_cycl_pro_SUFFIX_only.run_experiments(16, "STRONG", "CF")
# _11_cycl_pro_SUFFIX_only.run_experiments(17, "WEAK", "CF")
# _11_cycl_pro_SUFFIX_only.run_experiments(18, "STRONG", "CF")
# _11_cycl_pro_SUFFIX_only.run_experiments(19, "WEAK", "CF")
# _11_cycl_pro_SUFFIX_only.run_experiments(20, "STRONG", "CF")

# _6_evaluate_baseline_SUFFIX_and_group.run_experiments(12, "STRONG", "CFR")
# _6_evaluate_baseline_SUFFIX_and_group.run_experiments(13, "WEAK", "CFR")
# _6_evaluate_baseline_SUFFIX_and_group.run_experiments(14, "STRONG", "CFR")
# _6_evaluate_baseline_SUFFIX_and_group.run_experiments(15, "WEAK", "CFR")
# _6_evaluate_baseline_SUFFIX_and_group.run_experiments(16, "STRONG", "CFR")
# _6_evaluate_baseline_SUFFIX_and_group.run_experiments(17, "WEAK", "CFR")
# _6_evaluate_baseline_SUFFIX_and_group.run_experiments(18, "STRONG", "CFR")
# _6_evaluate_baseline_SUFFIX_and_group.run_experiments(19, "WEAK", "CFR")
# _6_evaluate_baseline_SUFFIX_and_group.run_experiments(20, "STRONG", "CFR")

# run again
# _11_cycl_pro_SUFFIX_resource_LTL.run_experiments(12, "STRONG", "CFR")

# _11_cycl_pro_SUFFIX_resource_LTL.run_experiments(13, "WEAK", "CFR")
# _11_cycl_pro_SUFFIX_resource_LTL.run_experiments(14, "STRONG", "CFR")
# _11_cycl_pro_SUFFIX_resource_LTL.run_experiments(15, "WEAK", "CFR")
# _11_cycl_pro_SUFFIX_resource_LTL.run_experiments(16, "STRONG", "CFR")
# _11_cycl_pro_SUFFIX_resource_LTL.run_experiments(17, "WEAK", "CFR")
# _11_cycl_pro_SUFFIX_resource_LTL.run_experiments(18, "STRONG", "CFR")
# _11_cycl_pro_SUFFIX_resource_LTL.run_experiments(19, "WEAK", "CFR")
# _11_cycl_pro_SUFFIX_resource_LTL.run_experiments(20, "STRONG", "CFR")

# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(12, "STRONG", "CFR")
# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(13, "WEAK", "CFR")
# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(14, "STRONG", "CFR")
# run again
# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(15, "WEAK", "CFR")
# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(16, "STRONG", "CFR")
# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(17, "WEAK", "CFR")
# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(18, "STRONG", "CFR")
# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(19, "WEAK", "CFR")
# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(20, "STRONG", "CFR")

# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(10, "STRONG", "CFR")
# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(11, "WEAK", "CFR")

_6_evaluate_baseline_SUFFIX_and_group.run_experiments(21, "STRONG", "CFR")
_11_cycl_pro_SUFFIX_resource_LTL.run_experiments(21, "STRONG", "CFR")
# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(21, "STRONG", "CFR")

# from train1 import train1
# from train2 import train2
# from train3 import train3
# from train4 import train4
# from train5 import train5
# from train6 import train6
# from train7 import train7
# from train8 import train8
# from train_with_data1 import train_with_data1
# from train_with_data2 import train_with_data2
# from train_with_data3 import train_with_data3
# from train_with_data4 import train_with_data4
# from train_with_data5 import train_with_data5
# from train_with_data6 import train_with_data6
# from train_with_data7 import train_with_data7
# from train_with_data8 import train_with_data8

# train1()
# train2()
# train3()
# train4()
# train5()
# train6()
# train7()
# train8()
# train_with_data1()
# train_with_data2()
# train_with_data3()
# train_with_data4()
# train_with_data5()
# train_with_data6()
# train_with_data7()
# train_with_data8()
