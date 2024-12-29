import os 
import sys 
import logging 

foramtter = "[%(asctime)s - %(module)s - %(levelname)s - %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"runnung_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO, 
    format = foramtter, 
    handlers = [
        logging.FileHandler(log_filepath), 
        logging.StreamHandler(sys.stdout) # print log in terminals 
    ]
)

logger = logging.getLogger("mlprojectLogger")