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
import ptext
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
                        #for the beginning, testing if the mouse
                        #clicked on a button
                        mouse = pygame.mouse.get_pos()
                        #events on the starting menu
                        if self.state == STATES[1]:
                            rect_new = pygame.Rect((260,210),(260,60))
                            rect_high = pygame.Rect((260,300),(260,60))
                            rect_quit = pygame.Rect((260,390),(260,60))
                            if pygame.Rect.collidepoint(rect_new, mouse):
                                self.state = STATES[3]
                            elif pygame.Rect.collidepoint(rect_high,mouse):
                                self.state = STATES[2]
                            elif pygame.Rect.collidepoint(rect_quit,mouse):
                                self.started = False
                        #events on the highscore screen
                        if self.state == STATES[2]:
                            rect_back = pygame.Rect((10,10), (260, 60))
                            if pygame.Rect.collidepoint(rect_back, mouse):
                                self.state = STATES[1]
                        #events on the game screen
                        if self.state == STATES[3]:
                            pass
                        #events on the game over screen
                        if self.state == STATES[4]:
                            pass
                #start menu
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
                #highscore display
                elif self.state == STATES[2]:
                    self.screen.blit(self.background, (0,0))
                    b_back = loadImg('img','b_back.png')
                    self.screen.blit(b_back, (10,10))
                    banner = loadImg('img', 'highscores.png')
                    self.screen.blit(banner, (0,0))
                    #put a placeholder box to test size
                    #TODO : do a highscore thingy
                    placeholder = pygame.Surface((500,400))
                    placeholder.fill(WHITE)
                    self.screen.blit(placeholder, (150,190))

                    pygame.display.flip()
                #game
                elif self.state == STATES[3]:
                    self.screen.blit(self.background, (0,0))
                    b_abandon = loadImg('img','b_abandon.png')
                    portrait_cap = loadImg('img', 'Space_Captain_min.png')
                    portrait_pil = loadImg('img', 'Pilotmini.png')
                    portrait_sci = loadImg('img', 'Science_Officer_min.png')
                    portrait_sec = loadImg('img', 'SecurityOfficer_min.png')
                    #bg_ui = loadImg('img', 'bg_ui.png')
                    #self.screen.blit(bg_ui, (0,0))
                    self.screen.blit(portrait_cap, (30,10))
                    self.screen.blit(portrait_pil, (170,10))
                    self.screen.blit(portrait_sci, (320,10))
                    self.screen.blit(portrait_sec, (470,10))
                    self.screen.blit(b_abandon, (720, 10))
                    pygame.display.flip()
                #game_over display
                elif self.state == STATES[4]:
                    pass

            self.clock.tick(60)
            pygame.quit()
