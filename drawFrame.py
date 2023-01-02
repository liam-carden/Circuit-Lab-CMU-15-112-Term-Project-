from cmu_112_graphics import *

# draws the frame of the app, this includes the 
def drawFrame(app, canvas):
    verticleDivide = app.width * (3.75 / 5)
    canvas.create_line(verticleDivide, 0, verticleDivide, app.height)
    horizontalDivide = app.height * (4 / 5)
    canvas.create_line(0, horizontalDivide, app.width, horizontalDivide)
    dimension = min(app.width, app.height)
    textSize = dimension // 60
    canvas.create_text(5, app.height - 2 * textSize, 
                         anchor = 'nw', text=f'>>>{app.input}', 
                         font = f"Arial {textSize} bold",
                         fill='black')

    canvas.create_text(5, app.height * (4 / 5) + textSize,
                       anchor = 'nw', text=f'{app.display}', 
                       font = f"Arial {textSize} bold",
                       fill='black')
    quarterHeight = (app.height - (app.height - horizontalDivide)) // 4
    eigthHeight = (app.height - (app.height - horizontalDivide)) // 8
    for multiple in (1, 2, 3):
        canvas.create_line(verticleDivide, multiple * quarterHeight, 
                           app.width, multiple * quarterHeight)
    distanceYInSaved = eigthHeight
    textSize2 = dimension // 80
    if len(app.displayStorage) > 8:
        displayStorage = app.displayStorage[-3:-1]
    elif len(app.displayStorage) == 5:
        displayStorage = app.displayStorage[1:]
    elif len(app.displayStorage) == 6:
        displayStorage = app.displayStorage[2:]
    elif len(app.displayStorage) == 7:
        displayStorage = app.displayStorage[3:]
    else:
        displayStorage = app.displayStorage
    for display in displayStorage:
        canvas.create_text((65 * (app.width // 800)) + verticleDivide + 20, 
                           distanceYInSaved, anchor = 'c', text = f'{display}',
                           font = f"Arial {textSize2} bold", fil = 'black')
        distanceYInSaved += quarterHeight