import sys
sys.path.insert(0,'./System')
sys.path.insert(0,'./Scene')

import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

from Game_System import *
from pygame.locals import *
from Scene.Intro import Scene_Intro

#Game name
GAMENAME = "Hello pygame"

startup_Scene = Scene_Intro()
frame = 0

#Add support for console if needed (experiment)
import Game_Console
import Game_Debug

def showFPS():
    global FPSCLOCK, frame

    if (SDL2):
        ##Old Font
        img_FPS = pygame.pgSys.Font.render("%.2f (%d)" % (FPSCLOCK.get_fps(), frame) , 1, (255,255,255))
    else:
        ##Freetype
        img_FPS = pygame.pgSys.Font.render("%.2f (%d)" % (FPSCLOCK.get_fps(), frame) , (255,255,255))[0]
    if (pygame.pgSys.RenderEnabled):
        pygame.render.Sprite(pygame.pgSys.Renderer.load_texture(img_FPS)).render((0,0))
    else:
        pygame.pgSys.Screen.blit(img_FPS,(0,0))

    frame+=1
    pygame.display.set_caption("%s %.2f" % (GAMENAME, FPSCLOCK.get_fps()))

def main():
    global FPSCLOCK, sleeping
    FPSCLOCK = pygame.time.Clock()
    cur_x, cur_y = 0, 0

    pygame.pgSys.ChangeScene(startup_Scene)
    sleeping = False
    
    while True:
        #Exit event is handled in main process
        exitEvent = pygame.event.get(pygame.QUIT)
        if (len(exitEvent) > 0):
            pygame.quit()
            exit()
            break

        if (pygame.pgSys.Handle_Events_InMain):
            for event in pygame.event.get():
                #Mouse event example
                if event.type in (MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP):
                    cur_x, cur_y = event.pos
                    
                ####Support in pygame_sdl2
                elif (SDL2):
                    #Android back key.
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_AC_BACK:
                        break
                    #App is going to background, any screen updates will terminate the app.
                    elif event.type == pygame.APP_WILLENTERBACKGROUND:
                        sleeping = True
                    #App is awake from background, reinit the display
                    elif event.type == pygame.APP_DIDENTERFOREGROUND:
                        sleeping = False
                        pygame.pgSys.InitDisplay()

        if (not sleeping):
            if (pygame.pgSys.RenderEnabled):
                pygame.pgSys.Renderer.clear(pygame.pgSys.BGColor)
            else:
                pygame.pgSys.Screen.fill(pygame.pgSys.BGColor)

            if (pygame.pgSys.Scene):
                pygame.pgSys.Scene.update()
                pygame.pgSys.Scene.graphicsUpdate()

            #Only for debug
            showFPS()
            Game_Debug.showDebugInfo()
            
            if (pygame.pgSys.RenderEnabled):
                pygame.pgSys.Renderer.render_present()
            else:
                pygame.display.flip()

        FPSCLOCK.tick(FPS)
        
if __name__ == '__main__':
    main()
