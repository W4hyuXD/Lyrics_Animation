#! usr/bin/env python3

from time import sleep
import time, sys, os

def print_lyrics():
    lines = [
        ("My heart belongs to you", 0.1),
        ("I'll take a piece of you", 0.1),
        ("My heart belongs to you", 0.1),
        ("I'll take a piece of you", 0.2),
    ]

    delays = [8.5,8.5,8.2,2]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print("")

os.popen("play-audio apieceofyou.mp3");time.sleep(13);print_lyrics()
