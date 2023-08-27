# School Chatbot
import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)         # Breaks sentences to words(tokens)

def stem(word):                                 
    return stemmer.stem(word.lower())           # Return the stems of the words

def bag_of_words(tokenized_sentence,all_words):
    pass

# a = 'How long is your pen'
# print(a)
# a = tokenize(a)
# print(a)

words = ['eating',"eats","ate"]
stemmed_words = [stem(w) for w in words]
print(stemmed_words)