from index_tokens import Indexer
import json
import time
import math


class IR: 

    def index_tokens(self):
        self.indexer = Indexer(True)
        self.indexer.tokenize_docs()
        self.IR_dictionary = self.indexer.get_indexes()
        # print(self.IR_dictionary["ساعت"])

    def save_dictionary(self):
        
        json_dic = json.dumps(self.IR_dictionary)
        f = open("dict.json","w")
        f.write(json_dic)

    def load_dictionary(self): 
        self.indexer = Indexer(False)
        data_address = "dict.json"
        f = open(data_address)
        self.IR_dictionary = json.load(f)
        
    
    

    def find_suitable_docs(self,tokens):
        docs_dict = dict()
        for t in tokens:
            for d in self.IR_dictionary[t]["docs"].keys():
                if not d in docs_dict.keys():
                    docs_dict[d] = dict()
                docs_dict[d][t] = float(self.IR_dictionary[t]["docs"][d]["tf-idf"])

        return docs_dict 



    def answer_query(self,query):
        dict_query = dict()
        tokens =self.indexer.tokenize_text(query)
        

        for t in tokens :
            if not t in dict_query.keys():
                dict_query[t]=0
            dict_query[t]+=1

        tf_idf_query = {t:1+math.log(dict_query[t],10) for t in dict_query.keys()}
        print(tokens)
        docs = self.find_suitable_docs(set(tokens))
        docs_score = dict()
        for d in docs :
            for t in docs[d].keys():
                if not d in docs_score.keys():
                    docs_score[d] = 0
                docs_score[d] += docs[d][t] * tf_idf_query[t]
        
        sorted_docs = sorted(docs_score.items(), key=lambda x:x[1], reverse=True)[:10]
        best_docs = dict(sorted_docs)
        data_address = "IR_data_news_12k.json"
        f = open(data_address)
        json_file = json.load(f)

        
        with open(f'test.txt', 'w') as f:
            for d in best_docs.keys():      
                text = json_file[d]["content"]  
                f.write(f"{text}\n")
                f.write("--------------------------------------------------\n")

        

        


if __name__ == '__main__': 
    # start_time = time.time()
    
    ir = IR()
    ir.index_tokens()
    # ir.load_dictionary()
    ir.save_dictionary()

    ir.answer_query("قهرمانی تیم ملی ایران")


    # ir.answer_to_queries()
    # ir.index_tokens()
    # ir.calculate_tf_idf()
    # ir.save_dictionary()
    # end_time = time.time()
