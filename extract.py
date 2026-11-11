import os
import time
import json
import logging
from datetime import datetime #called 'from datetime import datetime' instead of just 'import datetime' to avoiding having to say datetime.datetime 
import requests
# this imports all the tools we need in the script

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

log_dir = 'logs' #should set up logging as early int he script as possible and you set up the dir/folder like the data one
os.makedirs(log_dir, exist_ok=True)
log_filename = f'{log_dir}/{timestamp}.log'

logging.basicConfig(
    filename=log_filename,
    format= '%(asctime)s - %(levelname)s - %(message)s', #level tells you severity of message whether warning or error etc.
    level = logging.INFO #how we want our logs to be configured 
)

logger = logging.getLogger() #get info you configured above and put into the logger
logger.info('Logger was successfuly initialised.') #tells us we want the message at the INFO level

# this prints the time and date now and formats it as a string using strftime
data_dir = 'data' #this is a place where we are going to put our data so we want to just put somethign there for now
os.makedirs(data_dir, exist_ok=True)  #this is using the make directory function from os in our folder and basically says once you see it, be happy?

filename = f'{data_dir}/{timestamp}.json' #this now gives us the data whatever it is with the time stamp in json format
#gives us the timestap as an f string in the json format

url = 'https://api.tfl.gov.uk/BikePoint/' #the url for the api 

attempt = 1
max_attempts =3

# had to tab everything below bc once we started the while loop, it takes underneath as that so this is separate?
while attempt <= max_attempts:
    response = requests.get(url) #this is us getting the response using the get fucntion from requests package to get the data from the url which is the bike point
    status_code = response.status_code

    if 200<=status_code<300:
        try:
            data = response.json() #turns the response from the API into json and save into data variable

            with open(filename, 'w') as file: #this opens up that file and begins writing and calls it 'file' and basically...
                json.dump(data, file)           # ... uses json to 'dump' the data into the 'file' that we have opened
            print(f'File {filename} saved successfully ☺️')
            logger.info(f'File {filename} saved successfully ☺️')
        except Exception as e:
            print(f'An error occured when saving the Json: {e} 😶')
            logger.info(f'An error occured when saving the Json: {e} 😶')
        
        break

    elif 300<=status_code<500:
        print(f'API call failed, status code {status_code} 😥')
        logger.info(f'API call failed, status code {status_code} 😥')
        break

    else:
        if attempt>max_attempts:
            print(f'Max number of attempts reached. Status code {status_code}. Investigate further. 😶‍🌫️')
            logger.info(f'Max number of attempts reached. Status code {status_code}. Investigate further. 😶‍🌫️')
        else:

            print(f'Attempt {attempt} failed, status code {status_code}, try again 🫡')
            logger.info(f'Attempt {attempt} failed, status code {status_code}, try again 🫡')
        attempt+=1
        time.sleep(30) #this allows a wait time of 30 seconds before another attempt
    

#we want to gitignore the json file with the data bc it's never gonna change 