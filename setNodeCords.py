# sets the node cordinants given where they were created and assigns them to
# their respective node object
#! is separate function from drawNodes inorder to avoid MVC violations
def setNodeCords(app, breadboard):
    numRows = len(breadboard)
    xCord = app.width * (1 / 30)
    oldYCord = app.height * (1 / 50)
    initialXMove = app.width*(1 / 25)
    oldXCord = initialXMove
    additional = 0
    condition = False
    side = 'L'
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
            if char == 'f':
                side = "R"
            coordinates = (xCord, yCord)
            oldXCord = xCord
            # This is the part that deals with linking the node to the cords
            breadboard[rowNumber][side][char].setCords(coordinates)
            app.nodeCords.add(coordinates)
        oldYCord = yCord
        oldXCord = initialXMove
        side = 'L'