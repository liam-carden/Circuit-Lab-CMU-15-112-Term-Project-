from cmu_112_graphics import *

# draws white space blockers that prevent text from clipping through various
# other parts of the app
def drawTextBlockers(app, canvas):
    # behind button
    behindButtonX = app.width * (3.75 / 5)
    behindButtonY = app.height * (4 / 5)
    canvas.create_rectangle(behindButtonX, behindButtonY, 
                            app.width+5, app.height+5, fill = 'white')

    # behind circuit
    canvas.create_rectangle(-5, -5, behindButtonX, behindButtonY, fill = 'white')