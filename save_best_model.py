import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.compose import ColumnTransformer
import warnings
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt 
import joblib

warnings.filterwarnings(action='ignore')


# load data

df = pd.read_excel('Data/Processed Data/model_data.xlsx')

predictors = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'time_signature', 'followers', 'is_pop_or_rap', 'months_since_release', 'duration_s']
target = 'popularity'

# create input and output data
X = df[predictors]
y = df[target]

# create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)



# transform training and testing data
ct_ohe = ColumnTransformer(transformers=[('one hot encode', OneHotEncoder(handle_unknown='ignore'), ['key'])], remainder='passthrough')
transform = Pipeline(steps=[('one hot encode', ct_ohe),
                        ('scaler', StandardScaler())])

X_train_shap = transform.fit_transform(X_train)
X_test_shap = transform.transform(X_test)


# fit random forest regressor
model = RandomForestRegressor(max_depth=30, min_samples_leaf=3, min_samples_split=5, n_estimators=700, n_jobs=1, random_state=42)
model.fit(X_train_shap, y_train)

# save model and pipeline object for future use 
joblib.dump(model, 'Models/random_forest_regressor.pkl', compress=9)
joblib.dump(transform, 'Models/preprocessing.pkl')

print('Done')