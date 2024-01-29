class Normalizer:
    def __init__(self):
        
        f = open("diacritics.txt", 'r')
        self.diacritics = f.readlines()
        self.diacritics = [t.replace("\n","") for t in self.diacritics]

    
    
    def delete_useless_tokens(self,tokens:list[str]):

        del_index = []
        useless_tokens = ["ی","ای"]
        for i,t in enumerate(tokens):
            if (t in useless_tokens):
                del_index.append(i)
            
            if t == "های" or t=="هایی": 
                tokens[i] = "ها"
            if t == "تری": 
                tokens[i] = "تر"
            if t == "ترینی": 
                tokens[i] = "ترین"
            if t == "های" or t=="هایی": 
                tokens[i] = "ها"
        
        for i in range(len(del_index)-1,-1,-1):
            tokens.pop(del_index[i])

    
    def normalize_alphabets(self,token:str):
        for d in self.diacritics:
            token = token.replace(d,"")

        token = token.replace("ؤ","و")
        token = token.replace("ئ","ی")
        token = token.replace("ي","ی")
        token = token.replace("إ","ا")
        token = token.replace("أ","ا")
        token = token.replace("آ","ا")
        token = token.replace("ة","ه")
        token = token.replace("ك","ک")

        return token
    
    def normalize_numbers(self,token:str):
        token = token.replace("0","۰")
        token = token.replace("1","۱")
        token = token.replace("2","۲")
        token = token.replace("3","۳")
        token = token.replace("4","۴")
        token = token.replace("5","۵")
        token = token.replace("6","۶")
        token = token.replace("7","۷")
        token = token.replace("8","۸")
        token = token.replace("9","۹")

        return token
        

    def normalize_tokens(self,tokens:list[str]):
        for i,t in enumerate(tokens):
            # tokens[i] = self.delete_punctuations_symbols(tokens[i])
            tokens[i] = self.normalize_alphabets(tokens[i])
            tokens[i] = self.normalize_numbers(tokens[i])
        
        tokens = self.process_verbs(tokens)
        tokens = self.process_nouns(tokens)
        return tokens


    def process_verbs(self,tokens: list[str]):
        return self.correct_spacing(tokens,["می","نمی"],before_word=True)

    
    def process_nouns(self,tokens: list[str]):
        self.delete_useless_tokens(tokens)
        return self.correct_spacing(tokens,["ها","تر","ترین","گر","گری","ام","ات","اش"],before_word=False)

    def correct_spacing(self,tokens:list[str],list_of_corrections,before_word=True):
        del_index = []
        for i,t in enumerate(tokens):
            if t in list_of_corrections: 
                if(before_word):
                    t = t+ "\u200c"
                    tokens[i+1] = t+ tokens[i+1]
                else:
                    a = tokens[i-1]+ "\u200c"
                    tokens[i-1] = a+t

                del_index.append(i)

        for i in range(len(del_index)-1,-1,-1):
            tokens.pop(del_index[i])
        
        return tokens