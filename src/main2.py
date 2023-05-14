from pygame.locals import *
import pygame
import sys
import time
from ui.grid import draw, grid
from mazes import maze_gen
from wall_follower import WallFollower
from tremaux import Tremaux


mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('game base')
size = 900
screen = pygame.display.set_mode((size, size))
font = pygame.font.SysFont(None, 70)
font_2 = pygame.font.SysFont(None, 34)


def draw_text(text, font, colour, surface, x, y):
    text_object = font.render(text, 1, colour)
    textrect = text_object.get_rect()
    textrect.topleft = (x, y)
    surface.blit(text_object, textrect)


def main_menu():

    click = False
    while True:
        screen.fill((41, 163, 82))
        draw_text('Labyrintinratkaisija', font,
                  (255, 255, 204), screen, 240, 40)

        mx, my = pygame.mouse.get_pos()
        buttons = [
            pygame.Rect(250, 150, 400, 95),
            pygame.Rect(250, 300, 400, 95),
            pygame.Rect(250, 450, 400, 95),
            pygame.Rect(250, 600, 400, 95)
        ]
        for button in buttons:
            pygame.draw.rect(screen, (255, 50, 125), button)

            if button.collidepoint((mx, my)):
                pygame.draw.rect(screen, (225, 20, 85), button)
                if click:
                    click = False
                    info(buttons.index(button))
        draw_text('Pieni', font, (255, 255, 255), screen, 387, 173)
        draw_text('Keskikokoinen', font, (255, 255, 255), screen, 275, 323)
        draw_text('Suuri', font, (255, 255, 255), screen, 380, 473)
        draw_text('Valtava', font, (255, 255, 255), screen, 360, 623)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)


def info(lab):
    click = False
    maze = maze_gen(lab)
    wf = WallFollower(maze)
    start = wf.find_start_and_end(maze)
    tm = Tremaux(maze, start[0], start[1])
    tm_start = time.process_time()
    tm_visited = tm.solve()
    tm_time = time.process_time() - tm_start
    print("")
    print("Tremauxin algoritmin löytämä reitti, pituus:", len(tm_visited))
    print("Algoritmin suoritus kesti", "{:.8f}".format(
        tm_time-tm_start), "sekuntia.")
    tm_path = tm.print_path(tm.solve())
    facing = 3
    wf_start = time.process_time()
    wf.wall_follower(maze, start[0][1], start[0][0], facing)
    wf_time = time.process_time() - wf_start
    visited = wf.draw_maze()
    print("Algoritmin suoritus kesti", "{:.8f}".format(wf_time), "sekuntia.")
    print(""*4)
    tm_mazes = tm.visualize(tm_path)
    running = True
    click = False

    while running:
        screen.fill((41, 163, 82))
        grid(screen, maze, 900, True)

        draw_text('Labyrintinratkaisija', font,
                  (255, 255, 204), screen, 240, 40)

        draw_text('Wall Follower-algoritmi:', font_2,
                  (255, 255, 204), screen, 170, 180)
        draw_text('Algoritmin suoritus kesti ' + '{:.8f}'.format(
            wf_time) + " sekuntia.", font_2, (255, 255, 204), screen, 170, 220)
        draw_text('Löydetyn reitin pituus on ' + str(len(visited)) +
                  " siirtoa.", font_2, (255, 255, 204), screen, 170, 250)

        draw_text('Trémauxin algoritmi:', font_2,
                  (255, 255, 204), screen, 170, 350)
        draw_text('Algoritmin suoritus kesti ' + '{:.8f}'.format(
            tm_time) + " sekuntia.", font_2, (255, 255, 204), screen, 170, 390)
        draw_text('Löydetyn reitin pituus on ' + str(len(tm_visited)) +
                  " siirtoa.", font_2, (255, 255, 204), screen, 170, 420)

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(250, 600, 400, 95)
        button_2 = pygame.Rect(250, 730, 400, 95)

        pygame.draw.rect(screen, (255, 50, 125), button_1)
        pygame.draw.rect(screen, (255, 50, 125), button_2)
        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (225, 20, 85), button_1)
            if click:
                click = False
                solver(wf.mazes, visited)
        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(screen, (225, 20, 85), button_2)
            if click:
                click = False
                solver(tm_mazes, visited)

        draw_text('Wall Follower', font, (255, 255, 255), screen, 270, 622)
        draw_text('Trémaux', font, (255, 255, 255), screen, 270, 750)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    click = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def solver(mazes, visited):
    running = True
    while running:
        screen.fill((0, 0, 0))
        running = draw(screen, mazes, size, visited, pygame)
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

        pygame.display.update()
        mainClock.tick(60)


if __name__ == "__main__":

    running = True
    menu = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        if menu:
            main_menu()
