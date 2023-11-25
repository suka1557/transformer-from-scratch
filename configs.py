import os, sys
PROJECT_ROOT = os.path.abspath('.')
print(PROJECT_ROOT)

DATA_FOLDER = '/Users/sukant.kumar/personal/codes/datasets/'
TRAIN_DATA_FILENAME = 'Hindi_English_Truncated_Corpus.csv.zip'

MAX_SEQUENCE_LENGTH = 150

#SPECIAL TOKENS
START_TOKEN = '<START>'
END_TOKEN = '<END>'
PADDING_TOKEN = '<PADDING>'
UNKNOWN_TOKEN = '<UNK>'