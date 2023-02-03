import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from PIL import Image



@st.cache(allow_output_mutation=True)
def load_pipeline_and_model():
    """load the pipeline object for preprocessing and the ml model"""

    preprocessing = joblib.load('Streamlit_objects/preprocessing.pkl')
    rf_model = joblib.load('Streamlit_objects/random_forest_regressor.pkl')
    return preprocessing, rf_model

def main():
    # load pipeline object and model
    preprocessing, rf_model = load_pipeline_and_model()

    # side bar and title
    st.sidebar.header('Track Features')
    st.header('Spotify Track Popularity Prediction App')

    # load image
    image = Image.open('Spotify.jpg')
    st.image('Spotify.jpg')

    # get feature values
    followers = st.sidebar.slider("Artist's Number of Followers", 0, 10000000, 1)
    genre = st.sidebar.selectbox('Genre', ('Pop', 'Rock', 'Rap', 'Country', 'EDM', 'Other'))
    months_since_release = st.sidebar.slider('Number of Months Since Relaase', 0, 36, 1)
    duration_s = st.sidebar.slider('Duration (s)', 0.0, 600.0, 0.01)
    danceability = st.sidebar.slider('Danceability', 0.0, 1.0, 0.01)
    energy = st.sidebar.slider('Energy', 0.0, 1.0, 0.01)
    key = st.sidebar.slider('Key', 0, 1, 11)
    loudness = st.sidebar.slider('Loudness', -20.0, 20.0, 0.1)
    mode = st.sidebar.slider('Mode', 0, 1, 1)
    speechiness = st.sidebar.slider('Speechiness', 0.0, 1.0, 0.01)
    acousticness = st.sidebar.slider('Acousticness', 0.0, 1.0, 0.01)
    instrumentalness = st.sidebar.slider('Instrumentalness', 0.0, 1.0, 0.01)
    liveness = st.sidebar.slider('Liveness', 0.0, 1.0, 0.01)
    valence = st.sidebar.slider('Valence', 0.0, 1.0, 0.01)
    time_signature = st.sidebar.slider('Time Signature', 0.0, 1.0, 0.01)

    # assign value to is_pop_or_rap feature
    if genre in ['Pop', 'Rap']:
        is_pop_or_rap = 1
    else:
        is_pop_or_rap = 0

    # create input matrix with user response
    input_features = pd.DataFrame(columns=['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
        'acousticness', 'instrumentalness', 'liveness', 'valence',
        'time_signature', 'followers', 'is_pop_or_rap', 'months_since_release',
        'duration_s'])
    input_features.loc[0] = [danceability, energy, key, loudness, mode, speechiness,
        acousticness, instrumentalness, liveness, valence,
        time_signature, followers, is_pop_or_rap, months_since_release,
        duration_s]

    # spotify documentation
    st.write(f'For a description of the audio features, visit the Spotify API documentation: https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features')

    # create button that generates prediction
    if st.button('Predict'):
        input_features_processed = preprocessing.transform(input_features)
        prediction = rf_model.predict(input_features_processed)[0]
        st.success(f'Popularity Score: {np.round(prediction, 2)}')

if __name__ == '__main__':
    main()