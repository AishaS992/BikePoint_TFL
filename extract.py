import os
import json
from datetime import datetime #called 'from datetime import datetime' instead of just 'import datetime' to avoiding having to say datetime.datetime 
import requests
# this imports all the tools we need in the script

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
# this prints the time and date now and formats it as a string using strftime
data_dir = 'data' #this is a place where we are going to put our data so we want to just put somethign there for now
os.makedirs(data_dir, exist_ok=True)  #this is using the make directory function from os in our folder and basically says once you see it, be happy?

filename = f'{data_dir}/{timestamp}.json' #this now gives us the data whatever it is with the time stamp in json format
#gives us the timestap as an f string in the json format

url = 'https://api.tfl.gov.uk/BikePoint/' #the url for the api 

response = requests.get(url) #this is us getting the response using the get fucntion from requests package to get the data from the url which is the bike point

data = response.json() #turns the response from the API into json and save into data variable

with open(filename, 'w') as file: #this opens up that file and begins writing and calls it 'file' and basically...
    json.dump(data, file)           # ... uses json to 'dump' the data into the 'file' that we have opened



#we want to gitignore the json file with the data bc it's never gonna change 