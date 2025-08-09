#used for get track of detail of running of project every single details ye bhi ek baar banta hai
#error log bhi krta ek book samjo joh sab likhe ga
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#time along with log content saved here
#Makes it into a filename ending with .log
# ex -"08_09_2025_11_45_12.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# os.getcwd() → Gets your current working directory (the folder where your script runs).
# "logs" → This is the folder name where you want to store your log files.
# LOG_FILE → The unique log filename we created in step 1.
# os.path.join(...) → Combines all these into a full path to the log file.
# Example:/Users/ayush/project_folder/logs/08_09_2025_11_45_12.log

os.makedirs(logs_path,exist_ok=True)

# logs_path currently includes the filename (not just the folder).
# This ensures only the folder "logs" is created.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    # logging.INFO means:

    # It will log INFO, WARNING, ERROR, and CRITICAL messages.


)
# exception arise hua and the it got transfer to logging and saved into log file
if __name__=="__main__":
    logging.info("logging started")#this code is present at line 40 so by formatting line 40 will be shown in logs file with log folder and log file name
    #info is the level name and message is printed inside the message block
    