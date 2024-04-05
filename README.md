
# end-to-end-project

1. Create new Enviroment
    conda create -p modular python=3.9 -y

2. Activate your enviroment
    conda activate modular/ ->cmd
    source activate env/ -git bash

3. Install requirements
 pip install -r requirements.txt


Description of Webapp-

This project builds a model to predict delivery time using distance ,Delivery person age,wheather condition ,vehicle condtion ,type of vechicle ,city (tier1,tier2,tier3),road traffic etc and othe factors . The goal is to estimate the delivery of food condsidering most of the factors that can affect the delivery process . The project includes:

Dataset - Dataset shared by zomato is used in this project 

Data Preprocessing:  Cleaning, feature engineering, and data transformation.
Feature Selection: Identifying and selecting relevant features for model building.
Model Training and Evaluation: Training and evaluating different regression models, such as Random Forest, Decision Tree, Gradient Boosting, Linear Regression, Ridge, and XGBRegressor.
Model Selection: Choosing the best-performing model based on evaluation metrics (r2, MAE, MSE, RMSE).
Deployment: Packaging the model and its dependencies for deployment.
Code Organization

The project code is organized as follows:

Articraft: Contains data ingestion, data transformation, and model training code.
Data: Contains the final preprocessed data.
Logs: Stores logs generated during the project.
Prediction: Contains code for batch prediction.
Batch_prediction: Stores the results of batch prediction.
Config: Contains configuration files (e.g., config.yaml).
Feature_eng: Includes code for feature engineering.
Src: Contains various components, configurations, constants, entities, exceptions, loggers, pipelines, and utilities.
App.py: The main script that orchestrates the project.
Exception.py: Handles exceptions and errors.
Logs.py: Manages logging functionality.
Schema.yaml: Defines the data schema.
Main.py: The entry point of the project.
Setup.py: Used for setting up the project environment.
Template.py: Provides a template for data ingestion and preprocessing.


Additional Features

In addition to the core project, the following features have been implemented:

Interactive Dashboard: A dashboard that visualizes the model predictions and other project insights.
Documentation: Detailed documentation explaining the project architecture, code structure, and deployment process.
Continuous Integration/Continuous Deployment (CI/CD): Automated pipelines for testing, building, and deploying the project.
Testing: Unit tests and integration tests to ensure code quality.
Version Control: Code is managed using Git for version control and collaboration.
