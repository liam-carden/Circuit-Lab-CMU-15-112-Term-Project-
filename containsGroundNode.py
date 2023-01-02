
#* returns True if the circuit contains a connection to a ground node, False otherwise
# looks through components and checks if any of the components are ground components
def containsGroundNode(components):
    for component in components:
        if component.isGroundComponent():
            return True
    return False