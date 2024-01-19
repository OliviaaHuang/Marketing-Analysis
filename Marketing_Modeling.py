# Step 1 Import Libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression

# Step 2 Import dataset
dataset=pd.read_excel("a1_Dataset_10Percent.xlsx")

dataset.shape

dataset.head()

# Step 3 Data Cleaning
dataset=dataset.drop(['ID'],axis=1)

dataset.head()

dataset.isna().sum()

dataset['DemAffl']=dataset['DemAffl'].fillna(dataset['DemAffl'].mode()[0])
dataset['DemAge']=dataset['DemAge'].fillna(dataset['DemAge'].mode()[0])
dataset['DemClusterGroup']=dataset['DemClusterGroup'].fillna(dataset['DemClusterGroup'].mode()[0])
dataset['DemGender']=dataset['DemGender'].fillna(dataset['DemGender'].mode()[0])
dataset['DemReg']=dataset['DemReg'].fillna(dataset['DemReg'].mode()[0])
dataset['DemTVReg']=dataset['DemTVReg'].fillna(dataset['DemTVReg'].mode()[0])
dataset['LoyalTime']=dataset['LoyalTime'].fillna(dataset['LoyalTime'].mean())

dataset.isna().sum()

dataset.head()

# Step 4 Machine learining
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

# Step 5 Checking for Multicollinearity
from statsmodels.stats.outliers_influence import variance_inflation_factor

def calc_vif(z):

    # Calculating VIF
    vif = pd.DataFrame()
    vif["variables"] = z.columns
    vif["VIF"] = [variance_inflation_factor(z.values, i) for i in range(z.shape[1])]

    return(vif)

z = dataset.iloc[:,0:9]
calc_vif(z)

# Step 6 Variable selection
y = dataset.iloc[:, 9].values
X = dataset.iloc[:, 0:9].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Step 7 Logistic regression model
classifier =  LogisticRegression(max_iter=200)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

import joblib
joblib.dump(classifier, './c2_Classifier_LoyalCustomers')

print(confusion_matrix(y_test,y_pred))

print(accuracy_score(y_test, y_pred))

predictions = classifier.predict_proba(X_test)
predictions

df_prediction_prob = pd.DataFrame(predictions, columns = ['prob_0', 'prob_1'])
df_test_dataset = pd.DataFrame(y_test,columns= ['Actual Outcome'])
df_x_test = pd.DataFrame(X_test)

dfx=pd.concat([df_x_test,df_test_dataset, df_prediction_prob], axis=1)

dfx.to_excel("c1_ModelOutput_10Percent.xlsx")

dfx.head()

