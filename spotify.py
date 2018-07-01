import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
#import pprint

class Spotify:

	def __init__(self):
		client_credentials_manager = SpotifyClientCredentials(client_id='ID_HERE', client_secret='SECRET_ID_HERE')
		self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	def find_song(self, song, artist):
		results = self.spotify.search(q=song, type = 'track')
		items = results['tracks']['items']
		for index, tracks in enumerate(items):
			track = items[index]
			current_artist = track['artists'][0]['name']
			if current_artist == artist:
				return track

	def get_recommendations(self, track):
		recommendations = self.spotify.recommendations(seed_tracks = [track['id']], seed_artists = [track['artists'][0]['id']])
		tracks_of_recommend = recommendations['tracks']
		return tracks_of_recommend
