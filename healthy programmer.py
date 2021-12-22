#___________________________Healthy Programmer__________________________________
"""
9 am - 5 pm
water - water. mp3(3.5 litres)- drank - log
eyes - eyes.mp3 - every 30 min - eye done - log
physical activity - physucal.mp3 - 45 min - exdone - log
pygame module to play mp3
"""
from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.load()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open ("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}")
if __name__ == '__main__':

    musicloop("water.mp3", "stop")
    init_water = time()