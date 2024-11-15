#! usr/bin/python3
# Copyright © WahyuXD

import time, os, sys
from time import sleep
from rich import print


def lirik(lyrics, textl, dbaris):
    for i, baris in enumerate(lyrics):
        for char in baris:
            print(char, end='', flush=True)
            time.sleep(textl[i])
        print()
        time.sleep(dbaris[i])

# Lirik
lyrics = [
    "I need to","tell you",
    "something",
    "My heart just can't be faithful",
    "For long",
    "I swear","I only make you cry"
]

# delay
textl = [0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.2] # Delay Animasi Text
dbaris = [1.5, 1.2, 1, 1.3, 1, 1, 2] # Delay Buat Line/Baris Baru


if __name__=="__main__":
    try:
        os.system('clear')
        os.popen("play-audio Cry.mp3") # Pemanggilan Lagu 
    except:pass
    sleep(6.5);lirik(lyrics, textl, dbaris)

