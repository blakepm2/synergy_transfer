import yaml

CONFIG_PATH = './config.yaml'

def read_config():
    with open(CONFIG_PATH, 'r') as infile:
        data = yaml.safe_load(infile)
        infile.close()
        
    return data