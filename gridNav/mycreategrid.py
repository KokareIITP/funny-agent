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

    worldDimensions = world.getDimensions()
    x = worldDimensions[0]
    y = worldDimensions[1]

    # determine the number of rows and columns needed
    numRows = int(math.floor(x / cellsize))
    numCols = int(math.floor(y / cellsize))

    # generate 2D array of traversability
    grid = [[True for i in xrange(numCols)] for j in xrange(numRows)]
    dimensions = (numRows, numCols)

    obstacles = world.getObstacles()
    for row in xrange(numRows):
        for col in xrange(numCols):
            # check for intersections
            corner1 = (row * cellsize, col * cellsize)
            corner2 = (row * cellsize, (col + 1) * cellsize)
            corner3 = ((row + 1) * cellsize, col * cellsize)
            corner4 = ((row + 1) * cellsize, (col + 1) * cellsize)
            for obstacle in obstacles:
                if obstacle.pointInside(corner1) or obstacle.pointInside(corner2) or obstacle.pointInside(corner3) or obstacle.pointInside(corner4):
                    grid[row][col] = False
                for point in obstacle.getPoints():
                    if pointInsidePolygonPoints(point, [corner1, corner2, corner3, corner4]):
                        grid[row][col] = False
                for line in obstacle.getLines():
                    caseA = rayTrace(corner1, corner2, line)
                    caseB = rayTrace(corner1, corner3, line)
                    caseC = rayTrace(corner2, corner4, line)
                    caseD = rayTrace(corner3, corner4, line)
                    if caseA or caseB or caseC or caseD:
                        grid[row][col] = False

    return grid, dimensions
