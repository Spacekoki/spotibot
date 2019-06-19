import spotibot

spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + name, type='artist')
print(results)
