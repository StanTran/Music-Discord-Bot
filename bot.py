import discord
from spotify import *
from emotion import *

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == '!stop': await client.logout()

    if message.content.startswith('!rec'):
        await client.send_message(message.channel, 'Enter the name of a song')
        response = await client.wait_for_message(timeout=30.0, author=message.author)
        song = response.content
        await client.send_message(message.channel, 'You entered: {}'.format(song))
        await client.send_message(message.channel, 'Now enter the name of the artist')
        response = await client.wait_for_message(timeout=30.0, author=message.author)
        artist = response.content
        await client.send_message(message.channel, 'You entered: {}'.format(artist))
        await client.send_message(message.channel, 'Song: {}, Artist: {}'.format(song, artist))
        
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


client.run('***REMOVED***')