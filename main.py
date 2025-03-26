#!/usr/bin/python3
from maze import Maze
from depth_first_explorer import DephtFirstExplorer

def readTextFile (filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            return file.read()
        
    except FileNotFoundError:
        print(f"file not found: {filePath}")
    except Exception as e:
        print(f"An error occured: {e}")
    return ""

mazeMap = readTextFile('maze1.txt')
maze = Maze(mazeMap)
print(f"Maze map\n{maze.map}")
print(f"Maze width: {maze.width}")
print(f"Maze height: {maze.width}")
print(f"Maze starting point: {maze.start}")

explorer = DephtFirstExplorer(maze)
explorer.getPossibleRoutes(22)
