class WordTokenizer:
    def __init__(self) -> None:
        self. punctuations = ["،",",","!","?","\"","\'","(",")","{","}","[","]","/","\\",";","؛","»","«",">","<",":"]
    
    def delete_punctuations_symbols(self,text:str):

        for p in self.punctuations:
            text = text.replace(p," ")
        return text
    
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

            if(text[dot_index-1]>= "0" and text[dot_index+1]<="9"):
                continue
            elif ((text[dot_index-1]>= "a" and text[dot_index+1]<="z") or (text[dot_index-1]>= "A" and text[dot_index+1]<="Z")):
                continue
            else: 
                
                text_list[dot_index] = " "

        
        text = "".join(text_list)
        text = self.delete_punctuations_symbols(text)
        tokens = text.split(" ")
        
                
        return tokens
    