from pathlib import Path
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject.config.configuration import ConfigurationManager
from mlproject import logger

STAGE_NAME= "Model Evaluation stage" 

class ModelEvaluationPipeline: 
    def __init__(self):
        pass

    def main (Self): 
        try: 
            config = ConfigurationManager()
            data_transformation_config = config.get_configutaion_model_evaluation()
            data_transformation = ModelEvaluation(config = data_transformation_config)
            data_transformation.log_into_mlflow()

        except Exception as e :
            logger.exception(e)
            raise e 

if __name__ =="__main__": 
    try:
        logger.info(f">> stage {STAGE_NAME} started <<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">> stage {STAGE_NAME} ended <<\n\n ========")
    
    except Exception as e :
        logger.exception(e)
        raise e 
