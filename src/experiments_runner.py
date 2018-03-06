"""
This file was created to manage running of experiments.

## settings are in the shared variables file
Author; Anton Yeshchenko
"""


# This will run whole set of experiments
from inference_algorithms import _6_evaluate_beseline_SUFFIX_only
from inference_algorithms import _6_evaluate_beseline_SUFFIX_only_group
from inference_algorithms import _9_cycl_SUFFIX_only
from inference_algorithms import _10_cycl_back_SUFFIX_only
from inference_algorithms import _11_cycl_pro_SUFFIX_only
from inference_algorithms import _11_cycl_pro_SUFFIX_only_group
from shared_variables import activateSettings, eventlog
# from train import train
from train_group import train
from formula_verificator import verify_with_data
from support_scripts.generate_declare_model import generateDeclareModel

formula1 = "WEAK"
formula2 = "STRONG"
formula_used = formula1
logNumber = 8

# train()
# _6_evaluate_beseline_SUFFIX_only.runExperiments()
# _9_cycl_SUFFIX_only.py.runExperiments()
# _10_cycl_back_SUFFIX_only.runExperiments()
# _6_evaluate_beseline_SUFFIX_only_group.runExperiments(logNumber, formula_used)
# _6_evaluate_beseline_SUFFIX_only.runExperiments(logNumber, formula_used)
# _9_cycl_SUFFIX_only.runExperiments(logNumber,formula_used)
# _10_cycl_back_SUFFIX_only.runExperiments(logNumber,formula_used)
# _11_cycl_pro_SUFFIX_only.runExperiments(logNumber,formula_used)
_11_cycl_pro_SUFFIX_only_group.runExperiments(logNumber, formula_used)

# generateDeclareModel(eventlog)
# verify_with_data()
