import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import config
import pandas as pd
import time




def spotipy_object(CLIENT_ID, CLIENT_SECRET):
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return sp

def get_artists(sp, artist):
    track_results = sp.search(q=f'artist:{artist}', type='artist', limit=1)

    print(track_results)

def get_tracks(sp, artist):

    offset = 0
    ls = []
    track_id = []
    track_name = []
    artist_id = []
    artist_name = [] 
    explicit = []
    popularity = []
    release_date = []
    followers = []
    artist_genres = []

    while offset<1000:
        
        track_results = sp.search(q=f'artist:{artist}', type='track', limit=50,offset=offset)

        for i, track in enumerate(track_results['tracks']['items']):

            try: 
                if track['artists'][0]['name']==artist:

                    track_id.append(track['id'])
                    track_name.append(track['name'])
                    artist_id.append(track['artists'][0]['id'])
                    artist_name.append(track['artists'][0]['name'])
                    explicit.append(track['explicit'])
                    release_date.append(track['album']['release_date'])
                    popularity.append(track['popularity'])
                    #followers.append(track['artists'][1]['followers']['total'])
                    #artist_genres.append(track['artists'][2]['genres'])
                  
                    ls.append(track['name'])
            except Exception as e:
                print(e)
                

        offset+=50

    print(f'{artist}: {len(ls)}')
    df = pd.DataFrame()
    df['track_id'] = track_id
    df['track_name'] = track_name 
    df['artist_id'] = artist_id
    df['artist_name'] = artist_name
    df['explicit'] = explicit
    df['release_date'] = release_date
    df['popularity'] = popularity

    return df      

def get_artist_genres(sp, artist_id):
    artist = sp.artist(artist_id)
    return artist['genres']

if __name__=='__main__':

    # cred 1
    # CLIENT_ID = 'bd412b0f40e24288914386672042fe42'
    # CLIENT_SECRET = '72595f60913742b78785ca3743f3ff3a'

    # cred 2
    #CLIENT_ID = '68848a39b8b84c8aaaea32f36e224a3c'
    #CLIENT_SECRET = 'e117936c575a45ebae3744edfe477ca5'

    # cred 3
    CLIENT_ID = config.CLIENT_ID
    CLIENT_SECRET = config.CLIENT_SECRET

    print('Start')

    

    sp = spotipy_object(CLIENT_ID=CLIENT_ID, CLIENT_SECRET=CLIENT_SECRET)

    artists = pd.read_excel('artists.xlsx')
    artists = list(artists['artist'])

    
    df = pd.DataFrame()
    for i, artist in enumerate(artists):
        df_artist = get_tracks(sp=sp, artist=artist)
        if i==0:        
            df = df_artist
        else:
            df = pd.concat([df, df_artist])
        time.sleep(2)

    '''
    df_audio_features = pd.DataFrame()
    df_audio_features['track_id'] = df['track_id']
    df_audio_features['audio'] = df_audio_features['track_id'].apply(lambda x: get_audio_features(sp=sp, track_id=x))

    split = pd.DataFrame(df_audio_features['audio'].to_list(), 
    columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'dusration_ms', 'time_signature'])
    print(split.head())
    '''
        
    print('Phase 1 done!')

    df.to_excel('Data/tracks.xlsx', index=False)
    #df_audio_features.to_excel('Data/audio_data.xlsx', index=False)
    #time.sleep(30)


    features = sp.audio_features('1bDbXMyjaUIooNwFE9wn0N')
    print("features:", features[0].keys())
    