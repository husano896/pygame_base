import sys
sys.path.insert(0,'./System')
sys.path.insert(0,'./Scene')

import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

from Game_System import *
from pygame.locals import *
from Scene.Title import Scene_Title

#Game name
GAMENAME = "Hello pygame"
cache_ImgDebugInfo = None
startup_Scene = Scene_Title()
frame = 0
def showFPS():
    global FPSCLOCK, frame
    
    img_FPS = pygame.pgSys.Font.render("%.2f (%d)" % (FPSCLOCK.get_fps(), frame) , 1, (255,255,255))
    if (pygame.pgSys.RenderEnabled):
        pygame.render.Sprite(pygame.pgSys.Renderer.load_texture(img_FPS)).render((0,0))
    else:
        pygame.pgSys.Screen.blit(img_FPS,(0,0))

    frame+=1
    pygame.display.set_caption("%s %.2f" % (GAMENAME, FPSCLOCK.get_fps()))

def showDebugInfo():
    global cache_ImgDebugInfo
    
    surf = pygame.Surface((400, 120), pygame.HWSURFACE | pygame.SRCALPHA)
    img1 = pygame.pgSys.Font.render("pygame version : %s" % pygame.version.ver, 1, (255,255,255))
    SDLVersion = pygame.get_sdl_version()
    img2 = pygame.pgSys.Font.render("SDL version : %d.%d.%d" % (SDLVersion[0], SDLVersion[1], SDLVersion[2]), 1, (255,255,255))
    img3 = pygame.pgSys.Font.render("RendererEnabled : %s" % (pygame.pgSys.RenderEnabled), 1, (255,255,255))
    surf.blit(img1, (surf.get_width() - img1.get_width(),0))
    surf.blit(img2, (surf.get_width() - img2.get_width(),img1.get_height()))
    surf.blit(img3, (surf.get_width() - img3.get_width(),img1.get_height()+img2.get_height()))
    if (cache_ImgDebugInfo == None):
        if (pygame.pgSys.RenderEnabled):
            cache_ImgDebugInfo = pygame.render.Sprite(pygame.pgSys.Renderer.load_texture(surf))
        else:
            cache_ImgDebugInfo = surf

    if (pygame.pgSys.RenderEnabled):
        cache_ImgDebugInfo.render((400,0))
    else:
        pygame.pgSys.Screen.blit(cache_ImgDebugInfo,(400,0))
        
def main():
    global FPSCLOCK
    FPSCLOCK = pygame.time.Clock()
    cur_x, cur_y = 0, 0

    pygame.pgSys.ChangeScene(startup_Scene)
    while True:
        #Exit event is handled in main process
        exitEvent = pygame.event.get(pygame.QUIT)
        if (len(exitEvent) > 0):
            pygame.quit()
            break

        if (pygame.pgSys.Handle_Events_InMain):
            for event in pygame.event.get():
                if event.type in (MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP):
                    cur_x, cur_y = event.pos
                        
        if (pygame.pgSys.RenderEnabled):
            pygame.pgSys.Renderer.clear(pygame.pgSys.BGColor)
        else:
            pygame.pgSys.Screen.fill(pygame.pgSys.BGColor)

        if (pygame.pgSys.Scene):
            pygame.pgSys.Scene.update()
            pygame.pgSys.Scene.graphicsUpdate()

        showFPS()
        showDebugInfo()
        
        if (pygame.pgSys.RenderEnabled):
            pygame.pgSys.Renderer.render_present()
        else:
            pygame.display.flip()

        FPSCLOCK.tick(FPS)
        
if __name__ == '__main__':
    main()
