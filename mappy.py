#-------------------------------------------------------------------------------
# Name:        Map
# Purpose:     the making of the map that will be played on.
#
# Author:      GrumpyGrizzly
#
# Created:     11/08/2015
# Copyright:   (c) Grizzly Gaming 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import pygame
import functions
import os.path
from constants_pw import *

class Map:

    def __init__(self, path):
        self.size_case = (14,26)
        self.size_real = (448, 768)
        self.map = self.createMap(path)

    def deleteReturn(self, path):
        """Removes the \n at the end of each line
        and returns a string with the whole map"""
        mapread = open(os.path.join('res', path), 'r')
        res=''
        for line in mapread:
            line = line.replace('\n','')
            res += line
        return res

    def getType(self,x):
        return self.map[x]

    def tupToX(self, x, y):
        return x * 26 + y % 26

    def createMap(self, path):
        return self.deleteReturn(path)

    def makeMapSurface(self):
        surf = pygame.Surface((768,448))
        surf.set_colorkey(BLACK)
        for i in range(self.size_case[0]):
            for j in range(self.size_case[1]):
                #1 is top left
                s = pygame.Surface((32,32))
                if self.getType(self.tupToX(i,j)) == '1':
                    s = functions.loadImg('img', 'corner.png')
                elif self.getType(self.tupToX(i,j)) == '2':
                    s = functions.loadImg('img', 'flat.png')
                elif self.getType(self.tupToX(i,j)) == '3':
                    s = functions.loadImg('img', 'corner.png')
                    s = pygame.transform.rotate(s, 270)
                elif self.getType(self.tupToX(i,j)) == '4':
                    s = functions.loadImg('img', 'flat.png')
                    s = pygame.transform.rotate(s, 270)
                elif self.getType(self.tupToX(i,j)) == '5':
                    s = functions.loadImg('img', 'sol.png')
                elif self.getType(self.tupToX(i,j)) == '6':
                    s = functions.loadImg('img', 'flat.png')
                    s = pygame.transform.rotate(s, 180)
                elif self.getType(self.tupToX(i,j)) == '7':
                    s = functions.loadImg('img', 'corner.png')
                    s = pygame.transform.rotate(s, 180)
                elif self.getType(self.tupToX(i,j)) == '8':
                    s = functions.loadImg('img', 'flat.png')
                    s = pygame.transform.rotate(s, 90)
                elif self.getType(self.tupToX(i,j)) == '9':
                    s = functions.loadImg('img', 'corner.png')
                    s = pygame.transform.rotate(s, 90)
                else:
                    s = functions.loadImg('img', 'empty.png')
                pygame.Surface.blit(surf, s, (32*i, 32*j))
                surf = surf.convert_alpha()

        return surf



m = Map('map.txt')

print(m)


