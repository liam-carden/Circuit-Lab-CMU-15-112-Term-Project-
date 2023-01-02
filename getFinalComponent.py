
#* returns the final component of the circuit
# iterates through the graph and its components and finds the connection that
# is itself not a key in the graph 
def getFinalComponent(graph):
    for component in graph:
        for connection in graph[component]:
            if connection not in graph:
                return connection