#-------------------------------------------------------------------------------
# Name:        Game
# Purpose:     Main class of the game More Data is required !
#
# Author:       GrumpyGrizzly
#
# Created:     09/08/2015
# Copyright:   (c)  Grizzly Gaming 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
from constants_pw import *
from functions import *
class Game:

    screen = pygame.display.set_mode(DISPLAY_SIZE)

    def __init__(self):
            pygame.init()

            pygame.display.set_caption("We need more data ! v0.1")
            self.background = pygame.Surface(DISPLAY_SIZE)
            self.started = True
            self.clock = pygame.time.Clock()
            self.state = STATES[1]

    def start(self):
            while self.started:
                for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                       self.started = False
                  if event.type == pygame.MOUSEBUTTONUP:
                        #for testing purposes
                        print(pygame.mouse.get_pos())

                if self.state == STATES[1]:
                    #make pictures used & blit them
                    self.background = loadImg('img','background.jpg')
                    self.screen.blit(self.background, (0,0))
                    banner  = loadImg('img', 'banner.png')
                    self.screen.blit(banner, (0,0))
                    b_start = loadImg('img', 'b_new.png')
                    self.screen.blit(b_start, (260, 210))
                    b_highscores = loadImg('img', 'b_highscores.png')
                    self.screen.blit(b_highscores, (260,300))
                    b_quit = loadImg('img', 'b_quit.png')
                    self.screen.blit(b_quit, (260,390))

                    pygame.display.flip()

            self.clock.tick(60)
            pygame.quit()
