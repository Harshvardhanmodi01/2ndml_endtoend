## the work on dataset will happen here

#we create the path in which we put the data insertion components

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')     # these 3 are the inputs that we giving to my dataingestion component
                                            # and data inge knows where to insert the data 

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()  #ingestion_config will consist of the 3 value which we define above
         
    def initiate_data_ingestion(self):
        logging.info("enter the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\StudentsPerformance.csv')
            logging.info('read the dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) 
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('train test split initiated')
            train_set, test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('ingestion of the data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()