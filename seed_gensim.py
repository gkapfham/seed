""" Uses gensim to analyze the text of the responses to the main questions of the SEED Survey """

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim


def create_topic_model(list_responses, num_topics_requested):
    """ Using LDA from gensim, create the topic model from the list of responses """
    topic_model_dictionary, texts_to_analyze = create_topic_model_dictionary(list_responses)
    # convert tokenized documents into a document-term matrix, or the corpus
    topic_model_corpus = [topic_model_dictionary.doc2bow(text) for text in texts_to_analyze]
    # generate LDA model from the texts_to_analyze and the topic_model_dictionary
    lda_model = gensim.models.ldamodel.LdaModel(topic_model_corpus, num_topics=num_topics_requested, id2word=topic_model_dictionary, passes=20)
    return lda_model, topic_model_corpus, texts_to_analyze


def create_topic_model_dictionary(list_responses):
    """ Create a topic model dictionary from the list of responses """
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
    return topic_model_dictionary, texts_to_analyze


def show_topic_model_textually(seed_gensim_topic_model, seed_gensim_corpus, texts_to_analyze, num_topics):
    """ Using only textual output provide a basic display of the topic model """
    print(seed_gensim_topic_model)
    print(seed_gensim_topic_model.print_topics(num_topics))
    print()
    # print("Analysis:")
    # for single_corpus, textual_document in zip(seed_gensim_corpus, texts_to_analyze):
        # print(single_corpus)
        # print(textual_document)
        # print(seed_gensim_topic_model[single_corpus])
    # print()
