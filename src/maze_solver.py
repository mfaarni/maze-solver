class WallFollower():

        def find_start(self, maze):
                y=0
                for row in maze:
                        x=0
                        for block in row:
                                if block == "S":
                                        return (x, y)
                                x+=1
                        y+=1


        def block_type(self, maze, x, y):
                return maze[y][x]

        def left(self, maze, start_x, start_y):
                if self.block_type(maze, start_x-1, start_y)=="G" or self.block_type(maze, start_x-1, start_y)==" ":
                        print("vasen", start_x-1, start_y, self.block_type(maze, start_x-1, start_y))
                        return True
                else:
                        return False
        
        def right(self, maze, start_x, start_y):
                if self.block_type(maze, start_x+1, start_y)=="G" or self.block_type(maze, start_x+1, start_y)==" ":
                        print("oikea", start_x+1, start_y, self.block_type(maze, start_x+1, start_y))
                        return True
                else:
                        return False
        
        
        def up(self, maze, start_x, start_y):
                if self.block_type(maze, start_x, start_y-1)=="G" or self.block_type(maze, start_x, start_y-1)==" ":
                        print("ylös", start_x, start_y-1, self.block_type(maze, start_x, start_y-1))
                        return True
                else:
                        return False
                
        def down(self, maze, start_x, start_y):
                if start_y<len(maze)-1: 
                        if self.block_type(maze, start_x, start_y+1)=="G" or self.block_type(maze, start_x, start_y+1)==" ":
                                print("alas", start_x, start_y+1, self.block_type(maze, start_x, start_y+1))
                                return True
                else:
                        return False
                

        def wall_follower(self, maze, start_x, start_y, facing, visited):
                if self.block_type(maze, start_x, start_y)=="G":
                        return
                
                if facing==0:
                        if self.left(maze, start_x, start_y):
                                visited.append([start_x-1,start_y])
                                self.wall_follower(maze,start_x-1,start_y, 1, visited)

                        elif self.up(maze, start_x, start_y):
                                visited.append([start_x,start_y-1])
                                self.wall_follower(maze,start_x,start_y-1, 0, visited)
                                

                        elif self.right(maze, start_x, start_y):
                                visited.append([start_x+1,start_y])
                                self.wall_follower(maze,start_x+1,start_y, 2, visited)
                                
                        elif self.down(maze, start_x, start_y):
                                visited.append([start_x,start_y+1])
                                self.wall_follower(maze,start_x,start_y+1, 3, visited)
                        else:
                                return

                elif facing==1:      

                        if self.down(maze, start_x, start_y):
                                visited.append([start_x,start_y+1])
                                self.wall_follower(maze,start_x,start_y+1, 3, visited)
                                           
                        elif self.left(maze, start_x, start_y):
                                visited.append([start_x-1,start_y])
                                self.wall_follower(maze,start_x-1,start_y, 1, visited)

                        elif self.up(maze, start_x, start_y):
                                visited.append([start_x,start_y-1])
                                self.wall_follower(maze,start_x,start_y-1, 0, visited)
                                

                        elif self.right(maze, start_x, start_y):
                                visited.append([start_x+1,start_y])
                                self.wall_follower(maze,start_x+1,start_y, 2, visited)
                        else:
                                return
                elif facing==2:
                        if self.up(maze, start_x, start_y):
                                visited.append([start_x,start_y-1])
                                self.wall_follower(maze,start_x,start_y-1, 0, visited)

                        elif self.right(maze, start_x, start_y):
                                visited.append([start_x+1,start_y])
                                self.wall_follower(maze,start_x+1,start_y, 2, visited)
                
                        elif self.down(maze, start_x, start_y):
                                visited.append([start_x,start_y+1])
                                self.wall_follower(maze,start_x,start_y+1, 3, visited)

                        elif self.left(maze, start_x, start_y):
                                visited.append([start_x-1,start_y])
                                self.wall_follower(maze,start_x-1,start_y, 1, visited)
                                
                elif facing==3:

                        if self.right(maze, start_x, start_y):
                                visited.append([start_x+1,start_y])
                                self.wall_follower(maze,start_x+1,start_y, 2, visited)
                
                        elif self.down(maze, start_x, start_y):
                                visited.append([start_x,start_y+1])
                                self.wall_follower(maze,start_x,start_y+1, 3, visited)

                        elif self.left(maze, start_x, start_y):
                                visited.append([start_x-1,start_y])
                                self.wall_follower(maze,start_x-1,start_y, 1, visited)
                        
                        elif self.up(maze, start_x, start_y):
                                visited.append([start_x,start_y-1])
                                self.wall_follower(maze,start_x,start_y-1, 0, visited)

        def draw_maze(self, maze, visited):
                maze_print=maze.copy()
                move=0
                draw_visited=[]

                for i in visited:
                        if i in draw_visited:
                                maze_print[i[1]]=maze_print[i[1]][:i[0]]+"!"+maze_print[i[1]][i[0]+1:]
                        else:     
                                maze_print[i[1]]=maze_print[i[1]][:i[0]]+"*"+maze_print[i[1]][i[0]+1:]
                                draw_visited.append(i)
                        move+=1
                return maze_print
