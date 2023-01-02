from cmu_112_graphics import *
import math

# draws a Resistor from (x1,y1) to (x2,y2)
def drawResistor(app, canvas, x1, y1, x2, y2):
    halfX = x1 + (x2 - x1) / 2
    halfY = y1 + (y2 - y1) / 2
    canvas.create_line(x1, y1, x2, y2, fill = "black", width = 3)
    thisResistorImage = app.resistorImage
    dx = (x2 - x1)
    dy = (y2 - y1)
    if dy != 0:
        theta = math.atan(dx / dy)
        if dx == 0:
            theta = 90
        thisResistorImage = app.resistorImage.rotate(theta, expand = True)
    thisResistorImage = app.scaleImage(thisResistorImage, 1 / 17)
    thisResistorImage = ImageTk.PhotoImage(thisResistorImage)
    canvas.create_image(halfX, halfY, anchor = 'c', image = thisResistorImage)