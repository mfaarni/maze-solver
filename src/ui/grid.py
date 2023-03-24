import pygame
pygame.init()
def grid(window, maze, size):
    for row in range(len(maze)):
        for block in range (len(maze[row])-2):
            block_size=(size/len(maze))
            x=-block_size+(block+1)*(size/len(maze))
            y=-block_size+(row+1)*(size/len(maze))
            if maze[row][block]=="#":
                pygame.draw.rect(window,(0,0,0), (x,y,x+block_size,y+block_size))
            elif maze[row][block]=="!":
                pygame.draw.rect(window,(100,0,100), (x,y,x+block_size,y+block_size))
            elif maze[row][block]=="*":
                pygame.draw.rect(window,(160,0,150), (x,y,x+block_size,y+block_size))
            elif maze[row][block]==" ":
                pygame.draw.rect(window,(255,255,255), (x,y,x+block_size,y+block_size))
            else:
                pygame.draw.rect(window,(0,255,255), (x,y,x+block_size,y+block_size))
                  

def draw(window, maze, size, visited):
    window.fill((255,255,255))
    grid(window, maze, size)
    myfont=pygame.font.SysFont('Corbel', 32)
    visited_text=myfont.render("Liikkeet: "+str(len(visited)-1),1,(200,200,0))
    window.blit(visited_text, (2,2))
    pygame.display.update()
