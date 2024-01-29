class WordTokenizer:
    def __init__(self) -> None:
        self. punctuations = ["،",",","!","?","\"","\'","(",")","{","}","[","]","/","\\",";","؛","»","«",">","<",":"]
    
    def delete_punctuations_symbols(self,text:str):

        for p in self.punctuations:
            text = text.replace(p," ")
        return text
    
    def isAlphaOrNum(self,c):
        if (c >= "a" and c <="z"):
            return True
        
        if (c >= "A" and c <="Z"):
            return True
        
        if (c >= "0" and c <="9"):
            return True
        
        return False

    def tokenize(self,text:str):    

        text = text.replace("\t", " ")
        text = text.replace("\n", " ")
        # text = text.replace("\u200c", " ")
        text = text.replace(u'\xa0', " ")

        dot_number = text.count(".")
        last_dot_index = -1
        text_list = list(text)
        for i in range(dot_number):

            dot_index = text.find(".",last_dot_index+1)
            last_dot_index = dot_index
            
            if (self.isAlphaOrNum(text_list[dot_index-1]) and self.isAlphaOrNum(text_list[dot_index+1])):
                continue
            else: 
                text_list[dot_index] = " "

        
        text = "".join(text_list)
        text = self.delete_punctuations_symbols(text)
        tokens = text.split(" ")
        
                
        return tokens
    