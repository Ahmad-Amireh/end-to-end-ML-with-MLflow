import joblib 
import numpy as np 
import pandas as pd 
from pathlib import Path 
from typing import List

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts\mdoel_training\model.joblib'))

    def predict(self, data): 
        prediction = self.model.predict([data]).tolist()

        return prediction
