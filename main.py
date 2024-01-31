from index_tokens import Indexer
import json
import time
import math


class IR: 
    def __init__(self,en_champion_list) -> None:
        self.enable_champion_list = en_champion_list
        data_address = "IR_data_news_12k.json"
        f = open(data_address)
        self.json_file = json.load(f)

    def index_tokens(self):
        self.indexer = Indexer(True)
        self.indexer.tokenize_docs()
        self.IR_dictionary = self.indexer.get_indexes()
        if self.enable_champion_list :
            self.indexer.generate_champion_list(10)
            self.champion_list= self.indexer.get_champion_list()
        
        # print(self.IR_dictionary["ساعت"])

    def save_dictionary(self):
        
        json_dic = json.dumps(self.IR_dictionary)
        f = open("dict.json","w")
        f.write(json_dic)
        ch_json = json.dumps(self.champion_list)
        f = open("champions.json","w")
        f.write(ch_json)

    def load_dictionary(self): 
        print ("setup search engine!")
        self.indexer = Indexer(False)
        data_address = "dict.json"
        f = open(data_address)
        self.IR_dictionary = json.load(f)
        if self.enable_champion_list:
            champion_address = "champions.json"
            f = open(champion_address)
            self.champion_list = json.load(f)
        

    def find_suitable_docs(self,tokens):
        docs_dict = dict()
        if self.enable_champion_list:
            for t in tokens:
                    for d in self.champion_list[t]:
                        if not d in docs_dict.keys():
                            docs_dict[d] = dict()
                        docs_dict[d][t] = float(self.champion_list[t][d])
        else:
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
        

        
        with open(f'{query}.txt', 'w') as f:
            for d in best_docs.keys():      
                title = self.json_file[d]["title"]  
                link = self.json_file [d]["url"]
                f.write(f"score: {best_docs[d]} - doc : {title}\t{link}")
                f.write("--------------------------------------------------\n")

        
    def get_queries(self):
        while True:
            print("enter your query : \t")
            query = input()
            if (query == "exit"):
                break
            self.answer_query(query)
        


if __name__ == '__main__': 
    # start_time = time.time()
    
    ir = IR(True)
    ir.index_tokens()
    # ir.load_dictionary()
    # ir.save_dictionary()

    ir.get_queries()
    

    # ir.answer_to_queries()
    # ir.index_tokens()
    # ir.calculate_tf_idf()
    # ir.save_dictionary()
    # end_time = time.time()
