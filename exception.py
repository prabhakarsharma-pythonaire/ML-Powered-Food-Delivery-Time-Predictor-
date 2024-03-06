import sys
from flask import Flask
from src.logger import logging
from src.exception import CustomException
app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    try:
        raise Exception("We are testing our Exception file") #Error
    except Exception as e:
        ML=CustomException(e,sys)
        logging.info(ML.error_message)
        logging.info("We are testing logging file")

        return "Welcome to me prabhakar sharma"

if __name__ =="__main__":
    app.run(debug=True) #default prot number 5000





