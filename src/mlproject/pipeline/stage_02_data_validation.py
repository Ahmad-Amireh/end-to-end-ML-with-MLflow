
from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_validation import DataValidation
from mlproject import logger

STAGE_NAME = "Data Validation Stage"
class DataValidationTrainingPipeline: 
    def __init__(self):
        pass 
    def main (self) :
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validate_all_column()

if __name__ == "__main__":
    try: 
        logger.info(f">> stage {STAGE_NAME} started")
        obj = DataValidation()
        obj.main()
        logger.info(f">> stage {STAGE_NAME} ended\n\n ========")
    except Exception as e:
        logger.exception(e)
        raise e