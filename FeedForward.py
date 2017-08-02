from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from datetime import datetime


# seed
np.random.seed(7)

descriptor = raw_input('archivo csv descriptor: ')
weights = raw_input(' archivo de salida h5 pesos: ')
#load dataset
dataset = np.loadtxt("descriptors/"+descriptor+".csv", delimiter=",")
X = dataset[:,0:128]
Y = dataset[:,128:135]

timeInitial = datetime.now()
# create model
model = Sequential() # pila lineal de capas

model.add(Dense(128, input_dim=128, init='normal', activation='sigmoid'))
model.add(Dense(32,activation='sigmoid'))
model.add(Dense(32,activation='sigmoid'))
model.add(Dense(6, init='normal', activation='sigmoid'))
# Compile model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
# Fit the model


model.fit(X, Y, epochs=100, verbose=2)
model.save_weights('weigths/'+weights+'.h5')
timeFinal = datetime.now()
time = timeFinal - timeInitial;
print  time
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# calculate prediction
predictions = model.predict(X).round()
#print model.predict_proba(X)
#print predictions