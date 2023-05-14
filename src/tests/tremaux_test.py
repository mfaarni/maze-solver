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

    def test_algorithm_small(self):
        val = self.tremaux.solve()
        self.assertEqual(val[0:5], [(7, 5), (6, 5), (5, 5), (5, 6), (4, 6)])

    def test_algorithm_med(self):
        self.test_maze = maze_gen(1)
        self.start_cords = self.wf.find_start_and_end(self.test_maze)
        self.tremaux = Tremaux(
            self.test_maze, self.start_cords[0], self.start_cords[1])
        val = self.tremaux.solve()
        self.assertEqual(val[0:5], [(21, 20), (20, 20), 
                                    (19, 20), (18, 20), (17, 20)])

    def test_algorithm_large(self):
        self.test_maze = maze_gen(2)
        self.start_cords = self.wf.find_start_and_end(self.test_maze)
        self.tremaux = Tremaux(
            self.test_maze, self.start_cords[0], self.start_cords[1])
        val = self.tremaux.solve()
        self.assertEqual(val[0:5], [(31, 29), (30, 29),
         (30, 30), (29, 30), (28, 30)])


    def test_algorithm_huge(self):
        self.test_maze = maze_gen(3)
        self.start_cords = self.wf.find_start_and_end(self.test_maze)
        self.tremaux = Tremaux(
            self.test_maze, self.start_cords[0], self.start_cords[1])
        val = self.tremaux.solve()
        self.assertEqual(val[0:5], [(80, 79),
             (79, 79), (79, 78), (79, 77), (78, 77)])

    def test_algorithm_circular(self):
        self.test_maze = [
        "#################",
        "# #  #      # #G#",
        "# #### #  #   # #",
        "### #   # # ### #",
        "#   #   #    #  #",
        "# # # #  ###   ##",
        "#     #      ## #",
        "#  ##   #   #   #",
        "#  ##  ###    ###",
        "#      # ###  # #",
        "#S  #    # #    #",
        "#################",
        ]
    def test_algorithm_circular_2(self):
        self.test_maze = [
        "#################",
        "#               #",
        "#           #   #",
        "#   ####### ##  #",
        "#   # #   # #  ##",
        "#   #   G # #   #",
        "#   # #   # # # #",
        "#   # ##### #   #",
        "#   #       ##  #",
        "#   #########   #",
        "#S             ##",
        "#################",
        ]
        self.start_cords = self.wf.find_start_and_end(self.test_maze)
        print(self.start_cords)
        self.tremaux = Tremaux(
            self.test_maze, self.start_cords[0], self.start_cords[1])
        val = self.tremaux.solve()
        self.assertEqual(val[-1], (5,8))
        self.assertEqual(len(val),55)

    def test_algorithm_circular_2(self):
        self.test_maze = [
        "#################",
        "#      # # #  # #",
        "# # ## #        #",
        "#   #  ## #######",
        "######    # #   #",
        "######    # # # #",
        "#      G    # # #",
        "# # #     ### # #",
        "#             # #",
        "############# ###",
        "#S              #",
        "#################",
        ]
        self.start_cords = self.wf.find_start_and_end(self.test_maze)
        self.tremaux = Tremaux(
            self.test_maze, self.start_cords[0], self.start_cords[1])
        val = self.tremaux.solve()
        self.assertEqual(val[-1], (6, 7))

    def test_algorithm_on_exit(self):
        self.test_maze = maze_gen(2)
        self.start_cords = ((20,20),(20,20))
        self.tremaux = Tremaux(
            self.test_maze, self.start_cords[0], self.start_cords[1])
        val = self.tremaux.solve()
        self.assertEqual(len(val),1)

    def test_path_len(self):
        val = self.tremaux.solve()
        self.assertEqual(len(val), 20)

    def test_path_len_med(self):
        self.test_maze = maze_gen(1)
        self.start_cords = self.wf.find_start_and_end(self.test_maze)
        self.tremaux = Tremaux(
            self.test_maze, self.start_cords[0], self.start_cords[1])
        val = self.tremaux.solve()
        self.assertEqual(len(val), 84)

                
    def test_is_valid(self):
        val=self.tremaux.is_valid(3,3)
        self.assertEqual(val, True)

    def test_print(self):
        val = self.tremaux.print_path(self.tremaux.solve())
        self.assertEqual(val[:4], [(7, 5), (6, 5), (5, 5), (5, 6)])

    def test_print_no_path(self):
        val = self.tremaux.print_path(None)
        self.assertEqual(val, None)

    def test_visualize_return(self):
        path = self.tremaux.solve()
        val = self.tremaux.visualize(path)
        self.assertIsInstance(val, list)

    def test_visualize_return_large(self):
        cords= self.wf.find_start_and_end(maze_gen(2))
        self.tremaux = Tremaux(
            maze_gen(2), cords[0], cords[1])
        path = self.tremaux.solve()
        val = self.tremaux.visualize(path)
        self.assertIsInstance(val, list)

    def test_visualize_path(self):
        path = self.tremaux.solve()
        val = self.tremaux.visualize(path)
        self.assertEqual(val[0:3], [['#G######0', '# #    #1', '# # ####2', '# #    #3', '# # ## #4', '# # #  #5', '#   # ##6', '#####X##7', '01234567-'], 
                               ['#G######0', '# #    #1', '# # ####2', '# #    #3', '# # ## #4', '# # #  #5', '#   #O##6', '#####X##7', '01234567-'], 
                               ['#G######0', '# #    #1', '# # ####2', '# #    #3', '# # ## #4', '# # #O #5', '#   #X##6', '#####X##7', '01234567-']])