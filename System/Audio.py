import pygame as pg

####https://www.pg.org/docs/ref/music.html

def init():
    result = True
    try:
        pg.mixer.pre_init(44100, 16, 2, 2048)
        pg.mixer.init()
    except Exception as e:
        result = False
        print(e)
    try:
        pg.mixer.quit()
        pg.mixer.init(44100, 16, 2, 2048)
    except Exception as e:
        result = False
        print(e)

    if (result):
        print("Successfully initalized mixer.")

def loadBGM(filename):
    if (not pg.mixer.get_init()):
        return

    pg.mixer.music.load(filename)
    
def playBGM(filename, loops=-1, pos=0.0, event=None):
    
    if (not pg.mixer.get_init()):
        return

    pg.mixer.music.load("Audio/BGM/%s" % filename)
        
    pg.mixer.music.play(loops, pos)

    if (event != None):
        pg.mixer.music.set_endevent(event)

def stopBGM():
    pg.mixer.music.stop()
    pg.mixer.music.set_endevent()

def fadeoutBGM(t):
    pg.mixer.music.fadeout(t)

class Sound(pg.mixer.Sound):

    def __init__(self, n):
        if (pg.mixer.get_init()):
            super().__init__("Audio/SE/%s" % n)
        
    def play(self, loops=0, maxtime=0, fade_ms=0):
        if (pg.mixer.get_init()):
            super().play(loops, maxtime, fade_ms)

    def stop(self):
        if (pg.mixer.get_init()):
            super().stop()
