"""
This file was created to manage running of experiments.

## settings are in the shared variables file
"""


from inference_algorithms import _6_evaluate_baseline_SUFFIX_only
from inference_algorithms import _11_cycl_pro_SUFFIX_only

from inference_algorithms import _6_evaluate_baseline_SUFFIX_and_group
from inference_algorithms import _11_cycl_pro_SUFFIX_resource_LTL
from inference_algorithms import _11_cycl_pro_SUFFIX_declare_smart_queue

from shared_variables import eventlog, activate_settings
from train import train
from train_with_data import train_with_data

# formula_used = "WEAK"
# formula_used = "STRONG"
# logNumber = 11
train()
# train_with_data()

# CF stands for Control Flow
# CFR stands for Control Flow + Resource
# They indicate which RNN model should be used for the inference algorithm

# _6_evaluate_baseline_SUFFIX_only.run_experiments(12, "STRONG", "CF")
# _11_cycl_pro_SUFFIX_only.run_experiments(12, "STRONG", "CF")

# _6_evaluate_baseline_SUFFIX_and_group.run_experiments(12, "STRONG", "CFR")
# _11_cycl_pro_SUFFIX_resource_LTL.run_experiments(13, "WEAK", "CFR")
# _11_cycl_pro_SUFFIX_declare_smart_queue.run_experiments(12, "STRONG", "CFR")
