from index_tokens import Indexer
import json
import time
import math

class IR: 
    def __init__(self) -> None:
        self.N = 12202 

    def index_tokens(self):
        self.indexer = Indexer(True)
        self.indexer.tokenize_docs()
        self.IR_dictionary = self.indexer.get_indexes()
        print(self.IR_dictionary["ساعت"])

    def save_dictionary(self):
        
        json_dic = json.dumps(self.IR_dictionary)
        f = open("dict.json","w")
        f.write(json_dic)

    def load_dictionary(self): 
        data_address = "dict.json"
        f = open(data_address)
        self.IR_dictionary = json.load(f)

    def calculate_tf_idf(self):
        for t in self.IR_dictionary.keys():
            n_t = self.IR_dictionary[t]["doc_frequency"]
            for d in self.IR_dictionary[t]["docs"].keys():
                f_td = self.IR_dictionary[t]["docs"][d]["term_frequency"]
                self.IR_dictionary[t]["docs"][d]["tf-idf"] = (1+math.log(f_td,10))*math.log(self.N/n_t)


if __name__ == '__main__': 
    # start_time = time.time()
    ir = IR()
    ir.load_dictionary()
    # ir.index_tokens()
    # ir.calculate_tf_idf()
    # ir.save_dictionary()
    # end_time = time.time()

    # print(f"process time : {end_time - start_time}")