import pygame
import time
from pygame.locals import *
pygame.init()

def grid(window, maze, size, isMenu):
    block_size_y = (size/len(maze))
    block_size_x = (size/len(maze[0]))
    if isMenu:
        colours=[
        (41, 163, 82),
        (21, 100, 60),
        (205, 215, 72),
        (245, 245, 102),
        (76, 185, 100)
        ]
    else:
        colours=[
        (41, 163, 82),
        (21, 100, 60),
        (205, 215, 72),
        (245, 245, 102),
        (141, 255, 182)
        ]
    for row in range(len(maze)):
        y = -block_size_y+(row+1)*(size/len(maze))
        for block in range(len(maze[row])):
            x = -block_size_x+(block+1)*(size/len(maze))
            if maze[row][block] in "#2134567890-":
                pygame.draw.rect(window, colours[0],
                                 (x, y, x+block_size_x, y+block_size_y))
            elif maze[row][block] == "O":
                pygame.draw.rect(window, colours[1],
                                 (x, y, x+block_size_x, y+block_size_y))
            elif maze[row][block] == "!":
                pygame.draw.rect(window, colours[2],
                                 (x, y, x+block_size_x, y+block_size_y))
            elif maze[row][block] in "*X":
                pygame.draw.rect(window, colours[3],
                                 (x, y, x+block_size_x, y+block_size_y))
            else:
                pygame.draw.rect(window, colours[4],
                                 (x, y, x+block_size_x, y+block_size_y))


def draw(window, mazes, size, visited, pygame):
    running=True
    window.fill((41, 163, 82))
    for maze in mazes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False
                    return False
        if running: 
            grid(window, maze, size, False)
            if len(visited)<500:
                time.sleep(2/len(visited))
            pygame.display.update()
    return True