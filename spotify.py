import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify:

	def __init__(self):
		client_credentials_manager = SpotifyClientCredentials(client_id='***REMOVED***', client_secret='***REMOVED***')
		self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	def find_song(self, song, artist):
		results = self.spotify.search(q=song, type = 'track')
		items = results['tracks']['items']
		for index, tracks in enumerate(items):
			track = items[index]
			current_artist = track['artists'][0]['name']
			if current_artist == artist:
				return track

	def get_recommendations(self, track, genre, limit):
		recommendations = self.spotify.recommendations(seed_tracks = [track['id']], seed_artists = [track['artists'][0]['id']], seed_genres = genre, limit = limit)
		tracks_of_recommend = recommendations['tracks']
		return tracks_of_recommend

	def get_genres(self):
		genres = self.spotify.recommendation_genre_seeds()
		return genres