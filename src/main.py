import pygame
from ui.grid import draw
from mazes import maze_gen
from maze_solver import draw_maze, find_start, wall_follower
if __name__=="__main__":

    maze = maze_gen(1)
    start=find_start(maze)
    facing=0
    """ 
        kertoo suunnan, johon algoritmi "katsoo", noudattaa seuraavaa järjestystä:y
        ylös = 0
        vasen = 1
        oikea = 2
        alas = 3
    """
    visited=[[start[0],start[1]]]
    wall_follower(maze,start[0],start[1], facing, visited)
    maze_print = draw_maze(maze, visited)
    size=900
    window = pygame.display.set_mode((size,size))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        draw(window, maze_print, size)
