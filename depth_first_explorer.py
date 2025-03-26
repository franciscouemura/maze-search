#!/usr/bin/python3
import math
from maze import Maze

class DephtFirstExplorer:
    def __init__(self, maze):
        self.frontier= []
        self.exploredSet=[]
        self.maze: Maze = maze

    def exploreCurrentNode(self, node:int):
        return
    
    def getPossibleRoutes(self, currentRoute: int):
        currentRouteLine = math.ceil(currentRoute/self.maze.width)
        currentRouteColumn = currentRoute - self.maze.width*(currentRouteLine-1)
        print(f'currentRouteLine {currentRouteLine}')
        print(f'currentRouteColumn {currentRouteColumn}')
        
        #TODO: validate before explore
        #TODO: explore item above
        #TODO: explore item below
        #TODO: explore item at right side
        #TODO: explore item at left side
        #TODO: pushi this to git