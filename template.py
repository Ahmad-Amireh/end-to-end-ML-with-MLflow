import os 
from pathlib import Path
import logging 


log_path= os.path.join(Path(os.getcwd()), "log.log")
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name= "mlproject"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", 
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py", 
    "app.py",
    "Dockerfile", 
    "requirments.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
    ]


for filepath in list_of_files: 
    filepath = Path(filepath) # convering path into windows path 
    filedir, filename= os.path.split(filepath) # seperating folder and files 

    if filedir != "": # the path have directory (not empty) as some path only contains a file 
        os.makedirs(filedir, exist_ok=True) # make a dir structure 
        logging.info(f"crating directory; {filedir} for the file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0): # if the path is not exist or filepath size =0 
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")