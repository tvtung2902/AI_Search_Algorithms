def BFS (initState, goal):
    frontier = [initState]
    explored = []
    while frontier:
        state = frontier.pop(0)
        explored.append(state)
        if(state == goal): return explored
        for neighbor in graph[state]:
            if(neighbor not in (explored and  frontier)):
                frontier.append(neighbor)
    return False

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': ['J', 'K'],
        'F': ['L', 'M'],
        'G': ['N', 'O'],
        'H': [], 'I': [], 'J': [], 'K': [],
        'L': [], 'M': [], 'N': [], 'O': []
    }

    result = BFS('A', 'O')
    if result:
        s = 'explored: ' 
        for i in result:
            s += i + ' '
        print(s)
    else:
        print("404 Not Found!")