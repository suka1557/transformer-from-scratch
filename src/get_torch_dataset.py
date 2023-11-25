from torch.utils.data import Dataset

class TextDataset(Dataset):

    def __init__(self, language1_sentences: list, language2_sentences: list):
        self.language1_sentences = language1_sentences
        self.language2_sentences = language2_sentences

    def __len__(self):
        return len(self.language1_sentences)

    def __getitem__(self, idx):
        return self.language1_sentences[idx], self.language2_sentences[idx]