
# Identifying Drivers of Spotify Tracks' Popularity With Causal ML


![Spotify](https://image.cnbcfm.com/api/v1/image/107009054-1643658568841-gettyimages-1236974580-ODOGMAN_005.jpeg?v=1668111049&w=740&h=416&ffmt=webp&vtcrop=y)

What makes a song tick? If you've browsed through any artist's album on Spotify, you've probably noticed that some songs are considerably more successful than others. 

These artists perform multiple tracks with the same voice, style, and genre. So, why do these songs differ so much in terms of popularity? Are there "hidden" factors that influences a listener's decision to like or not like a song?. To answer these questions, we turn to causal machine learning. By training an ML model to predict song popularity, we can run simulations and identify features that drive sogn popularity.

The goal of this project is to build a streamlit app that uses a machine learning model to predict how popular a Spotify song wil be based on certain features. 

## Learn More About This Project On Medium
For a step-by-step breakdown on how the project was conducted, check out the following article: https://towardsdatascience.com/identifying-drivers-of-spotify-song-popularity-with-causal-ml-934e8347d2aa#b34e

## Author
Aashish Nair  
LinkedIn: www.linkedin.com/in/aashish-nair  
Medium: https://medium.com/@aashishnair

## Web App Deployment Instructions
To run the streamlit app on your own device, do the following:  
1. Pull the files from this repository into your machine with this command. 
```
git clone https://github.com/anair123/Identifying_Drivers_Of_Song_Popularity_With_Causal_ML.git
```

2. Install all of these packages (preferably in a virtual environment):   

```
pip install pandas
pip install -U scikit-learn
pip install openpyxl  
pip install streamlit
```  
3. Load the machine learning model and preprocessing pipeline by running the "save_best_model.py" file. 
```python save_best_model.py```   

4. Run the streamlit app by running te following command.  
```streamlit run app.py```

## Tech Stack
Data collection: Requests  
Data analysis: Pandas, Numpy, Matplotlib, Seaborn  
Data modeling: Scikit Learn  
Model deployment: Streamlit




