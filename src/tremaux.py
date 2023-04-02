class Tremaux():

    def __init__(self, maze):
        self.facing = 0
        self.mazes = []
        self.last = None
        self.maze = maze
        self.moves=0
    def find_start(self):
        y = 0
        for row in self.maze:
            x = 0
            for block in row:
                if block == "S":
                    return (x, y)
                x += 1
            y += 1

    def block_type(self, x, y):
        return self.maze[y][x]

    def is_junction(self, cords):
        x=cords[0]
        y=cords[1]
        x_check=False
        y_check=False
        if self.maze[y-1][x] in " OX"  or self.maze[y+1][x] in " OX":
            x_check=True
        if self.maze[y][x-1] in " OX" or self.maze[y][x+1] in " OX":
            y_check=True
        
        if x_check and y_check:
            return True
        if y<len((self.maze))-2 and x<len(self.maze[x]):
            if self.dead_end(cords):
                return True
            
    def mark(self, cords):
        x=cords[0]
        y=cords[1]
        if self.maze[y][x]!="X" and self.maze[y][x]!="O":
            self.maze[y] = self.maze[y][:x]+"X"+self.maze[y][x+1:]
        else:
            self.maze[y] = self.maze[y][:x]+"O"+self.maze[y][x+1:]

    
    def marked(self, cords):
        x=cords[0]
        y=cords[1]
        return self.maze[y][x]

    def least_marks(self, cords):
        x=cords[0]
        y=cords[1]
        least = None
        ways = [self.maze[y][x-1],self.maze[y][x+1],self.maze[y-1][x],self.maze[y+1][x]]
        for way in ways:
            if way == " ":
                least = way
            elif way == "O" and least == None:
                least = way
            elif way == "X" and least == None:
                least = way
        return least
    
    def reverse(self, facing):
        if facing==0:
            return 3
        if facing==1:
            return 2
        if facing==2:
            return 1
        if facing==3:
            return 0
    
    def random_way(self, cords):
        x=cords[0]
        y=cords[1]
        if self.maze[y-1][x] == " ":
            return 0

        if self.maze[y+1][x] == " ":
            return 3
        
        if self.maze[y][x+1] == " ":
            return 2

        if self.maze[y][x-1] == " ":
            return 1
    def only_entrance_marked(self, cords):
        x=cords[0]
        y=cords[1]
        x_check=True
        y_check=True
        if self.maze[y-1][x] in "OX"  or self.maze[y+1][x] in "OX":
            y_check=False
            print("ycheck false")
        if self.maze[y][x-1] in "OX" or self.maze[y][x+1] in "OX":
            x_check=False
            print("xcheck false")
        if x_check or y_check:
            print("vaan tulosuunnassa merkattu")
            return True

    def dead_end(self, cords):
        x=cords[0]
        y=cords[1]
        counter=0
        if self.maze[y-1][x] in "#":
            counter+=1
        if self.maze[y+1][x] in "#":
            counter+=1
        if self.maze[y][x-1] in "#":
            counter+=1
        if self.maze[y][x+1] in "#":
            counter+=1
        if counter>=3:
            return True
    def tremaux(self, x, y, facing, visited):
        self.moves+=1
        if self.moves>300:
            return
        for row in self.maze:
            print(row)
        print("nyt:", x,y)
        visited.append([x,y])
        self.facing=facing
        if self.block_type(x, y)=="G":
            print("voitit")
            return
        
        #merkkaa nykyisen jos edellinen oli junction
        if len(visited)>2:
            self.last = [visited[len(visited)-2][0],visited[len(visited)-2][1]]
            print("viimesin: "+str(self.last))
            if self.is_junction(self.last):
                "merkataan ku oltiin junktionissa"
                self.mark([x,y])

            #merkkaa edellisen jos tullaan junctioniin
        if self.is_junction([x, y]):
            print("junktiossa")
            self.mark(self.last)
        
            
                # if only entrance where came from is marked,
                # pick unmarked entrance, if any.
            if self.only_entrance_marked([x,y]) and self.random_way([x,y]) != None:
                facing=self.random_way([x,y])
                print("nyt random suuntaan", facing)
            

                # elif entrance where came from is not double marked,
                # go back
            elif self.marked(self.last)!=2 or self.dead_end([x,y]):
                print("käännös")
                facing=self.reverse(facing)

                # else:
                # pick any entrance with te fewest marks
            else:
                print("pienin paha")
                facing = self.least_marks([x,y])


                # self.tremaux(self, maze, x, y-1, self.facing, visited)
        if facing==0:
            print("mennää yl")
            self.tremaux(x, y-1, facing, visited)
        elif facing==1:
            print("mennää vas")
            self.tremaux(x-1, y, facing, visited)
        elif facing==2:
            print("mennää oik")
            self.tremaux(x+1, y, facing, visited)
        elif facing==3:
            print("mennää al")
            self.tremaux(x, y+1, facing, visited)

    def draw_maze(self, visited, mazes):
        maze_print = self.maze.copy()
        move = 0
        draw_visited = []

        for i in visited:
            if i in draw_visited:
                maze_print[i[1]] = maze_print[i[1]][:i[0]] + \
                    "!"+maze_print[i[1]][i[0]+1:]
            else:
                maze_print[i[1]] = maze_print[i[1]][:i[0]] + \
                    "*"+maze_print[i[1]][i[0]+1:]
                draw_visited.append(i)
            move += 1
        mazes.append(maze_print)
        return
