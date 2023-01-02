# determines whether the circuit is entirely in series or not
# returns True if the circuit is entirely in series
# returns False if the circuit contains parallel components
# the graph of an entire series circuit will look like:
# {1:[2],2:[3],3:[4]}
def allInSeries(graph):
    for component in graph:
        if len(graph[component]) > 1:
            return False
    return True