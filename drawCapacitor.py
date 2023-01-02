from cmu_112_graphics import *
import math

# draws a Capacitor from the given (x0, y0) to (x2, y2) points
def drawCapacitor(app, canvas, x0, y0, x2, y2):
    halfX = x0 + (x2 - x0) / 2
    halfY = y0 + (y2 - y0) / 2
    canvas.create_line(x0, y0, x2, y2, width = 3)
    thisCapacitorImage = app.capacitorImage
    dx = (x2 - x0)
    dy = (y2 - y0)
    if dy == 0:
        thisCapacitorImage = app.capacitorImage.rotate(90, expand = True)
        thisCapacitorImage = app.scaleImage(thisCapacitorImage, 1 / 17)
        thisCapacitorImage = ImageTk.PhotoImage(thisCapacitorImage)
        canvas.create_image(halfX, halfY, anchor = 'c', 
                            image = thisCapacitorImage)
    if dy != 0:
        theta = math.atan(dx / dy)
        # theta /= (2*math.pi)
        # theta *= 180
        # print(theta)
        if dx == 0:
            theta = 90
        thisCapacitorImage = app.capacitorImage.rotate(theta + 90, expand = True)
        thisCapacitorImage = app.scaleImage(thisCapacitorImage, 1 / 17)
        thisCapacitorImage = ImageTk.PhotoImage(thisCapacitorImage)
        canvas.create_image(halfX, halfY, anchor = 'c', 
                            image = thisCapacitorImage)