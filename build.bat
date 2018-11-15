@echo off
echo build with -w option to remove console window!
pyinstaller --onefile main.py --hidden-import pygame_sdl2.mixer_music --hidden-import pygame_sdl2.mask --hidden-import pygame_sdl2.render