import requests
import json
import pandas as pd

from .set_config import read_config

config = read_config()

BASE_URL = 'https://api.drugcomb.org'

SAVE_DIR = config['SAVE_DIR']

def hello():
    print("hello")


def send_request(endpoint):
    response = requests.get(f'{BASE_URL}/{endpoint}')
    
    if response.status_code == 200:
        data = response.json()
        with open(f'{SAVE_DIR}/{endpoint}.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
            outfile.close()
        print(f"Data at {BASE_URL}/{endpoint} has been successfully saved to {endpoint}.json")
    
    else:
        print('Failed to fetch data:', response.status_code)
        

def convert_data(dataset):
    
    with open(f'{SAVE_DIR}/{dataset}.json', 'r') as infile:
        data = json.load(infile)
        infile.close()
        
    structured_data = {}
    for d in data:
        for k in d:
            if k not in structured_data.keys():
                structured_data[k] = [d[k]]
            else:
                structured_data[k].append(d[k])
    
    df = pd.DataFrame(structured_data)
    
    df.to_csv(f'{SAVE_DIR}/{dataset}.csv', index=False)
    
def load_dataset(dataset):
    
    data = pd.read_csv(f'{SAVE_DIR}/{dataset}.csv')
    
    return data

df = load_dataset('studies')

print(df.head())
        