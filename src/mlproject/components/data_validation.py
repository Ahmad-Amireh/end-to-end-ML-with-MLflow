import os
from mlproject import logger 
import pandas as pd
from mlproject.entity.config_entity import DataValidationConfig

class DataValidation: 
    def __init__(self, config:DataValidationConfig):
        self.config = config 

    def validate_all_column(self) -> bool: 
        try: 
            validation_status = None 
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()
            data_types = data.dtypes
            all_schema_data_type = list(self.config.all_schema.values())
            for i,col in enumerate(all_cols): 
                if col not in all_schema or data_types[col] != all_schema_data_type[i]:
                    print(data_types[col])
                    print(all_schema_data_type)
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                else: 
                    validation_status = True 
                    with open (self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status 
            
        except Exception as e: 
            raise e 