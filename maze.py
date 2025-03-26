#!/usr/bin/python3

class Maze:
    def __init__(self, map):
        self.map = map
        self.start = 0
        self.width = 0
        self.height = 0
        self.setStartingPoint()
        self.setSize()
        
    def setStartingPoint(self):
        for index,route in enumerate(self.map):
            if route == 'S':
                self.start = index+1
                break

    def setSize(self):
        for index, route in enumerate(self.map):
            if route == '\n':
                self.width = index+1
                break
        self.height = self.map.count('\n')+1