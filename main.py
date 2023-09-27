import os,sys 
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import * 

data_ingestion_config = DataIngestionConfig() 
data_ingestion = DataIngestion()
data_ingestion.initiate_data_ingestion()



