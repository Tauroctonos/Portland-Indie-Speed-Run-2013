__author__ = 'Devin & Stan'

import pygame

##
#Game
#Description: runs the main operational code
#
#Variables:
#
#
#

class Game(object):

    ##
    #__init__
    #
    #
    def __init__(self):
        pygame.init()
        size = (500, 500) #(width, height)
        self.screen = pygame.display.set_mode(size)


a = Game()
