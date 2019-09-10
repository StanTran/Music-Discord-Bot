# Bothoven
A Discord bot that has the user input a song and returns a list of recommendations based off of the song's emotion. Bothoven analyzes the lyrics of the song to capture a song's emotion and then outputs a list of songs that are similar in emotion.

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
* **Stanley Tran** - [Stantl3r](https://github.com/stanltran/Bothoven)
