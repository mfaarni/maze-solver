import pygame
from ui.grid import draw
from mazes import maze_gen
from wall_follower import WallFollower
from tremaux import Tremaux
if __name__ == "__main__":

    print("Tervetuloa labyrintinratkaisuohjelmaan. \
          Tällä hetkellä mahdolliset labyrintin koot ovat:")
    while True:
        print("0: pieni")
        print("1: Keskikokoinen")
        print("2: Suuri")
        print("3: Valtava")
        user_input = input(
            "Syötä haluamasi koko tai 'q' lopettaaksesi ohjelman:")
        if user_input == "q":
            break

        if user_input in "1234567890":
            user_input = int(user_input)
        maze = maze_gen(user_input)
        if maze:
            wf = WallFollower(maze)
            start = wf.find_start_and_end(maze)
            tm = Tremaux(maze, start[0], start[1])
            print("")
            print("Tremauxin algoritmin löytämä reitti, pituus:", len(tm.solve()))
            print("")
            tm.print_path(tm.solve())
            facing = 3
            visited = [[start[0][1], start[0][0]]]
            wf.wall_follower(maze, start[0][1], start[0][0], facing)
            wf.draw_maze()
        else:
            print("\n"*6)
            print("Syöte ei hyväksyttävä, yritä uudelleen!")

    # pygame printtaukseen, ei vielä valmis joten poissa
    # size=900
    # window = pygame.display.set_mode((size,size))
    # while True:
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            exit()
    #    draw(window, wf.mazes, size, visited, pygame)
