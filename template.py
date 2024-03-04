
import os,sys
from pathlib import  Path
import logging

while True:
    project_name=input("Enter project name: ")
    if project_name!="":
        break

    #suppose project name is:ml_p
    #ml_p/components/__init__.py

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "requirements.txt",
    "setup.py"
    ]

for f_path in list_of_files:
    filepath=Path(f_path)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        logging.info(f"Files and folders are already present at :{filepath}")