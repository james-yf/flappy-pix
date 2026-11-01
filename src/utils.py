from consts import TILE_SIZE
import pygame
def extract_tile(tilesheet, col_off, row_off):
    return tilesheet.subsurface(col_off*TILE_SIZE, row_off*TILE_SIZE, TILE_SIZE, TILE_SIZE)
