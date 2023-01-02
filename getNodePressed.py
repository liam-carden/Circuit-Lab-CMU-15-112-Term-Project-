# Takes in a set of event coordinates (x,y) and returns the node object at that
# point.
def getNodePressed(app, coordinates, breadboard):
    eventX, eventY = coordinates
    numRows = len(breadboard)
    side = 'L'
    nodeRadius = app.width * (1 / 150)
    for rowNumber in range(1, numRows + 1):
        for char in ('-', '+', 'a', 'b', 'c', 'd', 'e',
                     'f', 'g', 'h', 'i', 'j', '-', '+'):
            if char == 'f':
                side = "R"
            nodeInQuestion = breadboard[rowNumber][side][char]
            (xC, yC) = nodeInQuestion.getCords()
            x0 = xC - nodeRadius
            x1 = xC + nodeRadius
            y0 = yC - nodeRadius
            y1 = yC + nodeRadius
            if x0 <= eventX <= x1 and y0 <= eventY <= y1:
                return nodeInQuestion.getLocation()
        side = 'L'