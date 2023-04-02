import unittest
from maze_solver import WallFollower
from mazes import maze_gen

class TestWallFollower(unittest.TestCase):
    def setUp(self):
        self.wf = WallFollower()
        self.test_maze=maze_gen(0)
    
    def test_find_start(self):
        val=self.wf.find_start(self.test_maze)
        self.assertEqual(val, (5,7))

    def test_find_block_type(self):
        val=self.wf.block_type(self.test_maze,5,7)
        self.assertEqual(val, "S")

    def test_wall_follower(self):
        visited=[[5,7]]
        self.wf.wall_follower(self.test_maze,5,7,0,visited)
        self.assertEqual(visited[0:4], [[5, 7], [5, 6], [5, 5], [6, 5]])
    
    def test_draw_maze(self):
        visited=[[5, 7], [5, 6], [5, 5], [5, 4], [5, 3], 
                 [4, 3], [3, 3], [3, 4], [3, 5], [3, 6], 
                 [3, 5], [2, 5], [1, 5], [1, 4], [1, 3], 
                 [1, 2], [1, 1], [2, 1], [3, 1], [3, 0]]
        self.wf.draw_maze(self.test_maze, visited, self.wf.mazes)
        val = self.wf.mazes[len(self.wf.mazes)-1]
        self.assertEqual(val[4][4],"#")