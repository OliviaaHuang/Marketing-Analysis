# Step 1 Import Libraries
import pandas as pd

# Step 2 Import dataset
dataset=pd.read_excel("a2_Dataset_90Percent.xlsx")

dataset.head()

# Step 3 Data cleaning
dataset.isna().sum()

dataset['DemAffl']=dataset['DemAffl'].fillna(dataset['DemAffl'].mode()[0])
dataset['DemAge']=dataset['DemAge'].fillna(dataset['DemAge'].mode()[0])
dataset['DemClusterGroup']=dataset['DemClusterGroup'].fillna(dataset['DemClusterGroup'].mode()[0])
dataset['DemGender']=dataset['DemGender'].fillna(dataset['DemGender'].mode()[0])
dataset['DemReg']=dataset['DemReg'].fillna(dataset['DemReg'].mode()[0])
dataset['DemTVReg']=dataset['DemTVReg'].fillna(dataset['DemTVReg'].mode()[0])
dataset['LoyalTime']=dataset['LoyalTime'].fillna(dataset['LoyalTime'].mean())

dataset.isna().sum()

# Step 4 Machine learning
from sklearn.preprocessing import LabelEncoder
number = LabelEncoder()

dataset['DemClusterGroup'] = number.fit_transform(dataset['DemClusterGroup'].astype('str'))
integer_mapping = {l: i for i, l in enumerate(number.classes_)}
print(integer_mapping)

dataset['DemGender'] = number.fit_transform(dataset['DemGender'].astype('str'))
integer_mapping = {l: i for i, l in enumerate(number.classes_)}
print(integer_mapping)

dataset['DemReg'] = number.fit_transform(dataset['DemReg'].astype('str'))
integer_mapping = {l: i for i, l in enumerate(number.classes_)}
print(integer_mapping)

dataset['DemTVReg'] = number.fit_transform(dataset['DemTVReg'].astype('str'))
integer_mapping = {l: i for i, l in enumerate(number.classes_)}
print(integer_mapping)

dataset['LoyalClass'] = number.fit_transform(dataset['LoyalClass'].astype('str'))
integer_mapping = {l: i for i, l in enumerate(number.classes_)}
print(integer_mapping)

dataset.head()

# Step 5 Predictions
X_fresh = dataset.iloc[:, 1:10].values

import joblib
classifier = joblib.load('c2_Classifier_LoyalCustomers')

y_pred = classifier.predict(X_fresh)
print(y_pred)

predictions = classifier.predict_proba(X_fresh)
predictions

df_prediction_prob = pd.DataFrame(predictions, columns = ['prob_0', 'prob_1'])
dfx=pd.concat([dataset,df_prediction_prob], axis=1)
dfx.to_excel("d2_BuyProb_90Percent.xlsx")
dfx.head()

