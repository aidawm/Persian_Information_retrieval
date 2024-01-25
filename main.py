from index_tokens import Indexer
import json
import time

class IR: 
    def index_tokens(self):
        self.indexer = Indexer(True)
        self.indexer.tokenize_docs()
        self.IR_dictionary = self.indexer.get_indexes()
        print(self.IR_dictionary["ساعت"])

    def save_dictionary(self):
        json_dic = json.dumps(self.IR_dictionary)

        # open file for writing, "w" 
        f = open("dict.json","w")

        # write json object to file
        f.write(json_dic)


if __name__ == '__main__': 
    start_time = time.time()
    ir = IR()
    ir.index_tokens()
    ir.save_dictionary()
    end_time = time.time()
    
    print(f"process time : {end_time - start_time}")