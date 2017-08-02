import numpy as np
from keras.layers import Dense
from keras.models import Sequential

import cnf_Matrix
from old import confusionMatrix

archive = raw_input('archivo .csv de datos: ')
weights = raw_input('archivo de pesos: ')
dataset = np.loadtxt('descriptors/'+archive+'.csv', delimiter=",") # corection is variable archive

X = dataset[:,0:128]
Y = dataset[:,128:135]

model = Sequential()
model.add(Dense(128, input_dim=128, kernel_initializer='normal', activation='relu'))
model.add(Dense(32,activation='relu'))
model.add(Dense(32,activation='relu'))
model.add(Dense(6, kernel_initializer='normal', activation='sigmoid'))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

model.load_weights('weigths/'+weights+'.h5')
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# calculate prediction
predictions = model.predict(X)
cnf_Matrix.cnf_matrix(predictions, Y)
#confusionMatrix.cnf_matrix(predictions, Y)