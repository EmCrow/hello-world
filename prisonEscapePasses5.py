# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:49:08 2018

@author: mcroc
"""
def: TryGit():
    """# TODO: """
    pass
def NextMove(xMove, yMove, maze):
    NewPoint = 2
    try:
        NewPoint = maze[yMove][xMove]
    except:
        IndexError
    return NewPoint

def Inside(x, maze):
    return x >= 0 and x <= len(maze)

def Movement(x, y, maze, pastMove, message):
    position = [x, y]
    pastMove.append(position)
    return position, pastMove, message


def PossibleMoves(x,y,maze, pastMove):
    try:
        if Inside(x, maze) and Inside(y,maze):
            return maze[y][x] == 0 and [x,y] not in pastMove
    except:
        IndexError
    return False

def answer(maze, pastMove = [[0,0]],position = [0,0],x = 0,y = 0, moveCount = 1):

    while position != [len(maze) -1, len(maze)-1] and moveCount < 30:
        moves = [[x+1, y, 'x', 'Right'], [x, y+1,'y', 'Down'], [x-1, y,'x','left'], [x, y-1,'y','Up']]
        nextChoices = []
        for i in moves:
            if PossibleMoves(i[0],i[1],maze, pastMove):
                nextChoices.append(i)
#            print(PossibleMoves(i[0],i[1],maze, pastMove), end=  '    ')
            print(nextChoices, position)

#        if len(nextChoices) > 1:
#            lengthList = []
#            for i in nextCoices:
#                branchCount = answer(maze,pastMove,position,x,y,moveCount)
#
#

        xPoint = nextChoices[0][0]
        yPoint = nextChoices[0][1]
        varChanger = nextChoices[0][2]
        message = nextChoices[0][3]

        if NextMove(xPoint,yPoint,maze) == 0 and Inside(xPoint,maze) and [xPoint, yPoint] not in pastMove:
            position , pastMove ,message= Movement(xPoint, yPoint, maze, pastMove, message)
            x= xPoint if varChanger == 'x' else x
            y= yPoint if varChanger == 'y' else y
            moveCount += 1
            print(str(message))
#        moveCount +=1
    return moveCount

import random
def Maze(x=5):
    maze = []

    for i in range(x):
        maze.append([])
        for j in range(x):
            maze[i].append(random.randint(0,1))
    maze[0][0] =0
    maze[-1][-1] = 0

    return maze

#maze =   [[0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0]]
#maze = [[0, 1, 1, 0],
#        [0, 0, 0, 1],
#        [1, 1, 0, 0],
#        [1, 1, 1, 0]]
y = Maze()
print('\n')
for i in y:
    print(i)
x = answer(y)
print(x)
