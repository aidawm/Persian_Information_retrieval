class WordTokenizer:
    def simple_tokenizer(self,text):    

        text = text.replace("\t", " ")
        text = text.replace("\n", " ")
        text = text.replace("\u200c", " ")
        text = text.replace(u'\xa0', " ")

        tokens = text.split(" ")

        return tokens
    
    def process_verbs(self,tokens: list[str]):
        del_index = []
        for i,t in enumerate(tokens):
            if t == "می" or t == "نمی": 
                mi = t+ "\u200c"
                tokens[i+1] = mi+ tokens[i+1]
                del_index.append(i)

        for i in range(len(del_index)-1,-1,-1):
            tokens.pop(del_index[i])
        
        return tokens