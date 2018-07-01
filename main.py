#User inputs song and artist, use spotify to reccomend a number of songs
#From that list, use mood to narrow down
#Recommend list based off of both Spotify and mood

from spotify import *
from emotion import *

print("Please enter in the name of a song")
song = input()
print("Please enter in the name of the artist")
artist = input()

analyzer = Emotion()
emotion = analyzer.get_emotion(song, artist)
print(emotion)
sentiment = analyzer.get_sentiment(song, artist)
print(sentiment)

spotify = Spotify()
track = spotify.find_song(song, artist)
recommendations = spotify.get_recommendations(track)
for index, name in enumerate(recommendations):
	track_data = recommendations[index]
	track_name = track_data['name']
	artist_name = track_data['artists'][0]['name']
	print(track_name + " by " + artist_name)