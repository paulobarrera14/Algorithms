# graphColor Backtracking
class MyStack(object):
    def __init__(self, type): # Creates an empty list
        self.elemType = type
        self.state = [] # Empty list
    def __str__(self): # for print
        return str(self.state)
    def empty(self):
        return len(self.state) == 0
    def push(self, elem): # Adds an element to the top of a stack
        assert type(elem) == self.elemType
        self.state.append(elem)
    def pop(self): # Removes an element from the top of the stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state.pop()
    def top(self): # Returns the top of a nonempty stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]

def isFeasible(nodeColors, currentNode, color, graph):
    '''This function checks if it is feasible to color a given node with a particular color, this color depends on the current color assignments of other nodes'''
    for adj in range(len(graph[currentNode])):
        if graph[currentNode][adj] and nodeColors[adj] == color:
            return False
    return True

def graphColoring(graph, colors):
    '''This function initiates the backtracking process and manages the stack'''
    n = len(graph) # Number of nodes
    nodeColors = [None] * n # Initial empty state

    # Create a stack for DFS
    s = MyStack(list)
    s.push(nodeColors.copy()) # Empty color assignment

    while not s.empty(): # While the stack is not empty do:
        currentState = s.pop()
        currentNode = len([color for color in currentState if color is not None])

        # Check if a complete coloring is found
        if currentNode == n:
            print(currentState)  # Print the solution
            break  # Stop after finding the first solution

        for color in colors:
            if isFeasible(currentState, currentNode, color, graph):
                newState = currentState.copy()
                newState[currentNode] = color
                s.push(newState)

graph = [[False, True, False, False, False, True],
         [True, False, True, False, False, True],
         [False, True, False, True, True, False],
         [False, False, True, False, True, False],
         [False, False, True, True, False, True],
         [True, True, False, False, True, False]]
colors = ['r', 'g', 'b']

graphColoring(graph, colors)

# Output ['b', 'g', 'b', 'r', 'g', 'r']