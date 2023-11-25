import os, sys
import numpy as np, pandas as pd

from configs import DATA_FOLDER, TRAIN_DATA_FILENAME
data_file = os.path.join(DATA_FOLDER, TRAIN_DATA_FILENAME)

from src.get_char_dicts import get_char_idx_mappings
from src.get_torch_dataset import TextDataset

data = pd.read_csv(data_file)
print(data.shape)

#remove any missing data
data = data[ data['english_sentence'].notnull() ].reset_index(drop=True)
data = data[ data['hindi_sentence'].notnull() ].reset_index(drop=True)
print(data.shape)

#get language dictionaries
eng_char_to_idx, eng_idx_to_char = get_char_idx_mappings( data['english_sentence'].to_list() )
hin_char_to_idx, hin_idx_to_char = get_char_idx_mappings( data['hindi_sentence'].to_list() )

#Add sentence lengths 
data['eng_length'] = data['english_sentence'].apply(lambda x: len(x))
data['hin_length'] = data['hindi_sentence'].apply(lambda x: len(x))

#Creating a torch dataset by pairing english and hindi sentences
dataset = TextDataset(language1_sentences=data['english_sentence'].to_list(), language2_sentences=data['hindi_sentence'].to_list())

print(dataset[1])
print(len(dataset))