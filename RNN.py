from pandas import read_csv
from matplotlib import pyplot
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout, concatenate
import os


# load dataset
dtsname = 'price data/1min/EUR_GBP'
dataset = read_csv(dtsname, header=0, index_col=0)
# values = dataset.values
# # specify columns to plot
# groups = [0, 1, 2, 3, 4]
# i = 1
# # plot each column
# pyplot.figure()
# for group in groups:
# 	pyplot.subplot(len(groups), 1, i)
# 	pyplot.plot(values[:, group])
# 	pyplot.title(dataset.columns[group], y=0.5, loc='right')
# 	i += 1
# pyplot.show()

# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg

# load dataset
# dataset = read_csv('price data/1min/EUR_GBP', header=0, index_col=0)
values = dataset.values
# integer encode direction
encoder = LabelEncoder()
values[:,4] = encoder.fit_transform(values[:,4])
# ensure all data is float
values = values.astype('float32')
# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
# frame as supervised learning
reframed = series_to_supervised(scaled, 1, 1)
# drop columns we don't want to predict
reframed.drop(reframed.columns[[9,10,11,12,13,14,15]], axis=1, inplace=True)
print(reframed.head())



# split into train and test sets
values = reframed.values
train_number = 15000
train = values[:train_number, :]
test = values[train_number:, :]
# split into input and outputs
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

numberUnits = 200
opt = 'adam'
lss = 'mse'
drpout = 0.125
# design network
model = keras.models.Sequential()
model.add(LSTM(units = numberUnits, return_sequences = True, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dropout(drpout))
model.add(LSTM(units=numberUnits, return_sequences=True))
model.add(Dropout(drpout))
model.add(LSTM(units=numberUnits, return_sequences=True))
model.add(Dropout(drpout))
model.add(LSTM(units=numberUnits))
model.add(Dropout(drpout))
model.add(Dense(units=125))
model.compile(loss=lss, optimizer=opt, metrics=['accuracy'])
# fit network

history = model.fit(train_X, train_y, epochs=20, batch_size=32, validation_data=(test_X, test_y), verbose=2, shuffle=False)
# if(not os.path.exists(dtsname + '_opt-' + opt + '_loss-' + lss + '_dropout-' + str(drpout) + '_units-' + str(numberUnits) + '_stock_prediction.h5')):
#     model.save(dtsname + '_opt-' + opt + '_loss-' + lss + '_dropout-' + str(drpout) + '_units-' + str(numberUnits) + '_stock_prediction.h5')
#
# model = load_model(dtsname + '_opt-' + opt + '_loss-' + lss + '_dropout-' + str(drpout) + '_units-' + str(numberUnits) + '_stock_prediction.h5')

# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()

predictions = model.predict(test_X)
predictions = scaler.inverse_transform(predictions)

fig, ax = plt.subplots(figsize=(8,4))
plt.plot(df, color='red',  label="True Price")
ax.plot(range(len(train_y)+50,len(train_y)+50+len(predictions)),predictions, color='blue', label='Predicted Testing Price')
plt.legend()
plt.show()

# make a prediction
yhat = model.predict(test_X)
pyplot.plot(yhat)
test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
# invert scaling for forecast
inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,0]
# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,0]
# calculate RMSE
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.3f' % rmse)



# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import MinMaxScaler
# from keras.models import Sequential, load_model
# from keras.layers import LSTM, Dense, Dropout
# import os
#
# ### Loading in Dataset
#
# df = pd.read_csv('price data/5min/EUR_GBP')
# df = df[1:]
# # print(df.head())
#
# dftrain = pd.read_csv('price data/5min/EUR_USD')
# dftrain = dftrain[1:]
# # print(df[['open', 'high', 'low', 'close', 'ma1', 'wma1', 'upper_band1',  'middle_band1', 'lower_band1', 'rsi1']].head())
#
# # exit()
# ### Preprocessing and Feature Extraction
#
# df = df['open'].values
# df = df.reshape(-1, 1)
#
# dftrain = dftrain['open'].values
# dftrain = dftrain.reshape(-1, 1)
# # print(df.shape)
#
# # exit()
#
# dataset_train = np.array(dftrain)
# print(dataset_train[:5])
# dataset_test = np.array(df[int(df.shape[0]*0.8)-50:])
# print(dataset_test[:5])
# print(dataset_train.shape)
# print(dataset_test.shape)
#
# # exit()
#
# scaler = MinMaxScaler(feature_range=(0,1))
# dataset_train = scaler.fit_transform(dataset_train)
# dataset_train[:5]
#
# dataset_test = scaler.transform(dataset_test)
# dataset_test[:5]
#
# def create_dataset(df):
#     x = []
#     y = []
#     for i in range(50, df.shape[0]):
#         x.append(df[i-50:i, 0])
#         y.append(df[i, 0])
#     x = np.array(x)
#     y = np.array(y)
#     return x,y
#
# x_train, y_train = create_dataset(dataset_train)
# print(x_train[:1])
#
# x_test, y_test = create_dataset(dataset_test)
# print(x_test[:1])
#
# # Reshape features for LSTM Layer
# x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
# x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
#
# ### Building Model
#
# numberUnits = 125
#
# model = Sequential()
# model.add(LSTM(units=numberUnits, return_sequences=True, input_shape=(x_train.shape[1], 1)))
# model.add(Dropout(0.1))
# model.add(LSTM(units=numberUnits, return_sequences=True))
# model.add(Dropout(0.1))
# model.add(LSTM(units=numberUnits, return_sequences=True))
# model.add(Dropout(0.1))
# model.add(LSTM(units=numberUnits))
# model.add(Dropout(0.1))
# model.add(Dense(units=1))
#
# model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
#
# if(not os.path.exists('stock_prediction.h5')):
#     model.fit(x_train, y_train, epochs=2, batch_size=32)
#     model.save('stock_prediction.h5')
#
# model = load_model('stock_prediction.h5')
#
# ### Visualizing Results
#
# print("eeeeeeee" +  str(x_test[1][2]))
# predictions = model.predict(x_test)
# predictions = scaler.inverse_transform(predictions)
#
# fig, ax = plt.subplots(figsize=(8,4))
# plt.plot(df, color='red',  label="True Price")
# ax.plot(range(len(y_train)+50,len(y_train)+50+len(predictions)),predictions, color='blue', label='Predicted Testing Price')
# plt.legend()
# plt.show()
#
# y_test_scaled = scaler.inverse_transform(y_test.reshape(-1, 1))
#
# fig, ax = plt.subplots(figsize=(8,4))
# ax.plot(y_test_scaled, color='red', label='True Testing Price')
# plt.plot(predictions, color='blue', label='Predicted Testing Price')
# plt.legend()
# plt.show()
#
# exit()
#
# x = x_test[-1]
# num_timesteps = 100
# preds = []
# for i in range(num_timesteps):
#     data = np.expand_dims(x, axis=0)
#     prediction = model.predict(data)
#     prediction = scaler.inverse_transform(prediction)
#     preds.append(prediction[0][0])
#     x = np.delete(x, 0, axis=0) # delete first row
#     x = np.vstack([x, prediction]) # add prediction
#
# print(preds)
