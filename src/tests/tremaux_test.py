import unittest
from tremaux import Tremaux
from wall_follower import WallFollower
from mazes import maze_gen


class TremauxFollower(unittest.TestCase):
    def setUp(self):
        self.test_maze = maze_gen(0)
        self.wf = WallFollower(self.test_maze)
        self.start_cords = self.wf.find_start_and_end(self.test_maze)
        self.tremaux = Tremaux(
            self.test_maze, self.start_cords[0], self.start_cords[1])

    def test_algorithm(self):
        val = self.tremaux.solve()
        self.assertEqual(val[0:5], [(7, 5), (6, 5), (5, 5), (5, 6), (4, 6)])

    def test_algorithm_med(self):
        self.test_maze = maze_gen(1)
        self.start_cords = self.wf.find_start_and_end(self.test_maze)
        self.tremaux = Tremaux(
            self.test_maze, self.start_cords[0], self.start_cords[1])
        val = self.tremaux.solve()
        self.assertEqual(val[0:5], [(15, 20), (14, 20),
                         (12, 20), (10, 20), (9, 20)])

    def test_algorithm_large(self):
        self.test_maze = maze_gen(2)
        self.start_cords = self.wf.find_start_and_end(self.test_maze)
        self.tremaux = Tremaux(
            self.test_maze, self.start_cords[0], self.start_cords[1])
        val = self.tremaux.solve()
        self.assertEqual(val[0:5], [(30, 29), (30, 30),
                         (29, 30), (28, 30), (28, 29)])

    def test_path_len(self):
        val = self.tremaux.solve()
        self.assertEqual(len(val), 20)

    def test_print(self):
        val = self.tremaux.print_path(self.tremaux.solve())
        self.assertEqual(val[:4], [(7, 5), (6, 5), (5, 5), (5, 6)])

    def test_print_no_path(self):
        val = self.tremaux.print_path(None)
        self.assertEqual(val, None)
