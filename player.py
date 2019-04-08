import serial
import subprocess
import time

serial = serial.Serial('/dev/ttyACM0')

class Player: 
    def __init__(self, currentAlbum, playing, process):
        self.currentAlbum = currentAlbum
        self.playing = playing
        self.process = process

    def play(self, tag):
        if self.playing == True and tag == self.currentAlbum:
            if not (self.process is None):  
                print("Stopping player...")
                self.process.kill()
                self.playing = False
                self.currentAlbum = ""
        else:
            print("Starting player...")
            self.process = subprocess.Popen(["tizonia", "--spotify-album-id", albums.get(tag)])
            self.playing = True
            self.currentAlbum = tag

player = Player("", False, None)

albums = {
    "143 122 166 137 218": "6DEjYFkNZh67HP7R9PSZvv", # Reptation by Taylor Swift
    "241 161 49 45 76": "2QJmrSgbdM35R67eoGQo4j",    # 1989 by Taylor Swift
    "1 109 143 46 205": "6sUzNE1SPNLBXBCZs3PIAO",    # thank u, next by Ariana Grande
    "241 134 198 45 156": "6EVYTRG1drKdO8OnIQBeEj",  # Me Everything by Ariana Grande
    "241 117 60 45 149": "5MQBzs5YlZlE28mD9yUItn",   # Prism by Katy Perry
    "67 187 202 46 28": "0UlbGi4oAth8s6rwaGSU8Z",    # Witness by Katy Perry
}

while True:
    tag = serial.readline().rstrip()
    
    if tag in albums:
        player.play(tag)

if not (process is None):
    process.kill()

serial.close()
