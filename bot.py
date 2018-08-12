
#FIX INDEX OUT OF BOUNDS AT END

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

    if message.content == '!help':
        await client.send_message(message.channel, 'Invoke the bot with the command \'!rec\'')
        await client.send_message(message.channel, 'Then enter a song, artist, and genre in the following format:')
        await client.send_message(message.channel, '$song $artist $genre  (genre is optional)')

    if message.content.startswith('!rec'):

        original_emotion = None
        while original_emotion is None:
            response = None
            while response is None: 
                await client.send_message(message.channel, 'Enter a song, artist, and genre')
                response = await client.wait_for_message(timeout=30.0, author=message.author)
                response = response.content
                if '$' not in response:
                    await client.send_message(message.channel, 'Invalid format. Please try again.')
                    response = None
                else:
                    response = response.split('$')
                    if len(response) < 3 or len(response) > 4:
                        await client.send_message(message.channel, 'Invalid format. Please try again.')
                        response = None
                    else:
                        for index, items in enumerate(response):
                            if index == 0:
                                continue
                            elif index == 1:
                                song = items.strip()
                            elif index == 2:
                                artist = items.strip()
                            else:
                                genre = items.strip()

            index = set([0])
            for counter, x in enumerate(song):
                if x == ' ':
                    index.add(counter + 1)
            song = "".join(c.upper() if x in index else c for x, c in enumerate(song))

            index = set([0])
            for counter, x in enumerate(artist):
                if x == ' ':
                    index.add(counter + 1)
            artist = "".join(c.upper() if x in index else c for x, c in enumerate(artist))

            genre = None
            if len(response) == 4:
                index = set([0])
                for counter, x in enumerate(genre):
                    if x == ' ':
                        index.add(counter + 1)
                genre = "".join(c.lower() if x in index else c for x, c in enumerate(genre))
            

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
        recommendations = spotify.get_recommendations(track, genre, limit = 15)
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

client.run('***REMOVED***')