import random
import json 
import pickle
import numpy as numpy
import nltk

from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', rb))
classes = pickle.load(open('classes.pkl', rb))
model = load_model('chatbot_model.model')