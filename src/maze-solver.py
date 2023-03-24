import pygame
from mazes import maze_gen

maze = maze_gen(1)

def find_start(maze):
    y=0
    for row in maze:
        x=0
        for block in row:
            if block == "S":
                return (x, y)
            x+=1
        y+=1
    print("ei ollu")



def block_type(maze, x, y):
    return maze[y][x]



start=find_start(maze)
suunta=0
#  0
#1   2
#  3
print("aloitusruutu:", start)

visited=[[start[0],start[1]]]
def wall_follower(maze, start_x, start_y, suunta):

    if block_type(maze, start_x, start_y)=="G":
        return
    
    if suunta==0:
        
        if block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                wall_follower(maze,start_x-1,start_y, 1)

        elif block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1])
                wall_follower(maze,start_x,start_y-1, 0)
                

        elif block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y])
                wall_follower(maze,start_x+1,start_y, 2)
                
        elif start_y<len(maze)-1: 
            if block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1])
                wall_follower(maze,start_x,start_y+1, 3)

    elif suunta==1:
        
        if block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1])
                wall_follower(maze,start_x,start_y+1, 3)

        elif block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                wall_follower(maze,start_x-1,start_y, 1)

        elif block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1])
                wall_follower(maze,start_x,start_y-1, 0)
                

        elif block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y])
                wall_follower(maze,start_x+1,start_y, 2)
                
    elif suunta==2:
        
        if block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1])
                wall_follower(maze,start_x,start_y-1, 0)
                

        elif block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y])
                wall_follower(maze,start_x+1,start_y, 2)

        elif block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1])
                wall_follower(maze,start_x,start_y+1, 3)

        elif block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                wall_follower(maze,start_x-1,start_y, 1)

                
    elif suunta==3:

        if block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y])
                wall_follower(maze,start_x+1,start_y, 2)

        elif block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1]) 
                wall_follower(maze,start_x,start_y+1, 3)

        elif block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                wall_follower(maze,start_x-1,start_y, 1)
        
        elif block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1])
                wall_follower(maze,start_x,start_y-1, 0)
                
#print("1,0:", block_type(maze,1,0))
#print("1,1:", block_type(maze,1,1))

def grid(window, maze, size):
    for row in range(len(maze)):
        for block in range (len(maze[row])-2):
            if maze[row][block]=="X":
                pygame.draw.rect(window,(0,0,0), (-50+(block+1)*50,-50+(row+1)*50,40+(block+1)*50,40+(row+1)*50))
            elif maze[row][block]=="*":
                pygame.draw.rect(window,(160,0,150), (-50+(block+1)*50,-50+(row+1)*50,40+(block+1)*50,40+(row+1)*50))
            elif maze[row][block]==" ":
                pygame.draw.rect(window,(255,255,255), (-50+(block+1)*50,-50+(row+1)*50,40+(block+1)*50,40+(row+1)*50))
            else:
                pygame.draw.rect(window,(0,255,255), (-50+(block+1)*50,-50+(row+1)*50,40+(block+1)*50,40+(row+1)*50))
                  

def draw(window, maze, size):
    window.fill((255,255,255))
    grid(window, maze, size)
    pygame.display.update()

if __name__=="__main__":
    print(wall_follower(maze,find_start(maze)[0],find_start(maze)[1], suunta))
    maze_print=maze
    move=0
    for i in visited:
        print(i)
        maze_print[i[1]]=maze_print[i[1]][:i[0]]+"*"+maze_print[i[1]][i[0]+1:]
        move+=1
        #print(len(maze_print))
    for row in maze_print:
        print(row)
    print("siirtoja:", move-1)
    size=len(maze*50)
    window = pygame.display.set_mode((size,size))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        draw(window, maze, size)
