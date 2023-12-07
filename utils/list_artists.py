def list_artists(array):
    artist_string = ''
    i = 0
    for artist in array:
        if(i == 1):
            artist_string = artist_string.rstrip(', ')
            artist_string += ' ft. '

        artist_string += artist['name'] + ', '
        i += 1
    artist_string = artist_string.rstrip(', ')
    return artist_string



# artists = [
#           {
#             "external_urls": {
#               "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
#             },
#             "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
#             "id": "4q3ewBCX7sLwd24euuV69X",
#             "name": "Bad Bunny",
#             "type": "artist",
#             "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
#           }
          # {
          #   "external_urls": {
          #     "spotify": "https://open.spotify.com/artist/4SsVbpTthjScTS7U2hmr1X"
          #   },
          #   "href": "https://api.spotify.com/v1/artists/4SsVbpTthjScTS7U2hmr1X",
          #   "id": "4SsVbpTthjScTS7U2hmr1X",
          #   "name": "Arcángel",
          #   "type": "artist",
          #   "uri": "spotify:artist:4SsVbpTthjScTS7U2hmr1X"
          # },
          # {
          #   "external_urls": {
          #     "spotify": "https://open.spotify.com/artist/3EiLUeyEcA6fbRPSHkG5kb"
          #   },
          #   "href": "https://api.spotify.com/v1/artists/3EiLUeyEcA6fbRPSHkG5kb",
          #   "id": "3EiLUeyEcA6fbRPSHkG5kb",
          #   "name": "De La Ghetto",
          #   "type": "artist",
          #   "uri": "spotify:artist:3EiLUeyEcA6fbRPSHkG5kb"
          # },
          # {
          #   "external_urls": {
          #     "spotify": "https://open.spotify.com/artist/12vb80Km0Ew53ABfJOepVz"
          #   },
          #   "href": "https://api.spotify.com/v1/artists/12vb80Km0Ew53ABfJOepVz",
          #   "id": "12vb80Km0Ew53ABfJOepVz",
          #   "name": "Ñengo Flow",
          #   "type": "artist",
          #   "uri": "spotify:artist:12vb80Km0Ew53ABfJOepVz"
          # }
        # ]

# list_artist(artists)