# returns a list of the new components in graph
def getNewComponents(graph):
    s = set()
    for key in graph:
        for value in graph[key]:
            s.add(value)
        s.add(key)

    return list(s)