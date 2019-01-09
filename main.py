import sys, os
sys.path.insert(0,'./System')
sys.path.insert(0,'./Scene')

os.environ['SDL_VIDEO_CENTERED'] = '1'

from Game_System import *
from Scene.Intro import Scene_Intro

startup_Scene = Scene_Intro()

if pg.get_sdl_version() < (2,0,0):
    print("This example requires SDL2 or above.")

video.messagebox("Info", "pygame ver:" + pg.version.ver + "\n" + "SDL ver:" + str(pg.get_sdl_version()), None, True)
def main():

    global FPSCLOCK
    FPSCLOCK = pg.time.Clock()

    try:
        pg.Sys.ChangeScene(startup_Scene)
        
        while True:
            pg.Sys.Update()
            for event in pg.Sys.Events:
                pass
            
            pg.Sys.Renderer.clear()

            if (pg.Sys.Scene):
                pg.Sys.Scene.update()
                pg.Sys.Scene.graphicsUpdate()

            pg.Sys.Renderer.present()
            
            FPSCLOCK.tick(FPS)
            
    except Exception as e:
        #Error handling
        pg.quit()
        raise(e)
    
if __name__ == '__main__':
    main()
