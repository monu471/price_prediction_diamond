import os,sys 
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_file_path = os.path.join("artifacts","raw.csv") 
    test_file_path = os.path.join("artifacts","test.csv") 
    train_file_path = os.path.join("artifacts","train.csv")  

class DataIngestion:
    logging.info("Data ingestion started")
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:

            logging.info("loading the dataset") 
            df = pd.read_csv(os.path.join("notebook","price.csv")) 
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_file_path),exist_ok=True)
            logging.info("saving the dataset")
            df.to_csv(self.data_ingestion_config.raw_file_path,index= False)
            logging.info("spliting the dataset")
            train_data,test_data = train_test_split(df,random_state=42,test_size=0.2)
            logging.info("saving the train and the test dataset")
            train_data.to_csv(self.data_ingestion_config.train_file_path,index = False,header=False)
            test_data.to_csv(self.data_ingestion_config.test_file_path,index = False,header=False) 
            return(
                self.data_ingestion_config.train_file_path,
                self.data_ingestion_config.test_file_path
            )

        
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)
        
        
