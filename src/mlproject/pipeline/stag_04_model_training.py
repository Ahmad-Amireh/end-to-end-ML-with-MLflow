from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_training import ModelTrainer
from mlproject import logger

STAGE_NAME= "Model Training stage"

class ModelTrainingPipeLine:
    def __init__(self):
        pass
    
    def main(self): 
        config = ConfigurationManager()
        model_trainer_config = config.get_model_training_config()
        model_trainer = ModelTrainer (config=model_trainer_config)
        model_trainer.train()


if __name__ =="__main__": 
    try:
        logger.info(f">> stage {STAGE_NAME} started <<")
        obj = ModelTrainingPipeLine()
        obj.main()
        logger.info(f">> stage {STAGE_NAME} ended <<\n\n ========")
    
    except Exception as e :
        logger.exception(e)
        raise e 