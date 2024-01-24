import json
from word_tokenizer import WordTokenizer
from word_normalizer import Normalizer
from parsivar import FindStems

def read_file(url):
    f = open(url)
    data = json.load(f)
    return data

term_dictionary = {}
def count_terms(tokens):
    for t in tokens:
        if t == "":
             continue
        if (t in term_dictionary.keys()):
            term_dictionary[t]+=1
        else:
            term_dictionary[t]=1
        

def find_most_freq_terms():
    the_most_freq_terms= sorted(term_dictionary.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(the_most_freq_terms)


    with open('sorted_term_freq.txt', 'w') as f:
            for line in converted_dict.keys():
                f.write(f"{line}\t {term_dictionary[line]}\n")

    
    terms = list(converted_dict.keys())
    print(type(terms))
    terms = terms[0:50]
    with open('50_most_freq_terms.txt', 'w') as f:
            for line in terms:
                f.write(f"{line}\t {term_dictionary[line]}\n")




data_address = "IR_data_news_12k.json"

json_file = read_file(data_address)
tokenizer = WordTokenizer()
normalizer = Normalizer()

for i in range(10):

    text = json_file[str(i)]["content"]

    # with open(f'texts.txt', 'a') as f:
    #     f.write(f"{text}\n")
    #     f.write("-------------------------------------------------\n")

    
    tokens = tokenizer.simple_tokenizer(text)
    tokens = normalizer.normalize_tokens(tokens)

    stem = FindStems()
    tokens = [stem.convert_to_stem(t) for t in tokens]
    count_terms(tokens)

    # with open(f'token_text{i}.txt', 'w') as f:
    #     for line in tokens:
    #         f.write(f"{line}\n")

find_most_freq_terms()

        