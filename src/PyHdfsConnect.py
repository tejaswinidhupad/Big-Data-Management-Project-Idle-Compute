import requests
import pandas as pd
from hdfs import InsecureClient
import datetime

#Today date ---------
today = str(datetime.datetime.today()).split()[0]

#Temporal landing - using API
'''
api_url = "https://Idlecompute.com/renter_submit/1" 
response = requests.get(api_url)
daily_renter = response.json()

api_url = "https://Idlecompute.com/tanant_submit/1" 
response = requests.get(api_url)
daily_tanant = response.json()

#change json to dataframe and append to the previous one

'''

#Temporal landing - using local file, implemented this for now as we don't have the functional URL to retrive the data from (i.e.user forms)
daily_renter = pd.read_json('./dataset/renter_'+today+'.json') #replace this when we have front-end 
daily_tanant = pd.read_json('./dataset/tanant_'+today+'.json') #replace this when we have front-end 

#File conversion from JSON to parquet
daily_renter.to_parquet('./dataset/renter_'+today+'.parquet', compression=None) 
daily_tanant.to_parquet('./dataset/tanant_'+today+'.parquet', compression=None) 

#Persistent landing 
client = InsecureClient('http://10.4.41.85:9870', user='bdm') 
client.upload('dataset','./dataset/renter_'+today+'.parquet')
client.upload('dataset','./dataset/tanant_'+today+'.parquet')

print(today+' files have been added to HDFS.')