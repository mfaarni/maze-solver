def find_start(maze):
    y=0
    for row in maze:
        x=0
        for block in row:
            if block == "S":
                return (x, y)
            x+=1
        y+=1


def block_type(maze, x, y):
    return maze[y][x]



def wall_follower(maze, start_x, start_y, facing, visited):

    if block_type(maze, start_x, start_y)=="G":
        return
    
    if facing==0:
        
        if block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                wall_follower(maze,start_x-1,start_y, 1, visited)

        elif block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1])
                wall_follower(maze,start_x,start_y-1, 0, visited)
                

        elif block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y])
                wall_follower(maze,start_x+1,start_y, 2, visited)
                
        elif start_y<len(maze)-1: 
            if block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1])
                wall_follower(maze,start_x,start_y+1, 3, visited)

    elif facing==1:
        
        if block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1])
                wall_follower(maze,start_x,start_y+1, 3, visited)

        elif block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                wall_follower(maze,start_x-1,start_y, 1, visited)

        elif block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1])
                wall_follower(maze,start_x,start_y-1, 0, visited)
                

        elif block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y])
                wall_follower(maze,start_x+1,start_y, 2, visited)
                
    elif facing==2:
        
        if block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1])
                wall_follower(maze,start_x,start_y-1, 0, visited)
                

        elif block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y])
                wall_follower(maze,start_x+1,start_y, 2, visited)

        elif block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1])
                wall_follower(maze,start_x,start_y+1, 3, visited)

        elif block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                wall_follower(maze,start_x-1,start_y, 1, visited)

                
    elif facing==3:

        if block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y])
                wall_follower(maze,start_x+1,start_y, 2, visited)

        elif block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1]) 
                wall_follower(maze,start_x,start_y+1, 3, visited)

        elif block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                wall_follower(maze,start_x-1,start_y, 1, visited)
        
        elif block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1])
                wall_follower(maze,start_x,start_y-1, 0, visited)


def draw_maze(maze, visited):
    maze_print=maze.copy()
    move=0
    draw_visited=[]
    #print("siirtoja:", move-1)

    for i in visited:
        if i in draw_visited:
            maze_print[i[1]]=maze_print[i[1]][:i[0]]+"!"+maze_print[i[1]][i[0]+1:]
        else:     
            maze_print[i[1]]=maze_print[i[1]][:i[0]]+"*"+maze_print[i[1]][i[0]+1:]
            draw_visited.append(i)
            #print("!",draw_visited)
        move+=1
    return maze_print
