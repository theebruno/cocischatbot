import random
#for randomizing the response
import json
#to be able to load the intents.json file
import pickle
#for serialization purposes
import numpy as np
#for bagging process
import nltk

from nltk.stem import WordNetLemmatizer
#for a sort of refined way of stemming words that takes the root of the word and not a truncated formd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
#all the above are for creation of the neural nert model

lemmatizer = WordNetLemmatizer()
#create the lemmatizer to be used
intents = json.loads(open('intents.json').read())
#loading the json file for the intents

#creating lists for storing the words, classes and documents
words =[]
classes = []
documents = []
#specifying which characters to ignore
ignore_letters = ['?', '!', '.', ',']

#looping through the intents
for intent in intents['intents']:
	for pattern in intent['patterns']:
		word_list = nltk.word_tokenize(pattern)
		#add tokenized words to the words list
		words.extend(word_list)
		#store the class to which the appended word belongs
		documents.append((word_list, intent['tag']))
		if intent['tag'] not in classes:
			classes.append(intent['tag'])

#lemmatizing the words
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
#eliminate duplicates and sort the words
words = sorted(set(words))
classes = sorted(set(classes))

#store the lemmatized words and their classes
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# creating an empty list and a template of zeroes
training = []
output_empty = [0] * len(classes)

#creating an encoded bag of words
for document in documents:
	bag = []
	word_patterns = document[0]
	word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
	#check if word occurs in pattern and append a 0 or 1 in accordance
	for word in words:
		bag.append(1) if word in word_patterns else bag.append(0)
	#copy the list 
	output_row = list(output_empty)
	#find out class in the index and append the 1 to the training list
	output_row[classes.index(document[1])] = 1
	training.append([bag, output_row])

#shuffle the training data to reduce bias of model towards order of appearance
random.shuffle(training)
training = np.array(training)

#split it into x and y values into features and labels for training the neural network
train_x = list(training[:, 0])
train_y = list(training[:, 1])

#building the neural network using a sequential model
model = Sequential()

#adding input layer as first layer and activation function as a rectified linear unit
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
#in order to prevent overfitting add dropout layer
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
#add the last output layer with softmax function that allows us to sum up the percentages to add up to 1 and show the likelyhood of each neuron being the right choice
model.add(Dense(len(train_y[0]), activation='softmax'))


#adding stochastic gradient descent optimizer to find the model parameters that correspond to the best fit between predicted and actual outputs
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#specifying the input and output data
hist = model.fit(np.array(train_x), np.array(train_y), epochs=300, batch_size=5, verbose=1)

#saving the chatbot model
model.save('chatbotmodel.h5', hist)

#prompting for complete training
print("Done")