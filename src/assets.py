from pathlib import Path
import pygame
from consts import TILE_SIZE

ASSETS_DIR=Path(__file__).parent.parent/"assets"
IMGS=ASSETS_DIR/"imgs"

assets={}

def extract_tile(tilesheet, col_off, row_off):
    return tilesheet.subsurface(col_off*TILE_SIZE, row_off*TILE_SIZE, TILE_SIZE, TILE_SIZE)

def load_assets():
    assets["sky"]=pygame.image.load(IMGS/"sky.png").convert()
    assets["clouds"]=pygame.image.load(IMGS/"clouds.png").convert_alpha()
    assets["tree"]=pygame.image.load(IMGS/"tree.png").convert_alpha()
    assets["grass"]=pygame.image.load(IMGS/"grass.png").convert()
    assets["sheep"]=pygame.image.load(IMGS/"sheep.png").convert_alpha()
    pipe_tilesheet=pygame.image.load(IMGS/"logs.png")
    assets["pipe_body_tile"]=extract_tile(pipe_tilesheet,0,0)
    assets["pipe_cap_tile"]=extract_tile(pipe_tilesheet,1,0)

def get_asset(name):
    return assets[name]
