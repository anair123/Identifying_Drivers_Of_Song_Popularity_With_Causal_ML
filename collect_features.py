import collect_tracks
import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from concurrent.futures import ThreadPoolExecutor
import spotipy.util as util
import numpy as np
import pandas as pd
import time




def spotipy_object(CLIENT_ID, CLIENT_SECRET):
    """return the spotify object using the given client credentials"""

    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return sp

def get_audio_features(track_id):
    """obtain audio feature data for the given track"""
    try: 
        audio = sp.audio_features(track_id)[0]
        return audio
    except:
        return float('NaN')

def get_artist_info(artist_id):
    """obtain artist info for the given artist"""
    try:
        artist_info = sp.artist(artist_id)
        return artist_info
    except:
        return float('NaN')

def export_track_features(track_id, artist_id):
    try: 
        audio = sp.audio_features(track_id)[0]
        time.sleep(5)
    except:
        return float('NaN')
    



if __name__=='__main__':

    # cred 1
    #CLIENT_ID = 'bd412b0f40e24288914386672042fe42'
    #CLIENT_SECRET = '72595f60913742b78785ca3743f3ff3a'

    # cred 2
    #CLIENT_ID = '68848a39b8b84c8aaaea32f36e224a3c'
    #CLIENT_SECRET = 'e117936c575a45ebae3744edfe477ca5'

    # cred 3
    CLIENT_ID = config.CLIENT_ID
    CLIENT_SECRET = config.CLIENT_SECRET

    sp = spotipy_object(CLIENT_ID=CLIENT_ID, CLIENT_SECRET=CLIENT_SECRET)

    tracks = pd.read_excel('Data/tracks.xlsx', usecols=['track_id', 'artist_id'])
    artists = pd.read_excel('Data/artists.xlsx')
    artists = list(artists['artist'])
    print('Loaded datasets!')

    # get lists of tracks and artist for data collection
    track_ids = list(tracks['track_id'].unique())

    track_lists = [track_ids[i:i + 100] for i in range(0, len(track_ids), 100)]

    df_audio_features = pd.DataFrame()
    for track_list in track_lists:
        subset = pd.DataFrame()
        audio_features = sp.audio_features(track_list)
        subset['track_id'] = track_list
        subset['audio_features'] = audio_features

        df_audio_features = pd.concat([df_audio_features, subset])
        if len(df_audio_features)%100000 == 0:
            print(f'{len(df_audio_features)} records collected')

    print('Pulled audio feature data!')

    # collect information on each artist
    df_artist_info = pd.DataFrame()
    list_artist_info = []
    for artist in artists:
        result = sp.search(artist, limit=1, type="artist")
        artist_info = result["artists"]["items"][0]
        # Display genres associated with the first search result

        list_artist_info.append(artist_info)

    # store pulled information in to a data frame
    df_artist_info['artist'] = artists
    df_artist_info['artist_info'] = list_artist_info

    print('Pulled artist info data!')

    # export data frame to .xlsx file
    df_audio_features.to_excel('Data/audio_features.xlsx', index=False)
    df_artist_info.to_excel('Data/artist_info.xlsx', index=False)

    print('Exported data to .xlsx files!')

