from mlproject import logger 
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlproject.pipeline.stage_03_data_transformation import DataTransformationPipeLine
from mlproject.pipeline.stag_04_model_training import ModelTrainingPipeLine
from mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion stage"

try : 
    logger.info(f">> stage {STAGE_NAME} started <<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed << \n\n ==========")
except Exception as e : 
        logger.exception(e)
        raise e 

STAGE_NAME = "Data Validation stage"

try: 
    logger.info(f">> stage {STAGE_NAME} started")
    obj = DataValidationTrainingPipeline() 
    obj.main()
    logger.info(f">> stage {STAGE_NAME} ended\n\n ========")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">> stage {STAGE_NAME} started <<")
    obj = DataTransformationPipeLine()
    obj.main()
    logger.info(f">> stage {STAGE_NAME} ended <<\n\n ========")

except Exception as e :
    logger.exception(e)
    raise e 



STAGE_NAME = "Training Model stage"

try:
    logger.info(f">> stage {STAGE_NAME} started <<")
    obj = ModelTrainingPipeLine()
    obj.main()
    logger.info(f">> stage {STAGE_NAME} ended <<\n\n ========")

except Exception as e :
    logger.exception(e)
    raise e 



STAGE_NAME = "Evaluation Model stage"
try:
    logger.info(f">> stage {STAGE_NAME} started <<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">> stage {STAGE_NAME} ended <<\n\n ========")

except Exception as e :
    logger.exception(e)
    raise e 
