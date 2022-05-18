# python -m pip install numpy
# python -m pip install --user pandas
# python -m pip install matplotlib
# python -m pip install scikit-learn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

bream_length = pd.read_csv(
    "C:\green_workspace\downloads\시험\R패키지활용프로그래밍\csv파일/bream_length.csv", header=None)
bream_weight = pd.read_csv(
    "C:\green_workspace\downloads\시험\R패키지활용프로그래밍\csv파일/bream_weight.csv", header=None)
smelt_length = pd.read_csv(
    "C:\green_workspace\downloads\시험\R패키지활용프로그래밍\csv파일/smelt_length.csv", header=None)
smelt_weight = pd.read_csv(
    "C:\green_workspace\downloads\시험\R패키지활용프로그래밍\csv파일/smelt_weight.csv", header=None)

# print(bream_length)
# print("="*58)
# print(bream_weight)
# print("="*58)
# print(smelt_length)
# print("="*58)
# print(smelt_weight)
# print("="*58)

# print(type(bream_length))
# print(type(bream_weight))
# print(type(smelt_length))
# print(type(smelt_weight))
# print("="*58)

# print(bream_length.shape)
# print(bream_weight.shape)
# print(smelt_length.shape)
# print(smelt_weight.shape)
# print("="*58)

length = np.concatenate([bream_length, smelt_length])
weight = np.concatenate([bream_weight, smelt_weight])

# plt.scatter(length, weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

# print(length)
# print("="*58)
# print(weight)
# print("="*58)

# print(length.shape)
# print("="*58)
# print(weight.shape)
# print("="*58)

fish_data = np.column_stack((length, weight))

# print(fish_data)
# print(fish_data.shape)
# print("="*58)

fish_target = [1] * 35 + [0] * 14

# print(fish_target)

train_input = fish_data[:35]
train_target = fish_target[:35]

test_input = fish_data[35:]
test_target = fish_target[35:]

input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

# print(input_arr)
# print(target_arr)

# print(input_arr.shape)

np.random.seed(42)
index = np.arange(49)
np.random.shuffle(index)
# print(index)

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]

plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(test_input[:, 0], test_input[:, 1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
