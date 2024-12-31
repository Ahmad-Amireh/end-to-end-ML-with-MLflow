import dagshub
from mlproject.entity.config_entity import ModelEvaluationConfig
import os 
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn 
import numpy
import joblib 
import numpy as np
from mlproject.utils.common import save_json
from pathlib import Path

class ModelEvaluation: 
    def __init__(self, config: ModelEvaluationConfig): 
        self.config = config
        
    def eval_metrics(self, actual, pred): 
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae= mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2 
    
    def log_into_mlflow(self): 
        #print(self.config)
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        x_test = test_data.drop([self.config.target_column], axis=1) 
        y_test = test_data[self.config.target_column]

       #mlflow.set_tracking_uri(self.config.mlflow_uri)
        #tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        #print(tracking_url_type_store)
        dagshub.init(repo_owner=self.config.repo_owner, repo_name=self.config.repo_name, mlflow=True)
        with mlflow.start_run():
            y_predicted = model.predict(x_test)
            (rmse, mae, r2) = self.eval_metrics(y_test, y_predicted)
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"rmse":rmse, "mae":mae, "r2":r2})
            mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")