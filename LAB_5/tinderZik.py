import spotipy
import requests
import os
import sys
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=auth_manager)

urn = 'spotify:artist:687cZJR45JO7jhk1LHIbgq'
urn2 = 'KE5ybnbzL6ErCNAudYZhf?si=c8360fffd8e440d3'

artist: dict = sp.artist(urn)

user = sp.user('dekilech')
#
print(f"Name :{artist['name']}",f"Popularity : {artist['popularity']}",f"Followers: {artist['followers']['total']}",
      f"Genres:{artist['genres']}",sep='\n')

name = input("Artist:")
def get_artist(name):
    resultat = sp.search(q='artist:'+name,type=artist)
    print(resultat)

get_artist('tupac')

print(user)

# https://open.spotify.com/user/dekilech?si=9a4743c82b274fcf
