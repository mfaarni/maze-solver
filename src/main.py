import pygame
from ui.grid import draw
from mazes import maze_gen
from maze_solver import WallFollower
if __name__=="__main__":

    wf = WallFollower()
    maze = maze_gen(0)
    start=wf.find_start(maze)
    print(start)
    facing=0
    """ 
        kertoo suunnan, johon algoritmi "katsoo", noudattaa seuraavaa järjestystä:y
        ylös = 0
        vasen = 1
        oikea = 2
        alas = 3
    """
    visited=[[start[0],start[1]]]
    wf.wall_follower(maze,start[0],start[1], facing, visited)
    maze_print = wf.draw_maze(maze, visited)
    size=900
    window = pygame.display.set_mode((size,size))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        draw(window, maze_print, size, visited)
