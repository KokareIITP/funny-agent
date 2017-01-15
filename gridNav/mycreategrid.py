'''
 * Copyright (c) 2014, 2015 Entertainment Intelligence Lab, Georgia Institute of Technology.
 * Originally developed by Mark Riedl.
 * Last edited by Mark Riedl 05/2015
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

import sys, pygame, math, numpy, random, time, copy
from pygame.locals import *

from constants import *
from utils import *
from core import *

# Creates a grid as a 2D array of True/False values (True =  traversable). Also returns the dimensions of the grid as a (columns, rows) list.
def myCreateGrid(world, cellsize):

    # find the edges of the screen
    corners = world.getPoints()
    maxX = 0
    maxY = 0
    for x, y in corners:
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y

    # determine the number of rows and columns needed
    ### ask on piazza about intersection with boundaries and floor/ceil
    row = int(math.floor(maxX / cellsize))
    col = int(math.floor(maxY / cellsize))

    print row, col

    # generate 2D array of traversability
    grid = [[True for i in xrange(col)] for j in xrange(row)]
    dimensions = (row, col)

    obstacles = world.getObstacles()
    ### TO BE COMPLETED

    return grid, dimensions
