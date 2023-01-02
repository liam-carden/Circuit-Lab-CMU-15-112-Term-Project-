# calculates the total resistance of a parallel system
# Uses the equation 1/Rt = 1/R1 + ... + 1/Rn
# returns Rt
def parallelResistanceCalc(graph, startResistor, endResistor):
    summy = 0
    subSummy = 0
    for resistor in graph[startResistor]:
        while resistor != endResistor:
            subSummy += resistor.getResistance()
            nextResistor = graph[resistor][0]
            resistor = nextResistor
        summy += (subSummy)**(-1)
        subSummy = 0
    return (summy)**(-1)