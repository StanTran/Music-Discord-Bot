# Bothoven
A Discord bot that uses a combination of Spotify API and Natural Language Processing to retrieve a list of song recommendations based off of emotion. Based off of the initial song a user inputted, the bot begins retrieving recommendations using Spotify API. Each song's lyrics are then analyzed and compared with the initial song. The emotions being compared are sadness, joy, fear, disgust, and anger. The bot then returns the five most similar songs based off of the emotion.

## Getting Started
Follow the instructions to get Bothoven working in your very own Discord server!

### Prerequisites
In order to use Bothoven, you will need the following:
```
Discord
Discord account with Manage Server permission
```

### Setting Up Bothoven
Go into your preferred web browser and enter this link:
```
https://discordapp.com/oauth2/authorize?client_id=463529880940707850&scope=bot
```
Then choose the server you want to add Bothoven to from the dropdown menu and click 'Authorize'.
Bothoven should now be in the server and ready to be used.

## Using Bothoven
Now that Bothoven is all set up, all users have to do is invoke the bot and begin inputting songs
To receive instructions for the bot
```
!help
```
To invoke the bot
```
!rec
```
To input the song after invoking the bot
```
$song $artist $genre
Note: Genre is optional
```

## Built With
* [Discord API](https://discordpy.readthedocs.io/en/latest/index.html) - Interface that was used
* [Spotipy](https://spotipy.readthedocs.io/en/latest/) - Spotify API used to retrieve song data
* [IBM Watson](https://www.ibm.com/watson/) - Used for Natural Language Understanding

## Authors
* **Stanley Tran** - [stanltran](https://github.com/stanltran/Bothoven)
