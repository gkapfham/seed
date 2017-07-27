""" Uses gensim to analyze the text of the responses to the main questions of the SEED Survey """

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
