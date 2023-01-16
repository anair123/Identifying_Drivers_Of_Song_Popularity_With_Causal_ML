import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer



# import pipeline object and model
preprocessing = joblib.load('Models/preprocessing.pkl')
rf_model = joblib.load('Models/random_forest_regressor.pkl')
input_features = pd.DataFrame(columns=['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence',
       'time_signature', 'followers', 'is_pop_or_rap', 'months_since_release',
       'duration_s'])

input_features.loc[0] =[1 for _ in range(15)]

input_features_processed = preprocessing.transform(input_features)


prediction = rf_model.predict(input_features_processed)

print(prediction)