class WordTokenizer:
    def simple_tokenizer(self,text):    

        text = text.replace("\t", " ")
        text = text.replace("\n", " ")
        text = text.replace("\u200c", " ")
        text = text.replace(u'\xa0', " ")

        tokens = text.split(" ")

        return tokens
    


    def delete_punctuations_symbols(self,text):
        punctuations = [".","،",",","!","?","\"","\'","(",")","{","}","[","]","/","\\",":"]
        for p in punctuations:
            text = text.replace(p,"")

        return text
    

    def process_verbs(self,token: list[str]):
        del_index = []
        for i,t in enumerate(token):
            if t == "می":
                token[i+1] = "می"+ token[i+1]
                del_index.append(i)

        for i in range(len(del_index)-1,-1,-1):
            token.pop(del_index[i])
        
        return token