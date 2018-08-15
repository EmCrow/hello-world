# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 23:50:46 2018

@author: mcroc
"""
import copy
import random
maze = []
x = 10
y = 10
for i in range(x):
    maze.append([])
    for j in range(y):
        maze[i].append(random.randint(0,1))
maze[0][0] =0
maze[-1][-1] = 0
#
maze =   [[0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0]]
#maze = [[0, 1, 1, 0],
#        [0, 0, 0, 1],
#        [1, 1, 0, 0],
#        [1, 1, 1, 0]]
import copy
def find_path(graph, start, end, limit, path=[]):
    path = path + [start]
    length = len(path)
    if length == limit:
        return None
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end,limit-1, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def Graph(maze):
    graph = {}
    possibleWallMoves = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            moves = []
            try:
                if maze[i][j+1] == 0 and j < len(maze[i]):
                    moves.append(( j+1, i))
            except:
                IndexError
            try:
                if maze[i][j-1] == 0 and j > 0:
                    moves.append((j-1,i))
            except:
                IndexError
            try:
                if maze[i+1][j] == 0 and i < len(maze):
                    moves.append((j, i+1))
            except:
                IndexError
            try:
                if maze[i-1][j] == 0 and i > 0:
                    moves.append((j, i-1))
            except:
                IndexError
            if maze[i][j] == 1:
                possibleWallMoves.append((i, j))
            if len(moves) > 0:
                graph[(j, i)] = moves
    return graph, possibleWallMoves

def answer(maze):
    graph, possibleWallMoves = Graph(maze)
    start = (0, 0)
    end = (len(maze) -1,len(maze[0]) -1)
    path = []
    shorty = len(maze) * len(maze[0])

    if len(maze) > 15 and len(maze[0]) > 15:
        shorty = 27
        x = [find_path(graph, start, end, shorty, path)]
    else:
        x = find_path(graph, start, end, shorty, path)

    if type(x) == list:
        if shorty < len(x):
            shorty = len(x)
    for m in possibleWallMoves:

        print(m)
        possibleMaze = copy.deepcopy(maze)
        possibleMaze[m[0]][m[1]] = 0
        possibleGraph, otherVar = Graph(possibleMaze)
        movedPath = []

        if len(maze) > 15 and len(maze[0]) > 15:
#            return len(maze) + len(maze[0]) - 1
            adjustedX = find_path(possibleGraph, start, end, shorty, movedPath)
        else:
            adjustedX = find_path(possibleGraph, start, end, shorty, movedPath)

        if adjustedX != None:
            if len(adjustedX) < shorty:
                shorty = len(adjustedX)
    return shorty
print(answer(maze))
