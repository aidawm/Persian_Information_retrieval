
class MostFrequences :
    def __init__(self) -> None:
        self.term_dictionary = {}

    def count_terms(self,tokens):
        for t in tokens:
            if t == "":
                 continue
            if (t in self.term_dictionary.keys()):
                self.term_dictionary[t]+=1
            else:
                self.term_dictionary[t]=1
    
    def find_most_freq_terms(self):
        the_most_freq_terms= sorted(self.term_dictionary.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(the_most_freq_terms)


        with open('sorted_term_freq.txt', 'w') as f:
                for line in converted_dict.keys():
                    f.write(f"{line}\t {self.term_dictionary[line]}\n")


        terms = list(converted_dict.keys())
        terms = terms[0:50]
        with open('50_most_freq_terms.txt', 'w') as f:
                for line in terms:
                    f.write(f"{line}\t {self.term_dictionary[line]}\n")


