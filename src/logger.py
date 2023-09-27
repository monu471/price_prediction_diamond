import logging,os,sys 
from datetime import datetime
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 
log_dir = os.path.join(os.getcwd(),"logs",log_file) 
os.makedirs(log_dir,exist_ok=True) 

log_File_path = os.path.join(log_dir,log_file) 

logging.basicConfig(level=logging.INFO,
                     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                    filename=log_File_path
)
