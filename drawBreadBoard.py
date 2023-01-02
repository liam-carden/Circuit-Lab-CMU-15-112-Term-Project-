from cmu_112_graphics import *

# draws the breadboard
def drawBreadBoard(app, canvas, breadboard):
    numRows = len(breadboard)

    # row number labels
    xCord = app.width * (1 / 30)
    oldYCord = app.height * (1 / 50)
    for rowNumber in range(1, numRows + 1):
        yCord = app.height * (1 / 20) + oldYCord
        canvas.create_text(xCord, yCord, text=str(rowNumber))
        canvas.create_rectangle(xCord + app.width * (1 / 8.5), yCord, 
                                xCord + app.width * (1 / 3.05), yCord,
                                fill = 'grey')
        canvas.create_rectangle(xCord + app.width * (3.15 / 8.5), yCord, 
                                xCord + app.width * (1 / 1.75), yCord,
                                fill = 'grey')
        oldYCord = yCord

    # column letter labels
    yCord = app.height * (1 / 35)
    
    initialXMove = app.width * (1 / 25)
    oldXCord = initialXMove
    additional = 0
    condition = False
    side = "L"
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
        canvas.create_text(xCord, yCord, text=char)
        if char == 'j':
            condition = True
        if char == 'e':
            xrect1 = xCord + additional / 3 + app.width * (1 / 30) / 2
            xrect2 = xCord + 2 * additional / 3 + app.width * (1 / 30) / 2
            canvas.create_rectangle(xrect1, yCord, xrect2, 
                                    oldYCord + app.height * (1 / 50), 
                                    fill="grey")
            side = "R"
        if char == '-':
            canvas.create_rectangle(xCord - app.width * (1 / 500), 
                                    yCord + app.height * (1 / 50), 
                                    xCord + app.width * (1 / 500), 
                        oldYCord + app.height * (1 / 20) - app.height * (1 / 30), 
                                    fill = "blue")
        if char == '+':
            vReading = f"{breadboard[1][side][char].bar.getVoltage()}V"
            canvas.create_text(xCord - app.width * (1 / 60), yCord, 
                               text = vReading)
            canvas.create_rectangle(xCord - app.width * (1 / 500), 
                                    yCord + app.height * (1 / 50), 
                                    xCord + app.width * (1 / 500), 
                        oldYCord + app.height * (1 / 20) - app.height * (1 / 30), 
                                    fill = "red")
        oldXCord = xCord