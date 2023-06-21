import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

lines = []
with open("/content/Xtrain.txt", "r") as xtrain:
    lines = xtrain.readlines()
    for idx, elem in enumerate(lines):
        lines[idx] = eval(lines[idx].rstrip())

Xtrain = pd.DataFrame(lines).astype(float)

with open("/content/Ytrain.txt", "r") as ytrain:
    lines = ytrain.readlines()
    for idx, elem in enumerate(lines):
        lines[idx] = eval(lines[idx].rstrip())

Ytrain = pd.DataFrame(lines).astype(float)

with open("/content/Xtest.txt", "r") as xtest:
    lines = xtest.readlines()
    for idx, elem in enumerate(lines):
        lines[idx] = eval(lines[idx].rstrip())

Xtest = pd.DataFrame(lines).astype(float)

with open("/content/Ytest.txt", "r") as ytest:
    lines = ytest.readlines()
    for idx, elem in enumerate(lines):
        lines[idx] = eval(lines[idx].rstrip())

Ytest = pd.DataFrame(lines).astype(float)

for idx in range(164, 183, 2):
    Xtrain[idx] = scaler.fit_transform(Xtrain[[idx]])
    Xtest[idx] = scaler.fit_transform(Xtest[[idx]])

pca = PCA(n_components=2)
pca.fit(X=Xtrain)
df_pca = pd.DataFrame(data=pca.transform(Xtrain))

x_val = df_pca[0]
y_val = df_pca[1]
markers = ["o" if val == 0 else "*" for val in Ytrain[0]]
colors = ["blue" if val == 0 else "red" for val in Ytrain[0]]

for x, y, marker, color in zip(x_val, y_val, markers, colors):
    plt.scatter(x, y, marker=marker, color=color)

plt.xlabel("x")
plt.ylabel("y")
plt.show()

print("============================")
print(pca.explained_variance_ratio_)
print("============================")

layers = [
    tf.keras.layers.InputLayer(input_shape=(183,)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(64, activation=tf.nn.relu),
    tf.keras.layers.Dense(1, activation=tf.nn.sigmoid),
]

MLP = tf.keras.Sequential(layers)
MLP.compile(optimizer="Adam", loss="mean_squared_error", metrics=["accuracy"])

MLP.summary()

early_stop = tf.keras.callbacks.EarlyStopping(patience=2, verbose=1, monitor="val_acc", mode="max", min_delta=0.001, restore_best_weights=True)

Xtrain_array = Xtrain.values
Ytrain_array = Ytrain.iloc[:, 0].to_frame().values
Ytrain_array = np.expand_dims(Ytrain_array, axis=1)
Xtest_array = Xtest.values
Ytest_array = Ytest.iloc[:, 0].to_frame().values


train_dataset = tf.data.Dataset.from_tensor_slices((Xtrain_array, Ytrain_array))
test_dataset = tf.data.Dataset.from_tensor_slices((Xtest_array, Ytest_array))


batch_size = 32
train_dataset = train_dataset.batch(batch_size)
test_dataset = test_dataset.batch(batch_size)


MLP.fit(train_dataset, epochs=20, validation_data=test_dataset)
