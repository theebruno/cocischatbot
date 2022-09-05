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

#
training = []
output_empty = [0] * len(classes)

for document in documents:
	bag = []
	word_patterns = document[0]
	word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
	for word in words:
		bag.append(1) if word in word_patterns else bag.append(0)
	output_row = list(output_empty)
	output_row[classes.index(document[1])] = 1
	training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))


sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbotmodel.h5', hist)

print("Done")