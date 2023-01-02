from cmu_112_graphics import *
from drawPoweredNodes import *
from createBreadBoard import *
from drawFrame import *
from drawBreadBoard import *
from drawNodes import *
from drawComponents import *
from runAnalysis import *
from Button import *
from drawTextBlockers import *
from getNodePressed import *
from runCommand import *
from documentationStorage import *
from setNodeCords import *

def appStarted(app): 
    app.nodeCords = set()
    app.breadboard = createBreadBoard()
    app.components = []
    app.markers = []
    app.input = ""
    setNodeCords(app, app.breadboard)
    app.time = 0 # or app.time = 5
    app.displayDocumentation = False
    pistachio = f'#{147:02x}{197:02x}{114:02x}'
    maroon = f'#{176:02x}{48:02x}{96:02x}'
    color = f'#{150:02x}{150:02x}{150:02x}'
    app.guidelinesButton = Button(app.width * (3.75 / 5) + 5, 
                                  app.height * (4 / 5) + 5,
                                  app.width * (4.35 / 5) - 5,
                                  app.height * (4.5 / 5) - 5, 
                                  documentationStorage(1), 'Guidelines', 
                                  'bisque2')
    app.functionsButton = Button(app.width * (4.35 / 5) + 5, 
                                 app.height * (4 / 5) + 5,
                                 app.width - 5, app.height * (4.5 / 5) - 5, 
                                 documentationStorage(2), 'Commands', pistachio)
    app.drawingButton = Button(app.width * (3.75 / 5) + 5,
                               app.height * (4.5 / 5) + 5,
                               app.width * (4.35 / 5) - 5, app.height - 5, 
                               documentationStorage(3), 'Drawing', maroon)
    app.displayButton = Button(app.width * (4.35 / 5) + 5, 
                               app.height * (4.5 / 5) + 5,
                               app.width - 5, app.height - 5, 
                               documentationStorage(4), 'Display', color)
    app.namesSet = set()
    app.nextCapacitorNumber = 1
    app.nextResistorNumber = 1

    app.resistorImageBase = Image.open("Resistor3ImageFile.jpg")
    app.resistorImage = app.resistorImageBase
    
    app.capacitorImageBase = app.loadImage("CapacitorImageFile.jpg")
    app.capacitorImage = app.capacitorImageBase

    app.display = ''
    app.totalResistance = 0
    app.totalCapacitance = 0
    app.circuitCurrent = 0
    app.circuitVoltage = 0
    app.displayStorage = []

    app.drawing = None
    app.graph = {}

def keyPressed(app, event):
    if event.key == 'Tab':
        runAnalysis(app, app.components, app.time)
    elif event.key == "Backspace":
        app.input = app.input[:-1]
    elif event.key == "Space":
        app.input = app.input + " "
    elif event.key == "Enter":
        result = runCommand(app, app.input)
        app.input = ""
    else:
        app.input = app.input + event.key

def mousePressed(app, event):
    if app.guidelinesButton.mousePressed(event.x, event.y):
        app.functionsButton.enabled = False
        app.drawingButton.enabled = False
        app.displayButton.enabled = False
    elif app.functionsButton.mousePressed(event.x, event.y):
        app.guidelinesButton.enabled = False
        app.drawingButton.enabled = False
        app.displayButton.enabled = False
    elif app.drawingButton.mousePressed(event.x, event.y):
        app.guidelinesButton.enabled = False
        app.functionsButton.enabled = False
        app.displayButton.enabled = False
    elif app.displayButton.mousePressed(event.x, event.y):
        app.guidelinesButton.enabled = False
        app.functionsButton.enabled = False
        app.drawingButton.enabled = False
    node = getNodePressed(app, (event.x, event.y), app.breadboard)
    if node != None:
        location = str(node[0]) + node[2]
        if node[2] == '-' or node[2] == '+':
            location = location + node[1]
        app.input = app.input + location + ','

def sizeChanged(app):
    setNodeCords(app, app.breadboard)
    pistachio = f'#{147:02x}{197:02x}{114:02x}'
    maroon = f'#{176:02x}{48:02x}{96:02x}'
    color = f'#{150:02x}{150:02x}{150:02x}'
    app.guidelinesButton = Button(app.width * (3.75 / 5) + 5, 
                                  app.height * (4 / 5) + 5,
                                  app.width * (4.35 / 5) - 5,
                                  app.height * (4.5 / 5) - 5, 
                                  documentationStorage(1), 'Guidelines', 
                                  'bisque2')
    app.functionsButton = Button(app.width * (4.35 / 5) + 5, 
                                 app.height * (4 / 5) + 5,
                                 app.width - 5, app.height * (4.5 / 5) - 5, 
                                 documentationStorage(2), 'Commands', pistachio)
    app.drawingButton = Button(app.width * (3.75 / 5) + 5,
                               app.height * (4.5 / 5) + 5,
                               app.width * (4.35 / 5) - 5, app.height - 5, 
                               documentationStorage(3), 'Drawing', maroon)
    app.displayButton = Button(app.width * (4.35 / 5) + 5, 
                               app.height * (4.5 / 5) + 5,
                               app.width - 5, app.height - 5, 
                               documentationStorage(4), 'Display', color)

def redrawAll(app, canvas):
    drawFrame(app, canvas)
    drawTextBlockers(app, canvas)
    drawBreadBoard(app, canvas, app.breadboard)
    drawNodes(app, canvas, app.breadboard)
    drawComponents(app, canvas, app.components)
    drawPoweredNodes(app, canvas, app.breadboard)
    app.guidelinesButton.redrawButton(app, canvas)
    app.functionsButton.redrawButton(app, canvas)
    app.drawingButton.redrawButton(app, canvas)
    app.displayButton.redrawButton(app, canvas)

runApp(width=800, height=800)