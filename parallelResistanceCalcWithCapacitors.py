from Capacitor import *

# calculates the resistance of a parallel system that contains capacitors
# Uses the equation 1/Rt = 1/R1 + ... + 1/Rn
# returns Rt
def parallelResistanceCalcWithCapacitors(subDataStructure):
    summy = 0
    subSummy = 0
    for chain in subDataStructure:
        for component in chain:
            if not isinstance(component, Capacitor):
                subSummy += component.getResistance()
        if subSummy != 0:
            summy += (subSummy)**(-1)
        subSummy = 0
    if summy == 0:
        return 0
    return (summy)**(-1)