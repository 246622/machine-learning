# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:58:25 2022

@author: my_vegetable_dog
"""

import numpy as np
from sklearn.metrics import accuracy_score
from lib.svm_smo import SVM
# X 数据
# y 标签
# X_train, y_train, X_test, y_test
models = []
for i in range(3):
    y_i = 2 * (y==i).astype(np.int).reshape(-1,1) - 1
    y_train = y_i[selected_indices]
    model.fit(X_train, y_train, N = 10)
    models.append(model)

y_preds = np.arrray([model.predict(X_test) for model in models]).reshape(3, len(X_test))