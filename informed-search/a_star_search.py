from collections import defaultdict
from queue import PriorityQueue

# Graph data
data = defaultdict(list)
data['A'] = ['B', 2, 'C', 1, 'D', 3, 6]
data['B'] = ['E', 5, 'F', 4, 3]
data['C'] = ['G', 6, 'H', 3, 4]
data['D'] = ['I', 2, 'J', 4, 5]
data['E'] = [3]
data['F'] = ['K', 2, 'L', 1, 'M', 4, 1]
data['G'] = [6]
data['H'] = ['N', 2, 'O', 4, 2]
data['I'] = [5]
data['J'] = [4]
data['K'] = [2]
data['L'] = [0]
data['M'] = [4]
data['N'] = [0]
data['O'] = [4]


# Node class
class Node:
    def __init__(self, name, par=None, g=0, h=0):
        self.name = name
        self.par = par
        self.g = g
        self.h = h

    def display(self):
        print(self.name, self.g, self.h)

    def __lt__(self, other):
        if other is None:
            return False
        return self.g + self.h < other.g + other.h

    def __eq__(self, other):
        if other is None:
            return False
        return self.name == other.name


# Check if goal node is reached
def equal(O, G):
    return O.name == G.name


# Check if a node is in the priority queue
def checkInPriority(tmp, c):
    return tmp in c.queue if tmp else False


# Get the path from start to goal
def getPath(O):
    if O.par is not None:
        getPath(O.par)
    print(O.name, end=" ")  # Print path in order


# A* Algorithm
def AStar(S=Node('A'), G=Node('N')):
    frontier = PriorityQueue()
    explored = PriorityQueue()
    S.h = data[S.name][-1]
    frontier.put(S)

    while True:
        if frontier.empty():
            print("Error: No path found!")
            return
        
        O = frontier.get()
        explored.put(O)
        print("Exploring:", O.name, "g =", O.g, "h =", O.h)

        if equal(O, G):
            print("Search successful!")
            print("Path:", end=" ")
            getPath(O)
            print("\nTotal Distance:", O.g + O.h)
            return

        i = 0
        while i < len(data[O.name]) - 1:
            name = data[O.name][i]
            g = O.g + data[O.name][i + 1]
            h = data[name][-1]
            tmp = Node(name=name, g=g, h=h, par=O)

            if not checkInPriority(tmp, frontier) and not checkInPriority(tmp, explored):
                frontier.put(tmp)

            i += 2


# Main function to run the algorithm
if __name__ == "__main__":
    print("Starting A* search from A to N:")
    AStar()