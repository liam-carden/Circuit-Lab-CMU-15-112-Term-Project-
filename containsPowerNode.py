
#* returns True if the circuit contains a connection to a power node, False otherwise
# looks through components and checks if any of the components are power components
def containsPowerNode(components):
    for component in components:
        if component.isPowerComponent():
            return True
    return False