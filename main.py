from datetime import datetime
from modules.extract_function import extract_to_json
import logging
import os
from modules.load_function import load_to_s3
from dotenv import load_dotenv


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

load_dotenv()               # this beginning gives the python script access to these credientials in our .env file

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME =os.getenv('AWS_BUCKET_NAME')


extract_result = extract_to_json(url, data_dir, timestamp, max_attempts=4, delay=10)


if extract_result:
    load_to_s3(AWS_BUCKET_NAME, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, data_dir)
else:
    logger.info('Extract saved no data, nothing to attempt to upload so aborted.')

print(extract_result)