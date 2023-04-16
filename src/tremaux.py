
# Luokka toteuttaa Tremauxin ratkaisualgoritmin. 
# Luokka alustetaan ascii-muotoisella labyrintilla, sekä aloitus- ja loppupisteellä.

class Tremaux:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end

# Ratkaisualgoritmi, jossa alustetaan taulukko visited, joka pitää yllä vierailtuja solmuja. 
# Tämän avulla voidaan tarkistaa käytävien merkinnät, joita Tremauxin algoritmi hyödyntää.
# Alustetaan myös path, johon tallennetaan algoritmin löytämä reitti.

    def solve(self):
        visited = [[0] * len(self.maze[0]) for i in range(len(self.maze))]
        path = []
        # Aloitetaan ensimmäisestä kohdasta.
        x, y = self.start
        visited[x][y] = 1
        path.append((x, y))

        # Toisteteaan kunnes löydetään ulkoskäynti labyrintistä.
        while (x, y) != self.end:
            unmarked_entrances = self.get_unmarked_entrances(x, y, visited)
            if len(unmarked_entrances) == 0:
                x, y = path.pop()
            elif len(unmarked_entrances) == 1:
                dx, dy = unmarked_entrances[0]
                visited[x + dx][y + dy] += 1
                x, y = x + dx, y + dy
                path.append((x, y))
            else:
                dx, dy = self.choose_direction(x, y, unmarked_entrances, visited)
                visited[x + dx][y + dy] += 1
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

    def count_marks(self, x, y, dx, dy, visited):
        count = 0
        if self.is_valid(x + dx, y + dy) and visited[x + dx][y + dy] == 1:
            count += 1
        if self.is_valid(x - dx, y - dy) and visited[x - dx][y - dy] == 1:
            count += 1
        return count

    def is_valid(self, x, y):
        return 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0]) and self.maze[x][y] != "#"

    def print_path(self, path):
        if path:
            for i in range(len(self.maze)):
                row = ""
                for j in range(len(self.maze[i])):
                    if (i, j) in path:
                        row += "X"
                    else:
                        row += self.maze[i][j]
                print(row)
        else:
            print("Reittiä ei löytynyt.")
        print("")
        print("Reitin kaikki kohdat:")
        print(path)
        print("")

