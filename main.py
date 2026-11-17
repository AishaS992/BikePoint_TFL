from datetime import datetime
from modules.extract_function import extract_to_json
import logging
import os


timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

log_dir = 'logs' #should set up logging as early in the script as possible and you set up the dir/folder like the data one
os.makedirs(log_dir, exist_ok=True)
log_filename = f'{log_dir}/{timestamp}.log'

logging.basicConfig(
    filename=log_filename,
    format= '%(asctime)s - %(levelname)s - %(message)s', #level tells you severity of message whether warning or error etc.
    level = logging.INFO #how we want our logs to be configured 
)

logger = logging.getLogger() #get info you configured above and put into the logger
logger.info('Logger was successfuly initialised.') #tells us we want the message at the INFO level

url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'


extract_result = extract_to_json(url, data_dir, timestamp, max_attempts=4, delay=10)
print(extract_result)

