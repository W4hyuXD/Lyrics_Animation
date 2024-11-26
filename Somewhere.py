#! usr/bin/python3
# <!-- Copyright by WahyuXD -->
# Somewhere only we know+ Kaene

import sys
import time, os
from time import sleep

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_lyrics():
    lines = [
        ("And if you have a minute, why don't we go", 0.05),
        ("Talk about it somewhere only we know?", 0.05),
        ("This could be the end of everything", 0.05),
        ("So, why don't we go somewhere only we know?", 0.05)
    ]
    delays = [1, 1, 0.5, 2] # Delay Line

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end="")
            sys.stdout.flush()
            custom_sleep(0.09 if i in [0, 2, 3, 4] else 0.1) # Typing Speed
        custom_sleep(delays[i])
        print()

os.popen('play-audio somewhere.mp4');print_lyrics()

