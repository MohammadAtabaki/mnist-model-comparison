# -*- coding: utf-8 -*-
"""scratchpad

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/jakevdp/test-notebook-links/blob/master/scratchpad.ipynb

# Hello
"""

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
import matplotlib.pyplot as plt

mnist_data = fetch_openml('mnist_784')

X = mnist_data.data
y = mnist_data.target

has_nan = pd.DataFrame(mnist_data.data).isna().any().any()
print(has_nan)
X.shape

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.2, random_state=42)

lr = LogisticRegression(max_iter=100)
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

confusion_matrix(y_test, y_pred)
print('acc: ',accuracy_score(y_test, y_pred))
print('f1 score: ',f1_score(y_test, y_pred, average='macro'))

X_test_np =X_test.to_numpy()
y_test_np = y_test.to_numpy()

plt.figure(figsize=(12,6), dpi=150)
for i in range (16):
  plt.subplot(4,4,i+1)
  plt.imshow(X_test_np[i].reshape(28,28), cmap='gray')
  true_label = y_test_np[i]
  pred_label = y_pred [i]
  plt.title(f'True: {true_label}, Pred: {pred_label}')
  plt.axis('off')

plt.tight_layout()
plt.show()

svc = SVC()
svc.fit(X_train, y_train)

y_pred_svc = svc.predict(X_test)

print('acc: ',accuracy_score(y_test, y_pred_svc))
print('f1 score: ',f1_score(y_test, y_pred_svc, average='macro'))

rfc = RandomForestClassifier(n_estimators=100, random_state=42)
rfc.fit(X_train, y_train)

y_pred_rfc = rfc.predict(X_test)

print('acc: ',accuracy_score(y_test, y_pred_rfc))
print('f1 score: ',f1_score(y_test, y_pred_rfc, average='macro'))