import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

# The weather dataset

# This tutorial uses a weather time series dataset recorded by the Max Planck Institute for Biogeochemistry.

# This dataset contains 14 different features such as air temperature, atmospheric pressure, and humidity.
#  These were collected every 10 minutes, beginning in 2003. For efficiency, you will use only the data collected 
#  between 2009 and 2016. This section of the dataset was prepared by François Chollet for his book Deep Learning 
# with Python.

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

# zip_path = tf.keras.utils.get_file(
#     origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
#     fname='jena_climate_2009_2016.csv.zip',
#     extract=True)
# csv_path, _ = os.path.splitext(zip_path)

df = pd.read_csv("EUR_USD-1min.csv")
# slice [start:stop:step], starting from index 5 take every 6th record.
# df = df[5::2]
date_time = pd.to_datetime(df.pop('datetime'), format='%Y-%m-%d %H:%M:%S')

# print(df.head())

# plot_cols = ['open', 'high', 'low', 'close']
# plot_features = df[plot_cols]
# plot_features.index = date_time
# _ = plot_features.plot(subplots=True)

# plot_features = df[plot_cols][:480]
# plot_features.index = date_time[:480]
# _ = plot_features.plot(subplots=True)

# plt.show()

print(df.describe().transpose())

# wv = df['wv (m/s)']
# bad_wv = wv == -9999.0
# wv[bad_wv] = 0.0

# max_wv = df['max. wv (m/s)']
# bad_max_wv = max_wv == -9999.0
# max_wv[bad_max_wv] = 0.0

# # The above inplace edits are reflected in the DataFrame
# # df['wv (m/s)'].min()

# print(df.describe().transpose())

# plt.hist2d(df['wd (deg)'], df['wv (m/s)'], bins=(50, 50), vmax=400)
# plt.colorbar()
# plt.xlabel('Wind Direction [deg]')
# plt.ylabel('Wind Velocity [m/s]')

# wv = df.pop('wv (m/s)')
# max_wv = df.pop('max. wv (m/s)')

# # Convert to radians.
# wd_rad = df.pop('wd (deg)')*np.pi / 180

# # Calculate the wind x and y components.
# df['Wx'] = wv*np.cos(wd_rad)
# df['Wy'] = wv*np.sin(wd_rad)

# # Calculate the max wind x and y components.
# df['max Wx'] = max_wv*np.cos(wd_rad)
# df['max Wy'] = max_wv*np.sin(wd_rad)


# plt.hist2d(df['Wx'], df['Wy'], bins=(50, 50), vmax=400)
# plt.colorbar()
# plt.xlabel('Wind X [m/s]')
# plt.ylabel('Wind Y [m/s]')
# ax = plt.gca()
# ax.axis('tight')

#convert the datetime column to seconds
timestamp_s = date_time.map(datetime.datetime.timestamp)
# print(timestamp_s)


#split data into train, validation and test sets
column_indices = {name: i for i, name in enumerate(df.columns)}

n = len(df)
train_df = df[0:int(n*0.7)]
val_df = df[int(n*0.7):int(n*0.9)]
test_df = df[int(n*0.9):]

num_features = df.shape[1]
# print(num_features)

train_mean = train_df.mean()
train_std = train_df.std()

train_df = (train_df - train_mean) / train_std
val_df = (val_df - train_mean) / train_std
test_df = (test_df - train_mean) / train_std

#plot normalized data
df_std = (df - train_mean) / train_std
df_std = df_std.melt(var_name='Column', value_name='Normalized')
plt.figure(figsize=(12, 6))
ax = sns.violinplot(x='Column', y='Normalized', data=df_std)
_ = ax.set_xticklabels(df.keys(), rotation=90)


plt.show()


#_______________










