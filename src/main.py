import pygame
import time
from ui.grid import draw
from mazes import maze_gen
from wall_follower import WallFollower
from tremaux import Tremaux
if __name__ == "__main__":

    print("Tervetuloa labyrintinratkaisuohjelmaan.")
    print("Tällä hetkellä mahdolliset labyrintin koot ovat:")
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
            tm_start = time.process_time()
            tm = Tremaux(maze, start[0], start[1])
            tm_end = time.process_time()
            print("")
            print("Tremauxin algoritmin löytämä reitti, pituus:", len(tm.solve()))
            print("Algoritmin suoritus kesti", "{:.8f}".format(tm_end-tm_start), "sekuntia.")
            tm.print_path(tm.solve())
            facing = 3
            visited = [[start[0][1], start[0][0]]]
            wf_start = time.process_time()
            wf.wall_follower(maze, start[0][1], start[0][0], facing)
            wf_end = time.process_time()
            wf.draw_maze()
            print("Agoritmin suoritus kesti","{:.8f}".format(wf_end-wf_start) ,"sekuntia.")
            print(""*4)
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
