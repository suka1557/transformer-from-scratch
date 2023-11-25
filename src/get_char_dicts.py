from configs import START_TOKEN, END_TOKEN, PADDING_TOKEN, UNKNOWN_TOKEN

def get_char_idx_mappings(list_of_sentences: list) -> (dict, dict):
    char_to_idx = {}
    idx_to_char = {}

    for i,sentence in enumerate(list_of_sentences):
        try:
            for char in list(sentence):
                if char not in char_to_idx:
                    char_to_idx[char] = len(char_to_idx) + 1
        except Exception as e:
            print(f"Unparsable Value Found at index - {i} in sentence - {sentence} : Error - {e}")
            continue

    #Adding special tokens in the end
    char_to_idx[START_TOKEN]= len(char_to_idx) + 1
    char_to_idx[END_TOKEN] = len(char_to_idx) + 1
    char_to_idx[PADDING_TOKEN]= len(char_to_idx) + 1
    char_to_idx[UNKNOWN_TOKEN]= len(char_to_idx) + 1

    #Reversing char to idx
    idx_to_char = {v:k for k,v in char_to_idx.items()}

    return char_to_idx, idx_to_char
                
