import copy
import sys
sys.setrecursionlimit(5000)

# Luokka toteuttaa Tremauxin ratkaisualgoritmin.
# Luokka alustetaan ascii-muotoisella labyrintilla, sekä aloitus- ja loppupisteellä.

class Tremaux:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.mazes = []
        self.visualize_visited = []
        self.start = start
        self.end = end
        self.prints = 0

# Ratkaisualgoritmi, jossa alustetaan taulukko visited, joka pitää yllä vierailtuja solmuja.
# Tämän avulla voidaan tarkistaa käytävien merkinnät, joita Tremauxin algoritmi hyödyntää.
# Alustetaan myös path, johon tallennetaan algoritmin löytämä reitti.

    def solve(self):
        self.visualize_visited = []
        visited = [[0] * len(self.maze[0]) for i in range(len(self.maze))]
        path = []
        # Aloitetaan ensimmäisestä kohdasta.
        x, y = self.start
        visited[x][y] = 1
        self.visualize_visited.append((x, y))
        path.append((x, y))

        # Toisteteaan kunnes löydetään ulkoskäynti labyrintistä.
        while (x, y) != self.end:
            unmarked_entrances = self.get_unmarked_entrances(x, y, visited)
            if len(unmarked_entrances) == 0:
                x, y = path.pop()
            elif len(unmarked_entrances) == 1:
                if (x, y) not in path:
                    path.append((x, y))
                dx, dy = unmarked_entrances[0]
                visited[x + dx][y + dy] += 1
                self.visualize_visited.append((x + dx, y + dy))
                x, y = x + dx, y + dy
                path.append((x, y))
            else:
                if (x, y) not in path:
                    path.append((x, y))
                dx, dy = self.choose_direction(
                    x, y, unmarked_entrances, visited)
                visited[x + dx][y + dy] += 1
                self.visualize_visited.append((x + dx, y + dy))
                x, y = x + dx, y + dy
                path.append((x, y))
        return path

    # Etsii tietyn kohdan ympäröimät merkkaamattomat sisäänkäynnit.

    def get_unmarked_entrances(self, x, y, visited):
        entrances = []
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if self.is_valid(x + dx, y + dy) and visited[x + dx][y + dy] == 0:
                entrances.append((dx, dy))
        return entrances

    # Valitsee suunnan, johon algoritmi kulkee
    def choose_direction(self, x, y, entrances, visited):
        min_marks = 100000
        next_x, next_y = x, y
        for dx, dy in entrances:
            count = self.count_marks(x, y, dx, dy, visited)
            if count < min_marks:
                min_marks = count
                next_x, next_y = x + dx, y + dy
        return next_x - x, next_y - y

    # Laskee ympärillä olevien ruutujen merkintöjen määrät.
    def count_marks(self, x, y, dx, dy, visited):
        count = 0
        if self.is_valid(x + dx, y + dy) and visited[x + dx][y + dy] == 1:
            count += 1
        if self.is_valid(x - dx, y - dy) and visited[x - dx][y - dy] == 1:
            count += 1
        return count

    # Tarkistaa, ovatko koordinaatit labyrintin sisällä ja sisältävätkö ne seiniä.
    def is_valid(self, x, y):
        return 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0]) and self.maze[x][y] not in "1234567890#"


    # Tulostaa komentoriville labyrintin ja löydetyn reitin.
    def print_path(self, path):
        if path:
            for i in range(len(self.maze)):
                row = ""
                for j in range(len(self.maze[i])):
                    if (i, j) in path:
                        row += "X"
                    else:
                        row += self.maze[i][j]
                for col in range(len(row)-1):
                    if row[col] in "!*X":
                        print("\033[91m{}\033[00m".format(row[col]), end="")
                    else:
                        print("\033[93m{}\033[00m".format(row[col]), end="")
                print(row[len(row)-1])
        else:
            print("Reittiä ei löytynyt.")
        print("")
        return path
    
    # Visualisoi labyrinttia luomalla jokaisesta siirrosta uuden ascii-labyrintin.
    # Pygame käy nämä läpi ja muodostaa niistä animoidun labyrintin ratkaisun.

    def visualize(self, path):
        maze_print = self.maze.copy()
        mazes = []
        last = self.visualize_visited[0]
        for i in self.visualize_visited:
            if i not in self.visualize_visited[0] and self.visualize_visited[len(self.visualize_visited)-1]:
                maze_print[i[0]] = maze_print[i[0]][:i[1]] + \
                    "O"+maze_print[i[0]][i[1]+1:]
                if last in path:
                    maze_print[last[0]] = maze_print[last[0]][:last[1]] + \
                        "X"+maze_print[last[0]][last[1]+1:]
                else:
                    maze_print[last[0]] = maze_print[last[0]][:last[1]] + \
                        "!"+maze_print[last[0]][last[1]+1:]
                last = i
                app = copy.copy(maze_print)
                mazes.append(app)
        return mazes
