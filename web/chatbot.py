import random
# for randomizing the response
import json
# to be able to load the intents.json file
import pickle
# for serialization purposes
import numpy as np
# for bagging process
import nltk

nltk.download('punkt')

from nltk.stem import WordNetLemmatizer
# for a sort of combined tokenization and stemming
from tensorflow.keras.models import load_model

from django.db.models import Q

from apps.events.models import Event

# from rest_framework.response import Response
# from django.http import JsonResponse
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

# for loading the model that we created in training.py

# create the lemmatizer to be used
lemmatizer = WordNetLemmatizer()

# loading the json file for the intents
intents = json.loads(open('intents.json').read())

# load the pickle files in reading binary mode
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# loading the model
model = load_model('chatbotmodel.h5')


# @api_view(['GET', 'POST', ])
# def respond(request):
#     if request.method == 'GET':
#         # Retrieve the name from url parameter
#         # name = request.GET.get('query', None)
#         name = request.query_params.get('query', None)
#         ints = predict_class(name)
#         res = get_response(ints, intents)
#         return JsonResponse({"response": res})


@api_view(['GET', 'POST', ])
def respond(request):
    if request.method == 'GET':
        # Retrieve the name from url parameter
        # name = request.GET.get('query', None)
        name = request.query_params.get('query', None)
        namee = name.lower()

        if namee.find('event') != -1:
            foo = ""
            res = Event.objects.all()

            for name in res:
                organised_by = " organised by "
                date_of_event = " date is "
                location_of_event = " location is "
                comma = " , "
                ccc = " "

                foo += str(ccc) + str(name.name) + \
                       str(organised_by) + str(name.organiser) +\
                       str(location_of_event) + str(name.location) + \
                       str(date_of_event) + str(name.event_date) + comma
            return JsonResponse({"response": foo})
        else:
            ints = predict_class(name)
            res = get_response(ints, intents)
            return JsonResponse({"response": res})


# function for legitimating and tokenizing the sentence
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# function for conversion of a sentence into a list that denotes the occurence of a word in the
# sentence using 0s and 1s
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


# function for predicting the class a sentence falls under
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    res_index = np.argmax(res)
    global var
    var = 0
    if res[res_index] < 0.6:
        var = 1
    # specifies the level of uncertainity that is acceptable for our model prediction
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    # sort in descending order with highest probability first
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


# function for gettig the response based off the class predicted by the model
def get_response(intents_list, intents_json):
    try:
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if var == 1:
                result = "I have not quite understood your question please rephrase it for me"
            elif i['tag'] == tag:
                result = random.choice(i['responses'])
                break
        return result
    except:
        result = "I am having a hard time understanding your question please rephrase it for me"
        return result


print("Chatbot is now active")

# loop for running the chatbot
while True:
    try:
        message = input("")
    except EOFError:
        break
    if message == "quit":
        break
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)
