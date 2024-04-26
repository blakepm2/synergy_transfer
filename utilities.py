import json
import pandas as pd
from alive_progress import alive_bar

# +
class Mapping():
    
    def __init__(self, items):        
        self.item2idx={}
        self.idx2item=[]
        
        for idx, item in enumerate(items):
            self.item2idx[item]=idx
            self.idx2item.append(item)
            
    def add(self,item):
        if item not in self.idx2item:
            self.idx2item.append(item)
            self.item2idx[item]=len(self.idx2item)-1


def json_to_csv(json_fp):

    # load the json file
    with open(json_fp, 'r') as infile:
        data = json.load(infile)
        infile.close()

    structured_data = {}
    with alive_bar(len(data)) as bar:
        for i, d in enumerate(data):
            for k in d.keys():
                if k not in structured_data:
                    structured_data[k] = [d[k]]
                else:
                    structured_data[k].append(d[k])
            bar.text(f'Processing Study ({i+1}/{len(data)})')
            bar()
    
    return pd.DataFrame(structured_data)



