from cmu_112_graphics import *
from Wire import *
from Resistor import *
from drawResistor import *
from drawCapacitor import *
from Capacitor import *

# draws the components from the component list
def drawComponents(app, canvas, components):
    for component in components:
        x1, y1 = component.startNode.getCords()
        x2, y2 = component.endNode.getCords()
        if isinstance(component, Wire):
            color = component.getColor()
            canvas.create_line(x1, y1, x2, y2, fill = color, width = 3)
        if isinstance(component, Resistor):
            name = component.getName()
            drawResistor(app, canvas, x1, y1, x2, y2)
            halfX = x1 + (x2 - x1) / 2
            halfY = y1 + (y2 - y1) / 2
            canvas.create_text(halfX, halfY, text = name, 
                               font = "Arial 10 bold", fill = "brown") 
        if isinstance(component, Capacitor):
            name = component.getName()
            drawCapacitor(app, canvas, x1, y1, x2, y2)
            halfX = x1 + (x2 - x1) / 2
            halfY = y1 + (y2 - y1) / 2
            canvas.create_text(halfX, halfY, text = name, 
                               font = "Arial 10 bold", fill = "brown")