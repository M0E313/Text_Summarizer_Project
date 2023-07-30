import os
import sys
import logging

# define log format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# create the directory "logs" and create the file "running_logs.log"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        # create the file running_logs.log
        logging.FileHandler(log_filepath), 
        # show log in terminal
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")