import unittest
from wall_follower import WallFollower
from mazes import maze_gen


class TestWallFollower(unittest.TestCase):
    def setUp(self):
        self.test_maze = maze_gen(0)
        self.wf = WallFollower(self.test_maze)

    def test_find_start_and_end(self):
        val = self.wf.find_start_and_end(self.test_maze)
        self.assertEqual(val, ((7, 5), (0, 1)))

    def test_find_start_and_end_missing_S(self):
        self.test_maze[7] = "##########"
        val = self.wf.find_start_and_end(self.test_maze)
        self.assertEqual(val, "Alkua tai loppua ei löytynyt.")

    def test_find_start_and_end_missing_G(self):
        self.test_maze[0] = "#########"
        val = self.wf.find_start_and_end(self.test_maze)
        self.assertEqual(val, "Alkua tai loppua ei löytynyt.")

    def test_find_block_type(self):
        val = self.wf.block_type(self.test_maze, 5, 7)
        self.assertEqual(val, "S")

    def test_find_block_type_2(self):
        val = self.wf.block_type(self.test_maze, 2, 2)
        self.assertEqual(val, "#")

    def test_find_block_type_3(self):
        val = self.wf.block_type(self.test_maze, 3, 2)
        self.assertEqual(val, " ")

    def test_wall_follower(self):
        self.wf.wall_follower(self.test_maze, 5, 7, 0)
        self.assertEqual(self.wf.visited[0:4],
                         [[5, 7], [5, 6], [5, 5], [6, 5]])

    def test_wall_follower_maze_med(self):
        self.test_maze = maze_gen(1)
        self.wf = WallFollower(self.test_maze)
        start = self.wf.find_start_and_end(self.test_maze)
        self.wf.wall_follower(self.test_maze, start[0][1], start[0][0], 3)
        self.assertEqual(self.wf.visited[0:4],
                         [[20, 21], [20, 20], [20, 19], [20, 18]])

    def test_wall_follower_maze_large(self):
        self.test_maze = maze_gen(2)
        self.wf = WallFollower(self.test_maze)
        start = self.wf.find_start_and_end(self.test_maze)
        self.wf.wall_follower(self.test_maze, start[0][1], start[0][0], 3)
        self.assertEqual(self.wf.visited[0:4],
                         [[29, 31], [29, 30], [30, 30], [30, 29]])

    def test_wall_follower_maze_trem(self):
        self.test_maze = maze_gen("t")
        self.wf = WallFollower(self.test_maze)
        start = self.wf.find_start_and_end(self.test_maze)
        print("AAAAAAA", start)
        self.wf.wall_follower(self.test_maze, start[0][1], start[0][0], 3)
        self.assertEqual(self.wf.visited[0:4],
                         [[1, 0], [1, 1], [2, 1], [3, 1]])

    def test_wall_follower_stuck(self):
        self.test_maze[7] = "##########"
        self.test_maze[6] = "##########"
        self.test_maze[5] = "##########"
        self.wf.wall_follower(self.test_maze, 5, 7, 0)
        self.assertEqual(self.wf.visited, [[5, 7]])

    def test_draw_maze(self):
        self.wf.wall_follower(self.test_maze, 7, 5, 3)
        val = self.wf.draw_maze()
        self.assertEqual(val[3], "#*#****#3")
