from Node import *
from RowBar import *
from PowerBar import *
from GroundBar import *

#* Creates a new breadboard data structure
# the breadboard data structure is a multidimensional dictionary in the form
# {rowNumber:{side:{col:node}}}
def createBreadBoard(size = 5):
    breadboard = {}
    for row in range(1, 16):
        sideDict = {}
        for side in ('L', 'R'):
            colDict = {}
            if side == 'L':
                for col in ('a', 'b', 'c', 'd', 'e', '+', '-'):
                    location = (row, side, col)
                    colDict[col] = Node(location)
            else:
                for col in ('f', 'g', 'h', 'i', 'j', '+', '-'):
                    location = (row, side, col)
                    colDict[col] = Node(location)
            sideDict[side] = colDict
        breadboard[row] = sideDict

    for row in range(1, 16):
        for side in ('L', 'R'):
            rowBar = RowBar(row, side)
            powerBar = PowerBar(side)
            groundBar = GroundBar(side)
            for col in breadboard[row][side]:
                if col == '+':
                    breadboard[row][side][col].assignBar(powerBar)
                elif col == '-':
                    breadboard[row][side][col].assignBar(groundBar)
                else: 
                    breadboard[row][side][col].assignBar(rowBar)
                    rowBar.addNode(breadboard[row][side][col])

    return breadboard