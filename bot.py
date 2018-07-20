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

        original_emotion = None
        while original_emotion is None:
            await client.send_message(message.channel, 'Enter in the name of a song')
            response = await client.wait_for_message(timeout=30.0, author=message.author)
            song = response.content
            index = set([0])
            for counter, x in enumerate(song):
                if x == ' ':
                    index.add(counter + 1)
            song = "".join(c.upper() if x in index else c for x, c in enumerate(song))
            await client.send_message(message.channel, 'Enter in the name of the artist')
            response = await client.wait_for_message(timeout=30.0, author=message.author)
            artist = response.content
            for counter, x in enumerate(artist):
                if x == ' ':
                    index.add(counter + 1)
            artist = "".join(c.upper() if x in index else c for x, c in enumerate(artist))
            await client.send_message(message.channel, 'Enter a genre if possible, if not, enter \'none\'')
            response = await client.wait_for_message(timeout=30.0, author=message.author)
            genre = response.content
            for counter, x in enumerate(artist):
                if x == ' ':
                    index.add(counter + 1)
            genre = "".join(c.lower() if x in index else c for x, c in enumerate(artist))
            
            analyzer = Emotion()
            try:
                original_emotion = analyzer.get_emotion(song, artist)
                print(original_emotion)
            except:
                await client.send_message(message.channel, 'Song does not exist in the library')
                pass
        
        spotify = Spotify()
        track = spotify.find_song(song, artist)
        list_genres = spotify.get_genres()
        if genre not in list_genres['genres']:
            genre = None
        recommendations = spotify.get_recommendations(track, genre, limit = 10)
        rec_emotion = dict()
        for index, name in enumerate(recommendations):
            track_data = recommendations[index]
            track_name = track_data['name']
            artist_name = track_data['artists'][0]['name']
            print(track_name + " by " + artist_name)
            if track_name == song and artist_name == artist:
                continue
            try: 
                emotion = analyzer.get_emotion(track_name, artist_name)
                rec_emotion[track_name + " by " + artist_name] = emotion
            except:
                pass
        for key, value in rec_emotion.items():
            error = abs(original_emotion['sadness'] - value['sadness']) + abs(original_emotion['joy'] - value['joy']) + abs(original_emotion['fear'] - value['fear']) + abs(original_emotion['disgust'] - value['disgust']) + abs(original_emotion['anger'] - value['anger'])
            rec_emotion[key] = error
        rec_emotion = sorted(rec_emotion.items(), key = lambda v: v[1])
        await client.send_message(message.channel, 'Recommendations for \'' + song + ' by ' + artist + '\':')
        await client.send_message(message.channel, '{}, {}, {}, {}, {}'.format(rec_emotion[0][0], rec_emotion[1][0], rec_emotion[2][0], rec_emotion[3][0], rec_emotion[4][0]))

client.run('TOKEN')
