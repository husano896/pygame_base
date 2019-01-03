@echo off
echo build with -w option to remove console window!
pyinstaller --onefile main.py --hidden-import pygame as pg_sdl2.mixer_music --hidden-import pygame as pg_sdl2.mask --hidden-import pygame as pg_sdl2.render