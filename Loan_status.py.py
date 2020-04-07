# -*- coding: utf-8 -*-
"""Bank Loan .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cn6z70s9VYQG25HwjSdBl4ex5zAoqkEN
"""

from google.colab import files
import io
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import seaborn as sns
from sklearn.svm import SVC


uploaded = files.upload()

df = pd.read_csv(io.BytesIO(uploaded['Bank loan data.csv']))

df.head()

data = df.drop(['Loan_ID','CoapplicantIncome','Married','Dependents','LoanAmount','Loan_Amount_Term','Property_Area'] , axis=1)

data.head()

#X = data.iloc[:,:-1]    # (Loan_ID,	Gender,	Education,	Self_Employed,	ApplicantIncome,	Credit_History,	Property_Area,	Loan_Status)
#y = data.iloc[:,-1]     # Loan Status

data.isnull().sum()

data['Gender'].fillna('Male',inplace=True)
data['Self_Employed'].fillna('No', inplace=True)
data['Credit_History'].fillna(1.0, inplace=True)



label_enc_X = LabelEncoder()
data_col = ['Gender',	'Education',	'Self_Employed',	'Loan_Status']

for i in data_col:
  data[i] = label_enc_X.fit_transform(data[i])


X = data.iloc[:,:-1].values   # (	Gender,	Education,	Self_Employed,	ApplicantIncome,	Credit_History)

y = data.iloc[:,-1].values   # Loan Status




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)





plt.plot(X,y)
plt.xlabel('ApplicantIncome')
plt.ylabel('Loan Status')
plt.show()



sns.pairplot(data)

X_TRAIN = np.array(X_train).reshape(1,-1)
Y_TRAIN = np.array(y_train).reshape(1,-1)
X_TEST = np.array(X_test).reshape(1,-1)
Y_TEST = np.array(y_test).reshape(1,-1)

Y_TEST

''' SVM  '''


X_TRAIN = np.array(X_train).reshape(1,-1)
Y_TRAIN = np.array(y_train).reshape(-1,1)
X_TEST = np.array(X_test).reshape(-1,1)
Y_TEST = np.array(y_test).reshape(-1,1)

classifier = SVC(kernel='linear')
classifier.fit(X_train, Y_TRAIN)
y_pred = classifier.predict(X_test)

print('Confusion Matrix\n {}\n\n'.format(confusion_matrix(Y_TEST,y_pred)))
print('Classification Report \n {}\n\n'.format(classification_report(Y_TEST,y_pred)))
print('SVC Accuracy - \t {}\n'.format(classifier.score(X_test, Y_TEST)))



'''    For predicting the output '''

classifier.predict(X_test)

classifier.predict([[ 4.54299688e-01,  1.85024956e+00, -3.80160683e-01,
        -2.51883331e-01,  4.07763147e-01]])

classifier.predict([[ 4.54299688e-01,  1.85024956e+00, -3.80160683e-01,
        -6.19638466e-01, -2.45240407e+00],])




