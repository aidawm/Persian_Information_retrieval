class Normalizer:
    def __init__(self):
        self. punctuations = [".","،",",","!","?","\"","\'","(",")","{","}","[","]","/","\\",";","؛","»","«",">","<",":"]
        f = open("diacritics.txt", 'r')
        self.diacritics = f.readlines()
        self.diacritics = [t.replace("\n","") for t in self.diacritics]

    def delete_punctuations_symbols(self,token:str):

        for p in self.punctuations:
            token = token.replace(p,"")

        return token
    
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
            tokens[i] = self.delete_punctuations_symbols(tokens[i])
            tokens[i] = self.normalize_alphabets(tokens[i])
            tokens[i] = self.normalize_numbers(tokens[i])

