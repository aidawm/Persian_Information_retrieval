import json
from word_tokenizer import WordTokenizer

def read_file(url):
    f = open(url)
    data = json.load(f)
    return data

data_address = "IR_data_news_12k.json"

json_file = read_file(data_address)
tokenizer = WordTokenizer()


for i in range(10):

    text = json_file[str(i)]["content"]

    # with open(f'texts.txt', 'a') as f:
    #     f.write(f"{text}\n")
    #     f.write("-------------------------------------------------\n")

    text = tokenizer.delete_punctuations_symbols(text)
    tokens = tokenizer.simple_tokenizer(text)
    tokens = tokenizer.process_verbs(tokens)
    with open(f'token_text{i}.txt', 'w') as f:
        for line in tokens:
            f.write(f"{line}\n")

        