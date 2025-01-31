# Spotifun
Project tracking user spotify stats

## Dependencies
spotipy - handles auth and spotify api requests
flask - webserver interface and session storage of token
pandas, numpy - handle managing and visualizing data

## App flow
1. User is asked to register or login
2. When register direct to login
3. When login succeeds the user is asked to login to spotify
4. User is sesnt to homepage containing information (playlists etc)