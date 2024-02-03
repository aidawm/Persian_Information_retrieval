# Persian Information Retrieval 

This project is for Informaticontainingon Retrieval course which aims to implement a search engine for Free text queries on [Fars News Dataset](https://drive.google.com/file/d/1x-ypTPZ0R_T83YfCw-p55MaQtpCvkrsb/view?usp=sharing).

persian documentation of project -> [brawse this link](https://github.com/aidawm/Persian_Information_retrieval/blob/master/Project%20Report.pdf)

## Implementation 

### Data Preprocessing 

1. Tokenization -> it's implemented in word_tokenizer.py
2. Normalization -> it's implemented in word_normalizer.py
3. Stemming -> use the [parsivar](https://github.com/ICTRC/Parsivar) library
4. Removing Stopwords

### Creating a Positional Inverted Index 
An inverted index is a data structure used to store and organize information for efficient search and retrieval. It maps each term to the documents which the term appears in.
A positional Inverted Index is an extension of an inverted index that also stores the positions of each term in each document, usually as a list of integers. 

In this project the positional inverted index is implemented by dictionary python data structure in index_tokens.py.
in this phase also compute tf-idf for each term-document to be able to have ranked retrieval. 

### query Processing
1. do preprocess on query
2. Used Index elimination techniques such as creating champion list 
3. Compute cosine similarity between query terms and documents
4. Rank results based on most relevent results

this part is implemented in main.py in IR class.

## How to Use 
1. install project dependency -> `pip3 install parsivar`
2. clone the project
3. use IR's methods:
  - index_tokens() -> to do preprocess on dataset and create a positional index
  - load_dictionary() -> if you have created the positional index and you prefer to use it instead of create it again
  - save_dictionary() -> after calling index_tokens(), you can save your positional index for future!
  - get_queries() -> to find the most relevent documents to your queries. (**NOTE: The document list will be saved in a file with the same name as your query**)







