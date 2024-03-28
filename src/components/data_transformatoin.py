from src.constants import *
from src.logger import logging
from src.exception import CustomException
from src.config.configuration import *
from dataclasses import dataclass
import os,sys
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import simpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder,OneHotEncoder


#we will define two function here
#1. Feature engineering
#2. Data Transofrmation

class Feature_Engineering(BaseEstimator,TransformerMixin):
    def __init__(self):
        logging.info("************************************** feature engineering started***********************")

    def distance_calc( self , df , lat1 , lon1 , lat2 , lon2 ):
        p = np.pi/180
        a = 0.5 - np.cos((df[lat2] - df[lat1]) * p) / 2 + np.cos(df[lat1] * p) * np.cos(df[lat2] * p) * (
                    1 - np.cos((df[lon2] - df[lon1]) * p)) / 2
        df['distance'] = 12734 * np.arccos(np.sort(a))

    def transform_data(self, df):
        try:
            df.drop(['ID'], axis=1, inplace=True)

            self.distance_calc(df, 'Restaurant_latitude',
                                'Restaurant_longitude',
                                'Delivery_location_latitude',
                                'Delivery_location_longitude')

            df.drop(['Delivery_person_ID', 'Restaurant_latitude', 'Restaurant_longitude',
                     'Delivery_location_latitude',
                     'Delivery_location_longitude',
                     'Order_Date', 'Time_Orderd', 'Time_Order_picked'], axis=1, inplace=True)

            logging.info("droping columns from our original dataset")

            return df

        except Exception as e:
            raise CustomException(e, sys)

    def fit(self, X, Y=None):
        return self

    def transform(self, X: pd.DataFrame, Y=None):
        try:
            transformed_df = self.transform_data(X)

            return transformed_df
        except Exception as e:
            raise CustomException(e, sys) from e

@dataclass
class DataTransformationConfig():
    processed_obj_file_path:PREPROCESSING_OBJ_FILE
    transfor_train_path: TRANSFORMATION_TRAIN_FILE_PATH
    transform_test_path: TRANSFORMATION_TEST_FILE_PATH
    feature_engg_obj_path: FEATURE_ENGINEERING_OBJ_FILE_PATH


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_obj(selfself):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)