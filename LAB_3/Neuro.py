from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation
from keras.optimizers import SGD
import logging
import TA



model = Sequential()
model.add(Dense(units=10,activation='relu',input_dim=5,name="Layer_1"))
model.add(Dropout(0.2,name="Layer_2"))
model.add(Dense(units=10,activation='relu',name="Layer_3"))
model.add(Dropout(0.2,name="Layer_4"))
model.add(Dense(units=1,name="Final_Layer"))

model.compile(loss='mse',optimizer=SGD(learning_rate=0.01))


model.fit(X_train,
          y_train,
          batch_size=32,
          nb_epoch =10)


score =  model.evaluate(x_test,y_test,batch_size=32)

print("Test Loss", score[0])
print("Test accuracy:", score[1])


