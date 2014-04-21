import sys
import mpd
import time

cli = mpd.MPDClient()
cli.connect("192.168.1.40", 6600)
#cli.connect("192.168.1.85", 6601)

import random

artists = sorted(sys.argv[1:] or cli.list("artist"))
start = random.randint(0, len(artists))
start = 0
count = 10
artists = artists[start:start+count]
len_artists = float(len(artists))
print "%d artists from %s" % (len_artists, start)
for i, artist in enumerate(artists):
#  print "%0.2f%% %s" % (i/len_artists*100., artist)
  try:
    albums = cli.list("album", "artist", artist)
  except:
    print "error with artist", artist
    continue

#  print "%d albums for %s" % (len(albums), artist)
  if not list(albums):
    print "0 albums", artist

  # Mpdroid phone version
  for album in sorted(albums):
    #print album
    try:
      cli.find("artist", artist, "album", album)
      cli.list("album", artist)
      cli.count("artist", artist, "album", album)
    except:
      print "Error with", album
      continue

