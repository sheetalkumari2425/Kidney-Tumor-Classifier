from src.KidneyTumorClassifier import logger
from KidneyTumorClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from KidneyTumorClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from KidneyTumorClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from KidneyTumorClassifier.pipeline.stage_04_model_evaluation_with_mlflow import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"------ Stage {STAGE_NAME} started ------")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"------ Stage {STAGE_NAME} completed successfully ------")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f"--------- stage {STAGE_NAME} started ---------")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f"--------- stage {STAGE_NAME} completed -----------\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f"--------- stage {STAGE_NAME} started ---------")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f"--------- stage {STAGE_NAME} completed -----------\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Evaluation"
try: 
   logger.info(f"*******************")
   logger.info(f"--------- stage {STAGE_NAME} started ---------")
   model_trainer = EvaluationPipeline()
   model_trainer.main()
   logger.info(f"--------- stage {STAGE_NAME} completed -----------\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     