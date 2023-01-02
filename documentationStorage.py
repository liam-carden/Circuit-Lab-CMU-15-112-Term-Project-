# stores the multiline strings that contain documentation
# returns the documentation that is requested
# 1 = Guidelines
# 2 = Commands
# 3 = Drawing
# 4 = Display
def documentationStorage(documentationNum):
    documentation1 = '''
    Guidelines:
    
    1. Do not connect more than 1 component to each node.
    2. Do not build circuits that have multiple layers of parallel, condense the 
       circuit into singular layers of parallel with components in that layer 
       connected in series only.
    3. Commands / Functions that the user inputs are not case sensitive, the 
       parameters within them are case sensitive.
    4. After any change to a circuit is made 'run' will need to be called again 
       inorder to reanalyse the circuit.
    5. Wires in this simulation have a resistance of 1^-14. This may lead to 
       some values being off due to the built in rounding.
    6. After typing in the command you wish to use hit enter.
    7. Do not include '' with your command inputs, this is merely for 
       documentation purposes.
    8. Some commands have alternate inputs that can be used these will be 
       included in [] after their description.
    9. All resistance, capacitance, and time values should be integers.
    10. Nodes should be given as the row number and column letter. If the node 
        is a power or ground node include 
        + or - as the column respectively and also include either L or R to 
        indicate the left or right side of the breadboard.
    '''
    documentation2 = '''
    Commands:
    
    'reset' -> resets the breadboard completely. ['clear','deleteboard']
    'run' -> Completes a full analysis of the circuit and it's components. 
             ['runanalysis', 'execute'] User can also press 'Tab' key to run.
    'addResistor(node1, node2, resistance, name)' -> adds a resistor at the 
                specified nodes with the given resistance and name. If no name 
                is given a name will be assigned. ['addr']
    'addCapacitor(node1, node2, capacitance, name)' -> adds a capacitor at the 
                 specified nodes with the given capacitance and name. 
                 If no name is given a name will be assigned. ['addc']
    'remove(name)' -> removes a component from the breadboard given the name of 
                      that component.
    'addWire(node1, node2)' -> adds a wire to the breadboard at the specified 
                               nodes.
    'setVoltage(voltage value, side)' -> sets the voltage of one or both power 
               bars to be a new specified voltage. If no side argument is given 
               then both sides will be set to that voltage. Side arguments are 
               either 'L' or 'R' for left and right.['voltage', 'v']
    'time(newTime)' -> sets the time to newTime (0 or 5) or simply swaps the 
                       time to the other (of 0 and 5) if no input is given. 
                       ['settime','swaptime']
    'display(component)' -> displays information about a given component or the 
                            circuit if 'circuit' is passed as the component. Can 
                            also display the current time if 'time' is passed 
                            as the component. ['disp']
    'store' -> stores whatever is currently in the display in the storage boxes 
               to the right. More information in display section.
    'draw___' -> allows the user to select nodes to draw components. See draw 
                 section for more details.
    '''

    documentation3 = '''
    Drawing:
    
    Drawing acts as a way for users to select the component they would like to 
    draw and then simply select the nodes they wish to connect with the 
    component. To begin enter the command 'drawResistor', 'drawCapacitor', or 
    'drawWire' depending on the type of component you would like to draw.

    This will place the node location into the command bar as well as a comma. 
    After selecting the two nodes, input the value you would like for the 
    component. For resistors this should be an integer resistance for capacitors
    an integer capacitance. For wires do not input any value.

    Once this value is typed in press 'Enter' and see the component being drawn.

    An important note is that while in draw mode no other commands will work. 
    Inorder to preform another command the user will need to input 'stopDrawing'
    as a command. This allows the user to remove a component or simply start 
    drawing a different type of component as is outlined here.

    When drawing you are unable to input a different name than the default names 
    for components. If you would like to give a component a specific name then 
    use the regular commands.
    '''

    documentation4 = '''
    Display:

    Using the 'display' command the user is able to display information about a 
    component, time, or entire circuit based on the last time the circuit was 
    run. The next layer of this is the 'store' command.
    
    The 'store' command stores any information that is currently being displayed
    in the four storage boxes the right of the breadboard. 

    This allows the user to store up to 4 displays of information at a time. 
    This means the user is able to compare componets, compare entire circuits, 
    or compare components across different time values.
    '''

    if documentationNum == 1:
        return documentation1
    elif documentationNum == 2:
        return documentation2
    elif documentationNum == 3:
        return documentation3
    elif documentationNum == 4:
        return documentation4