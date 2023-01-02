from Capacitor import *

#* returns True if the circuit contains no capacitors, False otherwise
# looks through components and checks if any of them are capacitors
def containsNoCapacitors(components):
    for component in components:
        if isinstance(component, Capacitor):
            return False
    return True