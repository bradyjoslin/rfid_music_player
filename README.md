# RFID Music Player
Raspberry Pi music box project created with my daughter over a few weekends as a way to keep her interested in STEM.  Have a set of RFID cards that represent specific albums.  Tapping the card on the corner of our entertainment console triggers that album to play through our stereo. 

<img src="https://github.com/bradyjoslin/rfid_music_player/raw/master/cards.png" height="250">

The hardware is an RFID reader wired to an Arduino Uno connected via USB to a Raspberry Pi 3 B+ whose audio output goes into the stereo.  The Arduino broadcasts the RFID card's serial number over USB which a python service on the pi listens on.  If the message matches a s/n in a dictionary, get the associated Spotify album id, then trigger that song to play using an open source service called [Tizonia](http://tizonia.org/).  If you scan the same album that's already playing, stop the music.  

The sample source code that came with the RFID reader on the Arduino ended up working fine for doing the s/n broadcast.  So, the only code I had to write was the python service for the Pi that listens on the USB port and plays music, which ended up being less than 50 lines of code.  

There are a number of other projects like this out there, here are some other similar projects which served as inspiration. 

http://www.brendandawes.com/projects/plasticplayer

https://www.theverge.com/circuitbreaker/2019/1/1/18163939/diy-jukebox-magstripe-swipeable-cards-chris-patty

https://www.youtube.com/watch?v=AvCseOQidSw&app=desktop
