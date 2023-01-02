from cmu_112_graphics import *

# draws the Nodes of the breadboard
def drawNodes(app, canvas, breadboard):
    nodeRadius = app.width * (1 / 150)
    numRows = len(breadboard)
    xCord = app.width * (1 / 30)
    oldYCord = app.height * (1 / 50)
    initialXMove = app.width * (1 / 25)
    oldXCord = initialXMove
    additional = 0
    condition = False
    for rowNumber in range(1, numRows + 1):
        yCord = app.height * (1 / 20) + oldYCord
        for char in ('-', '+', 'a', 'b', 'c', 'd', 'e', 
                     'f', 'g', 'h', 'i', 'j', '-', '+'):
            if char.isalpha():
                additional = app.width * (1 / 60)
            else:
                additional = 0
            if condition:
                additional = app.width * (1 / 60)
                condition = False
            xCord = oldXCord + app.width * (1 / 30) + additional
            if char == 'j':
                condition = True
            canvas.create_oval(xCord - nodeRadius, yCord - nodeRadius,
                               xCord + nodeRadius, yCord + nodeRadius, 
                               fill = 'grey')
            oldXCord = xCord
        oldYCord = yCord
        oldXCord = initialXMove