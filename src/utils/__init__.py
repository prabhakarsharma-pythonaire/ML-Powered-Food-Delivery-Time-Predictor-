from src.logger import logging
from src.exception import CustomException
import pickle
import os, sys
from sklearn.metrics import r2_score

def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj,file_obj )
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(X_train ,Y_train,X_test,Y_test,models):
    try:
        report= {}

        for i in range(len(models)):
            model = list(models.values())[i]

            model.fit(X_train,Y_train)

            Y_test_pred = model.predict(X_test)

            test_model_score = r2_score(Y_test,Y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report


    except Exception as e:
        raise CustomException(e, sys)

def load_model(file_path):
    try:
        with open(file_path,"rb") as f:
            return pickle.load(f)

    except Exception as e:
        logging.info("Exception occured while lpading model")
        raise CustomException(e,sys)