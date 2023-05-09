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
            last = wf.find_start_and_end(maze)
            tm_start = time.process_time()
            tm = Tremaux(maze, last[0], last[1])
            tm_end = time.process_time()
            print("")
            print("Tremauxin algoritmin löytämä reitti, pituus:", len(tm.solve()))
            print("Algoritmin suoritus kesti", "{:.8f}".format(tm_end-tm_start), "sekuntia.")
            tm_path = tm.print_path(tm.solve())
            facing = 3
            wf_start = time.process_time()
            wf.wall_follower(maze, last[0][1], last[0][0], facing)
            wf_end = time.process_time()
            visited = wf.draw_maze()
            print("Agoritmin suoritus kesti","{:.8f}".format(wf_end-wf_start) ,"sekuntia.")
            print(""*4)
            tm_mazes=tm.visualize(tm_path)

            user_input=input(
                "Syötä 'p', mikäli haluat labyrintin visualisoinnin pygamella tai 'b' palataksesi ohjelman päävalikkoon:"
            )
            if user_input=="b":
                continue
            if user_input=="p":        
                size=900
                window = pygame.display.set_mode((size,size))
                running=True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running=False
                            pygame.quit()
                    draw(window, wf.mazes, size, visited, pygame)
                    
                    draw(window, tm_mazes, size, visited, pygame)

        else:
            print("\n"*6)
            print("Syöte ei hyväksyttävä, yritä uudelleen!")

