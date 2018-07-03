# Incremental-Predictive-Monitoring-of-Business-Processes-with-A-priori-knowledge

### Code based on:

* [link](https://github.com/yesanton/Process-Sequence-Prediction-with-A-priori-knowledge)
* [link](https://github.com/verenich/ProcessSequencePrediction)

### Inference algorithms used in this project:

* _6_evaluate_baseline_SUFFIX_only -> This is Baseline 1 - no apriori knowledge is used and only the control-flow is predicted.
* _6_evaluate_baseline_SUFFIX_and_group -> This is the extended version of Baseline 1, where also the resource attribute is predicted.
* _11_cycl_pro_SUFFIX_only -> This is Baseline 2 - apriori knowledge is used on the control-flow and only the control-flow is predicted.
* _11_cycl_pro_SUFFIX_resource_LTL -> This is the extended version of Baseline 2, where apriori knowledge is used on the control-flow but also the resource attribute is predicted.
* _11_cycl_pro_SUFFIX_declare_smart_queue -> This is the proposed approach, where apriori knowledge is used on the control-flow and on the resource attribute. Both the control-flow and the resource are predicted.

### How to run the algorithms:

It is necessary to first start the Java server found in LTLCheckForTraces/StackEntryPoint.java. The server contains the code for checking the compliance with a single trace and the specified apriori knowledge. The proposed approach uses the DeclareAnalyzer plugin implemented for Prom. 

Every csv file should be converted into the suitable format(only numerical values) using the files src/support_scripts/csv_converter.py and src/support_scripts/csv_converter_group.py accordingly. The scripts also create dictionaries which map the numerical values to actual values.

Baseline 2 uses apriori knowledge in the form of LTL rules which are expressed in the src/shared_variables.py file. 

The proposed approach uses apriori knowledge in the form of MP-Declare model, wchich are held in a separate file. The creation of the models can be done by following the structure found in the models in src/declare_models/.

The specification of the variables is done in the file src/shared_variables.py.

The file src/experiments_runner.py is used to run the the inference algorithms, wchich output the results to the folder output_files/.

