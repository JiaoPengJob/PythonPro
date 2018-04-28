#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

dataset_filename = "affinity_dataset.txt"

X = np.loadtxt(dataset_filename)

# print(X[:4])

number_apple = 0
numnber_ban = 0
number_ab = 0

for sim in X:
    if sim[3] == 1:
        number_apple += 1
    if sim[4] == 1:
        numnber_ban += 1
    if sim[3] == 1 and sim[4] == 1:
        number_ab += 1
# print(str(number_apple)+","+str(numnber_ban)+","+str(number_ab))


from collections import defaultdict

vailds = defaultdict(int)
invalids = defaultdict(int)
occurances = defaultdict(int)

from sklearn.datasets import load_iris

dataset = load_iris()
print(str(dataset.target_names))
print(str(dataset.data.shape))
print(str(dataset.target))
