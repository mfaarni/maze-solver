from mazes import maze

maze_test = maze()
maze_draw = maze_test

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



start=find_start(maze_test)
suunta=0
#  0
#1   2
#  3
moves=0

print(start)

visited=[[start[1],start[0]]]
def wall_follower(maze, start_x, start_y, suunta, moves):

    if block_type(maze, start_x, start_y)=="G":
        print(moves)
        return
    
    if suunta==0:
        
        if block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
            if [start_x-1, start_y] != visited[len(visited)-1]:
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                moves+=1
                wall_follower(maze,start_x-1,start_y, 1, moves)

        elif block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
            if [start_x, start_y-1] != visited[len(visited)-1]:
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1])    
                moves+=1
                wall_follower(maze,start_x,start_y-1, 0, moves)
                

        elif block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
            if [start_x+1, start_y] != visited[len(visited)-1]:
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y])  
                moves+=1         
                wall_follower(maze,start_x+1,start_y, 2, moves)
                
        elif block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
            if [start_x, start_y+1] != visited[len(visited)-1]:
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1]) 
                moves+=1        
                wall_follower(maze,start_x,start_y+1, 3, moves)

    elif suunta==1:
        
        if block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
            if [start_x, start_y+1] != visited[len(visited)-1]:
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1])   
                moves+=1        
                wall_follower(maze,start_x,start_y+1, 3, moves)

        elif block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
            if [start_x-1, start_y] != visited[len(visited)-1]:
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                moves+=1
                wall_follower(maze,start_x-1,start_y, 1, moves)

        elif block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
            if [start_x, start_y-1] != visited[len(visited)-1]:
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1])    
                moves+=1
                wall_follower(maze,start_x,start_y-1, 0, moves)
                

        elif block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
            if [start_x+1, start_y] != visited[len(visited)-1]:
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y]) 
                moves+=1         
                wall_follower(maze,start_x+1,start_y, 2, moves)
                
    elif suunta==2:
        
        if block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
            if [start_x, start_y-1] != visited[len(visited)-1]:
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1]) 
                moves+=1   
                wall_follower(maze,start_x,start_y-1, 0, moves)
                

        elif block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
            if [start_x+1, start_y] != visited[len(visited)-1]:
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y])      
                moves+=1         
                wall_follower(maze,start_x+1,start_y, 2, moves)

        elif block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
            if [start_x, start_y+1] != visited[len(visited)-1]:
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1]) 
                moves+=1         
                wall_follower(maze,start_x,start_y+1, 3, moves)

        elif block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
            if [start_x-1, start_y] != visited[len(visited)-1]:
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                moves+=1
                wall_follower(maze,start_x-1,start_y, 1, moves)

                
    elif suunta==3:

        if block_type(maze, start_x+1, start_y)=="G" or block_type(maze, start_x+1, start_y)==" ":
            if [start_x+1, start_y] != visited[len(visited)-1]:
                print("oikea", start_x+1, start_y, block_type(maze, start_x+1, start_y))
                visited.append([start_x+1,start_y])    
                moves+=1           
                wall_follower(maze,start_x+1,start_y, 2, moves)

        elif block_type(maze, start_x, start_y+1)=="G" or block_type(maze, start_x, start_y+1)==" ":
            if [start_x, start_y+1] != visited[len(visited)-1]:
                print("alas", start_x, start_y+1, block_type(maze, start_x, start_y+1))
                visited.append([start_x,start_y+1]) 
                moves+=1          
                wall_follower(maze,start_x,start_y+1, 3, moves)

        elif block_type(maze, start_x-1, start_y)=="G" or block_type(maze, start_x-1, start_y)==" ":
            if [start_x-1, start_y] != visited[len(visited)-1]:
                print("vasen", start_x-1, start_y, block_type(maze, start_x-1, start_y))
                visited.append([start_x-1,start_y])
                moves+=1
                wall_follower(maze,start_x-1,start_y, 1, moves)
        
        elif block_type(maze, start_x, start_y-1)=="G" or block_type(maze, start_x, start_y-1)==" ":
            if [start_x, start_y-1] != visited[len(visited)-1]:
                print("ylös", start_x, start_y-1, block_type(maze, start_x, start_y-1))
                visited.append([start_x,start_y-1])   
                moves+=1    
                wall_follower(maze,start_x,start_y-1, 0, moves)
                


                







#print("1,0:", block_type(maze_test,1,0))
#print("1,1:", block_type(maze_test,1,1))

print(wall_follower(maze_test,find_start(maze_test)[0],find_start(maze_test)[1], suunta, moves))