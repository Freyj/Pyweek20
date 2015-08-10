#-------------------------------------------------------------------------------
# Name:        functions.py
# Purpose:     define a few useful functions to save some copy/paste
#
# Author:      GrumpyGrizzly
#
# Created:     10/08/2015
# Copyright:   (c) Grizzly Gaming 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
import os.path

def loadImg(path, name):
    """gives a Surface from a file in path/name, adapted to various os
    and converts the result keeping the alpha for transparency"""
    res = pygame.image.load(os.path.join(path,name))
    return res.convert_alpha()
