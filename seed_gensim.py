""" Uses gensim to analyze the text of the responses to the main questions of the SEED Survey """

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim


def create_topic_model(list_responses):
    topic_model_dictionary = create_topic_model_dictionary(list_responses)


def create_topic_model_dictionary(list_responses):
    """ Create a topic model dictionary from responses """
    # create the objects needed to prepare the dictionary
    tokenizer = RegexpTokenizer(r'\w+')
    en_stop = get_stop_words('en')
    p_stemmer = PorterStemmer()
    texts_to_analyze = []
    # loop through the list of responses
    for i in list_responses:
        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)
        # remove the stop words from tokens
        stopped_tokens = [i for i in tokens if not i in en_stop]
        # stem the tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        # add tokens to list of texts to analyze
        texts_to_analyze.append(stemmed_tokens)
        # turn the tokenized documents into a id <-> term dictionary
        topic_model_dictionary = corpora.Dictionary(texts_to_analyze)
    return topic_model_dictionary
