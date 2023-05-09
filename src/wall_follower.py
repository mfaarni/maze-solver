import copy


class WallFollower():

    def __init__(self, maze):
        self.facing = 0
        self.maze = maze
        self.mazes = []
        self.start_cords = self.find_start_and_end(self.maze)
        self.visited = [[self.start_cords[0][1], self.start_cords[0][0]]]

    def find_start_and_end(self, maze):
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 'S':
                    start = (i, j)
                elif maze[i][j] == 'G':
                    end = (i, j)
        try:
            return (start, end)
        except:
            return "Alkua tai loppua ei löytynyt."

    def block_type(self, maze, x, y):
        return maze[y][x]

    def left(self, start_x, start_y):
        return self.block_type(self.maze, start_x-1, start_y) == "G" \
                or self.block_type(self.maze, start_x-1, start_y) == " "

    def right(self, start_x, start_y):
        return self.block_type(self.maze, start_x+1, start_y) == "G" \
                or self.block_type(self.maze, start_x+1, start_y) == " "

    def up(self, start_x, start_y):
        return self.block_type(self.maze, start_x, start_y-1) == "G" \
                or self.block_type(self.maze, start_x, start_y-1) == " "

    def down(self, start_x, start_y):
        if start_y < len(self.maze)-1:
            return self.block_type(self.maze, start_x, start_y+1) == "G" \
                or self.block_type(self.maze, start_x, start_y+1) == " " 
        return False

    def wall_follower(self, maze, start_x, start_y, facing):
        self.facing = facing
        if self.block_type(maze, start_x, start_y) == "G":
            return

        if self.facing == 0:
            if self.left(start_x, start_y):
                self.visited.append([start_x-1, start_y])
                self.wall_follower(maze, start_x-1, start_y, 1)

            elif self.up(start_x, start_y):
                self.visited.append([start_x, start_y-1])
                self.wall_follower(maze, start_x, start_y-1, 0)

            elif self.right(start_x, start_y):
                self.visited.append([start_x+1, start_y])
                self.wall_follower(maze, start_x+1, start_y, 2)

            elif self.down(start_x, start_y):
                self.visited.append([start_x, start_y+1])
                self.wall_follower(maze, start_x, start_y+1, 3)
            else:
                return

        elif self.facing == 1:

            if self.down(start_x, start_y):
                self.visited.append([start_x, start_y+1])
                self.wall_follower(maze, start_x, start_y+1, 3)

            elif self.left(start_x, start_y):
                self.visited.append([start_x-1, start_y])
                self.wall_follower(maze, start_x-1, start_y, 1)

            elif self.up(start_x, start_y):
                self.visited.append([start_x, start_y-1])
                self.wall_follower(maze, start_x, start_y-1, 0)

            elif self.right(start_x, start_y):
                self.visited.append([start_x+1, start_y])
                self.wall_follower(maze, start_x+1, start_y, 2)
            else:
                return
        elif self.facing == 2:
            if self.up(start_x, start_y):
                self.visited.append([start_x, start_y-1])
                self.wall_follower(maze, start_x, start_y-1, 0)

            elif self.right(start_x, start_y):
                self.visited.append([start_x+1, start_y])
                self.wall_follower(maze, start_x+1, start_y, 2)

            elif self.down(start_x, start_y):
                self.visited.append([start_x, start_y+1])
                self.wall_follower(maze, start_x, start_y+1, 3)

            elif self.left(start_x, start_y):
                self.visited.append([start_x-1, start_y])
                self.wall_follower(maze, start_x-1, start_y, 1)

        elif self.facing == 3:

            if self.right(start_x, start_y):
                self.visited.append([start_x+1, start_y])
                self.wall_follower(maze, start_x+1, start_y, 2)

            elif self.down(start_x, start_y):
                self.visited.append([start_x, start_y+1])
                self.wall_follower(maze, start_x, start_y+1, 3)

            elif self.left(start_x, start_y):
                self.visited.append([start_x-1, start_y])
                self.wall_follower(maze, start_x-1, start_y, 1)

            elif self.up(start_x, start_y):
                self.visited.append([start_x, start_y-1])
                self.wall_follower(maze, start_x, start_y-1, 0)

    def draw_maze(self):
        self.mazes=[]
        maze_print = self.maze.copy()
        draw_visited = []
        last=self.visited[0]

        for i in self.visited:
            if i not in self.visited[0] and self.visited[len(self.visited)-1]:
                maze_print[i[1]] = maze_print[i[1]][:i[0]] + \
                    "O"+maze_print[i[1]][i[0]+1:]
                    
                if last in draw_visited:
                    maze_print[last[1]] = maze_print[last[1]][:last[0]] + \
                        "!"+maze_print[last[1]][last[0]+1:]
                else:
                    maze_print[last[1]] = maze_print[last[1]][:last[0]] + \
                        "*"+maze_print[last[1]][last[0]+1:]
                draw_visited.append(last)
                last=i
                app=copy.copy(maze_print)
                self.mazes.append(app)
        print("")
        print("Wall Followerin löytämä reitti, pituus:", len(self.visited))
        for row in maze_print:
            for col in range(len(row)-1):
                if row[col]in "!*":
                        print("\033[91m{}\033[00m".format(row[col]), end= "")
                else:
                        print("\033[93m{}\033[00m".format(row[col]), end= "")
            print(row[len(row)-1])
        return self.visited
