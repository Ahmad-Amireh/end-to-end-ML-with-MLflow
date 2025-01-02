import pandas as pd
from sklearn.model_selection import train_test_split 
from mlproject import logger 
import os 
from mlproject.entity.config_entity import DataTransformationConfig



class DataTransformation : #train_test + encoding + PCA and all (#ALL EDA in ML cycle)
    def __init__(self, config:DataTransformationConfig):
        self.config = config  

    def renaming_columns(self): 
        data= pd.read_csv(self.config.data_path)
        data.rename(columns=lambda col: col.strip().replace(" ", "_").lower(), inplace=True)
        return data

    def train_test_splitting(self, data):
        train, test = train_test_split(data,test_size=0.25)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index= False) 

        logger.info("Splited data into training and testing sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
