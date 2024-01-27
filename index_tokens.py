import json
from word_tokenizer import WordTokenizer
from word_normalizer import Normalizer
from parsivar import FindStems
from term_frequency import MostFrequences
import math


class Indexer:
    def __init__(self,save_most_frequent_words = False) -> None:
        self.save_most_frequent_words= save_most_frequent_words
        self.tokenizer = WordTokenizer()
        self.normalizer = Normalizer()
        self.stemmer = FindStems()
        self.freq_term = MostFrequences()
        if (not self.save_most_frequent_words) : 
            self.get_eliminate_words()
            
        else:
            self.doc_tocken_list = dict()

        self.IR_dictionary = dict()

    def get_eliminate_words(self):
        f = open("50_most_freq_terms.txt", 'r')
        self.eliminated_words = f.readlines()
        self.eliminated_words = [l.replace("\n","").split("\t")[0] for l in self.eliminated_words]

    def create_posting_list(self,tokens: list[str], docID):

        count = 0 
        for t in tokens : 

            if t in self.IR_dictionary.keys():
                if(not docID in self.IR_dictionary[t]["docs"].keys()):
                    self.IR_dictionary[t]["docs"][docID]= dict()
                    self.IR_dictionary[t]["docs"][docID]["positions"]= list()
                    self.IR_dictionary[t]["docs"][docID]["term_frequency"]= 0
            else:
                self.IR_dictionary[t] = dict()
                self.IR_dictionary[t]["docs"] = dict()
                self.IR_dictionary[t]["docs"][docID]= dict()
                self.IR_dictionary[t]["docs"][docID]["positions"]= list()
                self.IR_dictionary[t]["docs"][docID]["term_frequency"]= 0

            self.IR_dictionary[t]["docs"][docID]["positions"].append(count)
            self.IR_dictionary[t]["docs"][docID]["term_frequency"] += 1
            
            count +=1
        

    def tokenize_text(self, text , is_indexing= False):

        tokens = self.tokenizer.simple_tokenizer(text)
        tokens = self.normalizer.normalize_tokens(tokens)

                
        tokens = [self.stemmer.convert_to_stem(t) for t in tokens]

        if not is_indexing:
            tokens = [ t for t in tokens if not (t in self.eliminated_words or t == "")]
        
        return tokens

    def tokenize_docs(self):
            data_address = "IR_data_news_12k.json"
            f = open(data_address)
            json_file = json.load(f)
            self.doc_numbers = len(json_file)
            # self.doc_numbers = 10

            for i in range(self.doc_numbers):
                if i%1000 == 1: 
                    print (f"process doc {i}\n")
            
                text = json_file[str(i)]["content"]

                
                
                if (self.save_most_frequent_words):
                    tokens = self.tokenize_text(text,True)
                    self.freq_term.count_terms(tokens)
                    self.doc_tocken_list[str(i)]= tokens

                else: 
                    tokens = self.tokenize_text(text)
                    self.create_posting_list(tokens,i)
                    


            if(self.save_most_frequent_words):
                self.freq_term.find_most_freq_terms()
                self.get_eliminate_words()
                for i in range(self.doc_numbers):
                    tokens = [ t for t in self.doc_tocken_list[str(i)] if not (t in self.eliminated_words or t == "")]
                    self.create_posting_list(tokens,str(i))
                    del self.doc_tocken_list[str(i)]
            for t in self.IR_dictionary.keys():
                self.IR_dictionary[t]["doc_frequency"] = len(self.IR_dictionary[t]["docs"].keys())

            print("calculate tf-idfs\n")
            self.calculate_tf_idf()
            self.calculate_doc_vector_normalization()

            # normalize tf_idfs 

            for t in self.IR_dictionary.keys():
                for d in self.IR_dictionary[t]["docs"].keys():
                    self.IR_dictionary[t]["docs"][d]["tf-idf"] = self.IR_dictionary[t]["docs"][d]["tf-idf"] / self.normalization_vector_docs[d]




    def get_indexes(self):
        return self.IR_dictionary
    

    def calculate_tf_idf(self):
        for t in self.IR_dictionary.keys():
            n_t = self.IR_dictionary[t]["doc_frequency"]
            for d in self.IR_dictionary[t]["docs"].keys():
                f_td = self.IR_dictionary[t]["docs"][d]["term_frequency"]
                self.IR_dictionary[t]["docs"][d]["tf-idf"] = (1+math.log(f_td,10))*math.log(self.doc_numbers/n_t)


    def calculate_doc_vector_normalization (self):
        self.normalization_vector_docs = dict()

        for t in self.IR_dictionary.keys():
            for d in self.IR_dictionary[t]["docs"].keys():
                if (not d in self.normalization_vector_docs.keys()):
                    self.normalization_vector_docs[d] = 0
                term_frequency = self.IR_dictionary[t]["docs"][d]["term_frequency"]
                tf_idf = self.IR_dictionary[t]["docs"][d]["tf-idf"]
                self.normalization_vector_docs[d] +=  term_frequency * (tf_idf **2)

        self.normalization_vector_docs = {d:self.normalization_vector_docs[d]**0.5 for d in self.normalization_vector_docs.keys() }

    
        
