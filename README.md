## Spotify Playlist Reorderer
**By Eric Xu**

A tool supporting the shuffling, unscrambling, and reversal of songs in a spotify playlist while maintaining the "date added" property for each song.

A short overview on how to use the code, my rationale behind the project, and final learnings.

## Features
- Shuffle a playlist while preserving date-added order
- Restore a playlist back to its original order while preserving date-added order
- Reverse playlist order

## Set Up

I used the official spotify documentation for developers and made a local web app using [link](https://developer.spotify.com/dashboard/create). 
I simply named my app and used "http://127.0.0.1:8888/callback" for the redirect URI, while leaving everything else blank. This creates a local app,
with its own unique client id and client secret. These can be accessed through the spotify dashboard. Copy and pasting your unique client id and client secret 
as well as the redirect uri into ".env.example" should allow the code to run without issues, although I
have not tested it yet. More detailed instructions can be found [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started).

*Note the program runs even if you can not see the songs moving in the spotify app. It moves the songs in the spotify database, which takes time to update on your app.

## How to Run
1. **Install dependencies**
   
Make sure you have Python 3.10+ installed, then run: 
```bash
pip install spotipy python-dotenv python-dateutil
```
2. **Set up your Spotify credentials**

Create or use the .env file in the project directory and add:
Set up your Spotify credentials

SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback


You can find these values in your Spotify Developer Dashboard under your app settings from [Set Up](#set-up).

3. **Run Main.Py and Follow the Prompts**
## Rationale and Project Inspiration

I was initial inspired by this [spotify shuffler](https://stevenaleong.com/tools/spotifyplaylistrandomizer) I found online, as I found myself feeling similarly
towards spotify's shuffle, but after using their shuffler on one of my main playlists, I felt like it looked kind of bad with all the dates mixed up. As they provided
no way to unscramble your playlist, I decided to try and figure out a way to revert my playlist to how it was before.

## Learning Outcomes and Closing Remarks
This was my first unguided coding project, so it was interesting implementing theory I learned in my computer science classes like mergesort and api calls into something 
actually useful and practical. Throughout this project, I struggled a lot with the correctness of my code, as I would be using the spotify application to see if it was working. The problem was that
spotify application stops showing updates in real time after a few iterations of song shuffling, but I did not know that, which made me question the correctness of my code, as well as if my api calls were being
limited. I would eventually find out that the playlist would update even without the playlist being updated visually, but I wasted a lot of time debugging correct code.

## Requirements
- Python 3.10+
- spotipy
- python-dotenv
- python-dateutil

## Changelog

### v1.0.0 (2025-11-18)

- First completed implementation

