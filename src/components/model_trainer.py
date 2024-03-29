from src.constants import *
from src.logger import logging
from src.exception import CustomException
import os, sys
from src.config.configuration import *
from dataclasses import dataclass
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils import evaluate_model,save_obj
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = MODEL_FILE_PATH

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initate_model_training(self, train_array, test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')

            X_train ,Y_train,X_test,Y_test = (train_array[:,:-1],train_array[:,-1],
                                              test_array[:,:-1],test_array[:,-1])

            models= {
                "XGBRegressor": XGBRegressor(),
                "SVR" : SVR(),
                "RandomForestRegressor":RandomForestRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "DecisionTreeRegressor" :DecisionTreeRegressor()

                }

            model_report : dict =evaluate_model(X_train ,Y_train,X_test,Y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')


            best_model_score=max(sorted(model_report.values()))

            # best_model_name = list(model_report.keys())[
            #     list(model_report.values().index(best_model_score))
            #
            # ]
            best_model_name = max(model_report, key=model_report.get)

            best_model = models[best_model_name]

            print(f"Best model :{best_model_name},R2 socre:{best_model_score}")
            print('\n====================================================================================\n')
            logging.info(f"Best model :{best_model_name},R2 socre:{best_model_score}")

            save_obj(file_path=self.model_trainer_config.trained_model_file_path,
                     obj= best_model)


        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e,sys)