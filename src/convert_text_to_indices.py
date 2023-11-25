from configs import MAX_SEQUENCE_LENGTH, START_TOKEN, END_TOKEN, PADDING_TOKEN, UNKNOWN_TOKEN

def tokenize_sentence(sentence: str, char_to_idx: dict):

    sentence_length = len(sentence)

    sentence_sequence = []

    #ADD START token
    sentence_sequence.append( char_to_idx[START_TOKEN] )

    if sentence_length < MAX_SEQUENCE_LENGTH:
        #Need to append Padding
        #Convert till normal length
        for i in range(sentence_length):
            if sentence[i] in char_to_idx:
                sentence_sequence.append(  char_to_idx[sentence[i]])
            else:
                sentence_sequence.append( char_to_idx[UNKNOWN_TOKEN] )

        #Add padding
        for i in range(sentence_length, MAX_SEQUENCE_LENGTH):
            sentence_sequence.append(char_to_idx[PADDING_TOKEN])

    else:
        for i in range(0, MAX_SEQUENCE_LENGTH):
            if sentence[i] in char_to_idx:
                sentence_sequence.append(  char_to_idx[sentence[i]])
            else:
                sentence_sequence.append( char_to_idx[UNKNOWN_TOKEN] )

    #ADD END TOKEN IN LAST
    sentence_sequence.append(char_to_idx[END_TOKEN])


    return sentence_sequence