root_folder = "/home/"
old_data_directory = root_folder+"data/raw/"
new_data_directory = root_folder+"data/new/"
intermediate_path = root_folder+"data/interim/"
db_path = root_folder+"database/"
db_file_name = "feature_store_v01.db"
model_dump_path = "/home/models/"
date_columns = ['registration_init_time','transaction_date_min','transaction_date_max','membership_expire_date_max','last_login']
ml_flow_path = "runs:/2b26c1f389b3485bb44b17cf85681cb6/models"
run_on = "old" #"old"
start_date = '2017-03-01'
end_date = '2017-03-31'
metric='std'
drfit_db_name = "drift_db_name_2.db"
mlflow_tracking_uri = "http://0.0.0.0:6006"
mlflow_experiment_name = "Model_Building_Pipeline_Drift"
short_exp_name_identifier = "without_dateprep"