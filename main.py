from wineproject import logger
from wineproject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from wineproject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from wineproject.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from wineproject.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
from wineproject.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<")
   obj = ModelTrainerTrainingPipeline()
   obj.main()
   logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
