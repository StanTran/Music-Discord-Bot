#User inputs song and artist, use spotify to reccomend a number of songs
#From that list, use mood to narrow down
#Recommend list based off of both Spotify and mood

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions, EmotionOptions
import json
from PyLyrics import *
import matplotlib.pyplot as plt
import numpy as np
import warnings

import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

client_credentials_manager = SpotifyClientCredentials(client_id='***REMOVED***', client_secret='***REMOVED***')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

warnings.filterwarnings('ignore')
natural_language_understanding = NaturalLanguageUnderstandingV1(version = '2017-02-27', username = "***REMOVED***", password = "***REMOVED***")
print("Please enter in the name of an artist")
user_artist = input()
print("Please enter in the name of their song")
user_song = input()

response = natural_language_understanding.analyze(text=PyLyrics.getLyrics(user_artist, user_song), features=Features(emotion=EmotionOptions(), sentiment = SentimentOptions()))
print(response.get('emotion').get('document').get('emotion'))
sentiment = response.get('sentiment').get('document').get('score')
print(sentiment)

results = spotify.search(q=user_song, type = 'track')
items = results['tracks']['items']
for index, tracks in enumerate(items):
    track = items[index]
    artist = track['artists'][0]['name']
    if artist == user_artist:
    	print(artist)
    	break

recommendations = spotify.recommendations(seed_tracks = [track['id']], seed_artists = [track['artists'][0]['id']])
tracks_of_recommend = recommendations['tracks']
for index, name in enumerate(tracks_of_recommend):
	track_data = tracks_of_recommend[index]
	track_name = track_data['name']
	artist_name = track_data['artists'][0]['name']
	print(track_name + " by " + artist_name)
