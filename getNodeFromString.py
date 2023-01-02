# takes in a string that corresponds to some node and returns the node object
# that the location corresponds to
def getNodeFromString(app, nodeString):
    # power nodes
    if '+' in nodeString:
        rowString = ''
        side = ''
        for char in nodeString:
            if char.isalpha():
                side = char
            elif char.isdigit():
                rowString = rowString + char

        row = int(rowString)
        if row < 1 or row > 15:
            return None
        
        if side == 'L' or side == 'R':
            return app.breadboard[row][side]['+']
        else:
            return None

    # ground nodes
    elif '-' in nodeString:
        rowString = ''
        side = ''
        for char in nodeString:
            if char.isalpha():
                side = char
            elif char.isdigit():
                rowString = rowString + char

        row = int(rowString)
        if row < 1 or row > 15:
            return None
        
        if side == 'L' or side == 'R':
            return app.breadboard[row][side]['-']
        else:
            return None
    
    # bar nodes
    else:
        rowString = ''
        col = ''
        
        for char in nodeString:
            if char.isalpha():
                col = char
            elif char.isdigit():
                rowString = rowString + char

        row = int(rowString)
        if row < 1 or row > 15:
            return None

        if col in {'a','b','c','d','e'}:
            return app.breadboard[row]['L'][col]
        elif col in {'f','g','h','i','j'}:
            return app.breadboard[row]['R'][col]
        else:
            return None