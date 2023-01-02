from createBreadBoard import *
from setNodeCords import *
from Button import *
from runAnalysis import *
from getNodeFromString import *
from Wire import *
from Capacitor import *
from Resistor import *
from documentationStorage import *

# Takes in the command input from the in-app command line and runs it if
# it is a valid command.
def runCommand(app, inputString):

    # some basic hot keys for testing
    if inputString == '1':
        inputString = 'addResistor(1+L,1a,3)'
    elif inputString == '2':
        inputString = 'addResistor(1b,2b,3)'
    elif inputString == '3':
        inputString = 'addResistor(2a,2-L,3)'

    error = 'Please enter a valid command'
    executed = 'Executed Command'
    command = ''
    params = ''

    # get the command and the parameters
    if '(' in inputString:
        parenIndex = inputString.find('(')
        command = inputString[:parenIndex]
        if ')' in inputString:
            parenEndIndex = inputString.find(')')
            params = inputString[parenIndex+1:parenEndIndex]
        else:
            return error
    else:
        command = inputString

    command = command.lower()

    # this is a case that is for testing / demonstration for the TP
    # It demonstrates all the complex elements of the application
    if command in {'lcarden'}:
        pnode = app.breadboard[1]['L']['+']
        a1 = app.breadboard[1]['L']['a']
        b1 = app.breadboard[1]['L']['b']
        a2 = app.breadboard[2]['L']['a']
        b2 = app.breadboard[2]['L']['b']
        c2 = app.breadboard[2]['L']['c']
        e2 = app.breadboard[2]['L']['e']
        a3 = app.breadboard[3]['L']['a']
        b3 = app.breadboard[3]['L']['b']
        b4 = app.breadboard[4]['L']['b']
        d4 = app.breadboard[4]['L']['d']
        a5 = app.breadboard[5]['L']['a']
        e5 = app.breadboard[5]['L']['e']
        b6 = app.breadboard[6]['L']['b']
        c6 = app.breadboard[6]['L']['c']
        b6 = app.breadboard[6]['L']['b']
        a7 = app.breadboard[7]['L']['a']
        b7 = app.breadboard[7]['L']['b']
        d7 = app.breadboard[7]['L']['d']
        e7 = app.breadboard[7]['L']['e']
        b8 = app.breadboard[8]['L']['b']
        d8 = app.breadboard[8]['L']['d']
        e8 = app.breadboard[8]['L']['e']
        b10 = app.breadboard[10]['L']['b']
        c10 = app.breadboard[10]['L']['c']
        d10 = app.breadboard[10]['L']['d']
        c15 = app.breadboard[15]['L']['c']
        a15 = app.breadboard[15]['L']['a']
        gnode = app.breadboard[15]['L']['-']
        app.components.append(Resistor(pnode, a1, '1', 3))
        app.components.append(Resistor(b1, b2, '2', 3))
        app.components.append(Resistor(a2, a3, '3', 3))
        app.components.append(Capacitor(c2, c6, '4', 3))
        app.components.append(Resistor(e2, e5, '5', 3))
        app.components.append(Resistor(b3, b4, '6', 3))
        app.components.append(Resistor(d4, d7, '7', 3))
        app.components.append(Capacitor(a5, a7, '8', 3))
        app.components.append(Resistor(b6, b7, '9', 3))
        app.components.append(Resistor(e7, e8, '10', 3))
        app.components.append(Resistor(d8, d10, '11', 3))
        app.components.append(Resistor(b8, b10, '12', 3))
        app.components.append(Resistor(c10, c15, '13', 3))
        app.components.append(Resistor(a15, gnode, '14', 3))

        for name in range(1, 15):
            app.namesSet.add(str(name))

        return executed

    # sets the drawing state to None
    if command in {'stopdrawing'}:
        app.drawing = None

    # drawing functions
    if app.drawing != None:
        if app.drawing == 1: # Resistor
            paramList = inputString.split(',')
            if len(paramList) == 3:
                nodeOneString = paramList[0]
                nodeTwoString = paramList[1]
                resistanceString = paramList[2]

                if not resistanceString.isdigit():
                    return error

                nodeOne = getNodeFromString(app, nodeOneString)
                if nodeOne == None:
                    return error
                nodeTwo = getNodeFromString(app, nodeTwoString)
                if nodeTwo == None:
                    return error
                
                if '.' in resistanceString:
                    return error
                else:
                    resistance = int(resistanceString)

                name = f'R{app.nextResistorNumber}'
                while True:
                    if name in app.namesSet:
                        app.nextResistorNumber += 1
                        name = f'R{app.nextResistorNumber}'
                    else:
                        break
                app.nextResistorNumber += 1
                app.namesSet.add(name)

                app.components.append(Resistor(nodeOne, nodeTwo, name, resistance))

                return executed
            else:
                return error
        elif app.drawing == 2: # Capacitor
            paramList = inputString.split(',')
            if len(paramList) == 3:
                nodeOneString = paramList[0]
                nodeTwoString = paramList[1]
                capacitanceString = paramList[2]

                if not capacitanceString.isdigit():
                    return error

                nodeOne = getNodeFromString(app, nodeOneString)
                if nodeOne == None:
                    return error
                nodeTwo = getNodeFromString(app, nodeTwoString)
                if nodeTwo == None:
                    return error
                
                if '.' in capacitanceString:
                    return error
                else:
                    capacitance = int(capacitanceString)

                name = f'C{app.nextCapacitorNumber}'
                while True:
                    if name in app.namesSet:
                        app.nextCapacitorNumber += 1
                        name = f'C{app.nextCapacitorNumber}'
                    else:
                        break
                app.nextCapacitorNumber += 1
                app.namesSet.add(name)

                app.components.append(Capacitor(nodeOne, nodeTwo, name, capacitance))

                return executed
            else:
                return error

        elif app.drawing == 3: # Wire
            paramList = inputString.split(',')
            if len(paramList) == 3:
                nodeOneString = paramList[0]
                nodeTwoString = paramList[1]
                
                nodeOne = getNodeFromString(app, nodeOneString)
                if nodeOne == None:
                    return error
                nodeTwo = getNodeFromString(app, nodeTwoString)
                if nodeTwo == None:
                    return error

                color = 'brown'
                
                if nodeOne.isGroundNode() or nodeTwo.isGroundNode():
                    color = 'black'
                elif nodeOne.isPowerNode() or nodeTwo.ispowerNode():
                    color = 'red'

                app.components.append(Wire(nodeOne, nodeTwo, color))
                
                return executed
            # This may seem like repeated code but it is user protection in
            # case they do or do not delete the final comma
            if len(paramList) == 2:
                nodeOneString = paramList[0]
                nodeTwoString = paramList[1]
                
                nodeOne = getNodeFromString(app, nodeOneString)
                if nodeOne == None:
                    return error
                nodeTwo = getNodeFromString(app, nodeTwoString)
                if nodeTwo == None:
                    return error

                color = 'brown'
                
                if nodeOne.isGroundNode() or nodeTwo.isGroundNode():
                    color = 'black'
                elif nodeOne.isPowerNode() or nodeTwo.ispowerNode():
                    color = 'red'

                app.components.append(Wire(nodeOne, nodeTwo, color))
                
                return executed
            else:
                return error

    # Completely resets the breadboard.
    # This command nearly entirely resets the app as I want the user to be able
    # to have a complete reset available if they need it.
    if command in {'reset', 'clear','deleteboard'}:
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
                                     documentationStorage(2), 'Commands', 
                                     pistachio)
        app.drawingButton = Button(app.width * (3.75 / 5) + 5, 
                                   app.height * (4.5 / 5) + 5,
                                   app.width * (4.35 / 5) - 5, app.height - 5, 
                                   documentationStorage(3), 'Drawing', maroon)
        app.displayButton = Button(app.width * (4.35 / 5) + 5, 
                                   app.height * (4.5 / 5) + 5,
                                   app.width - 5, app.height- 5, 
                                   documentationStorage(4), 'Display', color)
        app.namesSet = set()
        app.nextCapacitorNumber = 1
        app.nextResistorNumber = 1
        app.display = ''
        app.totalResistance = 0
        app.totalCapacitance = 0
        app.circuitCurrent = 0
        app.circuitVoltage = 0
        # app.displayStorage = [] # I have opted to not reset the display storage
                                  # however that may be something that should be
                                  # considered / wanted by others so I have left
                                  # it commented
        app.drawing = None
        app.graph = {}

        return executed
    
    # Runs analysis on the circuit
    elif command in {'runanalysis', 'run', 'execute'}:
        result = runAnalysis(app, app.components, app.time)
        if result != "Analysis Complete":
            app.display = result
        return executed
    
    # Command to add a resistor to the circuit
    elif command in {'addresistor','addr'}:
        paramList = params.split(',')
        if len(paramList) == 3: # no name given
            
            nodeOneString = paramList[0]
            nodeTwoString = paramList[1]
            resistanceString = paramList[2]
            
            nodeOne = getNodeFromString(app, nodeOneString)
            if nodeOne == None:
                return error
            nodeTwo = getNodeFromString(app, nodeTwoString)
            if nodeTwo == None:
                return error
            
            if '.' in resistanceString:
                return error
            else:
                resistance = int(resistanceString)

            name = f'R{app.nextResistorNumber}'
            while True:
                if name in app.namesSet:
                    app.nextResistorNumber += 1
                    name = f'R{app.nextResistorNumber}'
                else:
                    break
            app.nextResistorNumber += 1
            app.namesSet.add(name)

            app.components.append(Resistor(nodeOne, nodeTwo, name, resistance))

            return executed

        elif len(paramList) == 4: # name given
            nodeOneString = paramList[0]
            nodeTwoString = paramList[1]
            resistanceString = paramList[2]
            name = paramList[3]
            
            nodeOne = getNodeFromString(app, nodeOneString)
            if nodeOne == None:
                return error
            nodeTwo = getNodeFromString(app, nodeTwoString)
            if nodeTwo == None:
                return error
            
            if '.' in resistanceString:
                return error
            else:
                resistance = int(resistanceString)

            if name in app.namesSet:
                return error
            else:
                app.namesSet.add(name)

            app.components.append(Resistor(nodeOne, nodeTwo, name, resistance))
            
            return executed
        
        else:
            return error
    
    # Command to add a Capacitor to the circuit.
    elif command in {'addcapacitor', 'addc'}:
        paramList = params.split(',')
        if len(paramList) == 3: # no name given
            
            nodeOneString = paramList[0]
            nodeTwoString = paramList[1]
            capacitanceString = paramList[2]
            
            nodeOne = getNodeFromString(app, nodeOneString)
            if nodeOne == None:
                return error
            nodeTwo = getNodeFromString(app, nodeTwoString)
            if nodeTwo == None:
                return error
            
            if '.' in capacitanceString:
                return error
            else:
                capacitance = int(capacitanceString)

            name = f'C{app.nextCapacitorNumber}'
            while True:
                if name in app.namesSet:
                    app.nextCapacitorNumber += 1
                    name = f'C{app.nextCapacitorNumber}'
                else:
                    break
            app.nextCapacitorNumber += 1
            app.namesSet.add(name)

            app.components.append(Capacitor(nodeOne, nodeTwo, name, capacitance))

            return executed

        elif len(paramList) == 4: # name given
            nodeOneString = paramList[0]
            nodeTwoString = paramList[1]
            resistanceString = paramList[2]
            name = paramList[3]
            
            nodeOne = getNodeFromString(app, nodeOneString)
            if nodeOne == None:
                return error
            nodeTwo = getNodeFromString(app, nodeTwoString)
            if nodeTwo == None:
                return error
            
            if '.' in resistanceString:
                return error
            else:
                resistance = int(resistanceString)

            if name in app.namesSet:
                return error
            else:
                app.namesSet.add(name)

            app.components.append(Resistor(nodeOne, nodeTwo, name, resistance))
            
            return executed
        
        else:
            return error

    # Command to remove a specific component
    elif command in {'remove'}:
        paramList = params.split(',')
        if len(paramList) == 1:
            if paramList[0] == '':
                return error
            else:
                name = paramList[0]
                if name in app.namesSet:
                    for component in app.components:
                        if (component.getName() == name):
                            app.components.remove(component)
                            app.namesSet.remove(name)
                            app.graph = {}
                            node1 = component.getStartNode()
                            node2 = component.getEndNode()
                            node1.assignComponent(None)
                            node2.assignComponent(None)
                            
                            return executed

                else:
                    return error
        else:
            for param in paramList:
                if param == '':
                    continue
                else:
                    name = param
                    if name in app.namesSet:
                        for component in app.components:
                            if (not isinstance(component, Wire) 
                                and component.getName() == name):
                                app.components.remove(component)
    
    # Command to add a wire to the circuit
    elif command in {'addwire'}:
        paramList = params.split(',')
        if len(paramList) == 2:
            nodeOneString = paramList[0]
            nodeTwoString = paramList[1]
            
            nodeOne = getNodeFromString(app, nodeOneString)
            if nodeOne == None:
                return error
            nodeTwo = getNodeFromString(app, nodeTwoString)
            if nodeTwo == None:
                return error

            color = 'brown'
                
            if nodeOne.isGroundNode() or nodeTwo.isGroundNode():
                color = 'black'
            elif nodeOne.isPowerNode() or nodeTwo.ispowerNode():
                color = 'red'

            app.components.append(Wire(nodeOne, nodeTwo, color))
            
            return executed
        else:
            return error

    # Command to set the voltage to a specific level
    elif command in {'setVoltage','voltage','v'}:
        paramList = params.split(',')
        if len(paramList) == 1: # no side given
            if paramList[0].isdigit():
                node = app.breadboard[1]['L']['+']
                node.setVoltage(int(paramList[0]))
                node = app.breadboard[1]['R']['+']
                node.setVoltage(int(paramList[0]))
                return executed
            else:
                return error
        elif len(paramList) == 2: # side given
            if paramList[0] == 'L':
                if paramList[1].isdigit():
                    node = app.breadboard[1]['L']['+']
                    node.setVoltage(int(paramList[1]))
                    return executed
                else:
                    return error
            elif paramList[0] == 'R':
                if paramList[1].isdigit():
                    node = app.breadboard[1]['R']['+']
                    node.setVoltage(int(paramList[1]))
                    return executed
                else:
                    return error
            elif paramList[0].isdigit():
                if paramList[1] == 'L':
                    node = app.breadboard[1]['L']['+']
                    node.setVoltage(int(paramList[0]))
                    return executed
                
                elif paramList[1] == 'R':
                    node = app.breadboard[1]['R']['+']
                    node.setVoltage(int(paramList[0]))
                    return executed

    # Command to change the time
    elif command in {'settime','time','swaptime'}:
        paramList = params.split(',')
        if len(paramList) == 1:
            if paramList[0] == '' or paramList[0] == ' ':
                if app.time == 0:
                    app.time = 5
                else:
                    app.time = 0

                return executed
            else:
                if paramList[0].isdigit():
                    if paramList[0] == '0':
                        app.time = 0
                    else:
                        app.time = 5

                    return executed
                else:
                    return error

    # Command to display a certain element of the simulation
    elif command in {'display', 'disp'}:
        app.display = ''
        paramList = params.split(',')
        for param in paramList:
            if param == 'circuit':
                app.display = f'''
                Thevenin:
                Voltage = {app.circuitVoltage} V
                Current = {app.circuitCurrent} Amps
                Resistance = {app.totalResistance} Ohms
                Capacitance = {app.totalCapacitance} F
                '''

            elif param in {'time'}:
                app.display = f'''
                Current Time = {app.time} Tao
                '''
            elif param in app.namesSet:
                name = param
                for component in app.components:
                    if component.getName() == name:
                        if isinstance(component, Capacitor):
                            app.display = f'''
                            {name}:
                            Voltage Drop = {component.getVoltage()} V
                            Capacitance = {component.getCapacitance()} F
                            Current = {component.getCurrent()} Amps
                            '''
                        elif isinstance(component, Resistor):
                            app.display = f'''
                            {name}:
                            Voltage Drop = {component.getVoltage()} V
                            Resistance = {component.getResistance()} Ohms
                            Current = {component.getCurrent()} Amps
                            '''
                        else:
                            pass #implement in future perhaps

            else:
                return error

    # Command to store the display
    elif command in {'store'}:
        app.displayStorage.append(app.display)
        return executed

    # Command to initiate drawing of Resistors
    elif command in {'drawresistor'}:
        app.drawing = 1
        return executed

    # Command to initiate drawing of Capacitors
    elif command in {'drawcapacitor'}:
        app.drawing = 2
        return executed

    # Command to initiate drawing of Wires
    elif command in {'drawwire'}:
        app.drawing = 3
        return executed

    return error