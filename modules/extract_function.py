import os
import requests
import json
import time
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def extract_to_json(url: str, data_dir: str, timestamp: str, max_attempts: int, delay: int):
    """Function to extract JSON files from a URL and save to a destination.

    Args:
        url (str): URL to pull data from
        data_dir (str): filepath to save data to
        timestamp (str): timestamp to amend file name
        max_attempts (int): number of times to retry calls
        delay (int): how long to wait between calls
    """    """"""

#to do the documentation you do def and name the function then give the arguments where you apply the specifics for your jon
#then colon and next line speech marks 3 times and then go CTRL+Shift+2 to get the template and fill in the information

    #make directory if not exist
    os.makedirs(data_dir, exist_ok= True)

    #build out the file name
    filename = f'{data_dir}/{timestamp}.json'

    attempt = 1
    #max_attempts =

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

                # Flag that data was saved successfully
                return True

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
            time.sleep(delay) #this allows a wait time of 30 seconds before another attempt

    # return statement
    return False
        