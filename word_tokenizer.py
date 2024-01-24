class WordTokenizer:
    def simple_tokenizer(self,text):    

        text = text.replace("\t", " ")
        text = text.replace("\n", " ")
        text = text.replace("\u200c", " ")
        text = text.replace(u'\xa0', " ")

        tokens = text.split(" ")

        return tokens
    