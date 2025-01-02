from pathlib import Path
from mlproject.components.data_transformation import DataTransformation
from mlproject.config.configuration import ConfigurationManager
from mlproject import logger

STAGE_NAME= "Data Transformation stage" 

class DataTransformationPipeLine: 
    def __init__(self):
        pass

    def main (Self): 
        try: 
            with open (Path("artifacts/data_validation/status.txt"),"r") as f: 
                status = f.read().split(" ")[-1]
            
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data= data_transformation.renaming_columns()
                data_transformation.train_test_splitting(data=data)
                    
            else:
                raise Exception("Your data schema is not valid")
        except Exception as e :
            logger.exception(e)
            raise e 

if __name__ =="__main__": 
    try:
        logger.info(f">> stage {STAGE_NAME} started <<")
        obj = DataTransformationPipeLine()
        obj.main()
        logger.info(f">> stage {STAGE_NAME} ended <<\n\n ========")
    
    except Exception as e :
        logger.exception(e)
        raise e 
