

def loadGraph(edgeFilename):
    '''This function reads a graph from a file where each line contains two vertices 'a' and 'b' representing an edge from 'a' to 'b'.
    It constructs an adjacency list, where for each vertex 'a', all its neighbors 'b' are collected in a list.
    This adjacency list representation of the graph is used to efficiently find the neighbors of each vertex during the breadth-first search algorithm.'''
    graph = {}
    with open(edgeFilename, 'r') as f:
        for line in f:
            a, b = map(str, line.strip().split())
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)
        for vertex in graph:
            graph[vertex].sort()
        return graph

filename = 'edgesshort_2_2_2.txt'

contents = loadGraph(filename)

class MyQueue:
    '''Basic Queue implementation, enqueue adds item to end of queue, dequeue removes and retuirns the item from the front of the queue, is_emtpy returns True
    if queue is empty, False otherwise, __str()__ returns a string representation of the queue for debugging.'''
    def __init__(self):
        #initializes empty list 'items'
        self.items = []

    def enqueue(self, item):
        #adds items to the end of 'items' queue
        self.items.append(item)

    def dequeue(self):
        #removes and returns first 'items' from front of queue
        return self.items.pop(0)

    def is_empty(self):
        #retuns true if empty and false otherwise
        return len(self.items) == 0

    def __str__(self):
        #returns string representation of 'items' for easy debugging
        return str(self.items)

iterations = 0  # will keep track of iterations

def bfs(graph, vertex):
    '''Preforms Breadth-First Search from a starting vertex to find shortest distance to all other vertices in the graph.
    Returns a dictionary where keys are vertices and values are their distances from the starting vertex, also counts number of iterations and outputs it every 1000 iterations.'''
    global iterations
    visted_set = set()
    queue = MyQueue()
    distance = {}
    visted_set.add(vertex)
    queue.enqueue((vertex, 0)) #enqueue tuple

    while not queue.is_empty():
        if iterations % 1000 == 0: #prints message every 1000 iterations
            print(f"Iteration: {iterations}")
        iterations += 1

        v, d = queue.dequeue() #dequeue tuple
        distance[v] = d
        for neighbor in graph.get(v, []):
            if neighbor not in visted_set:
                visted_set.add(neighbor)
                queue.enqueue((neighbor, d + 1)) #updates distance for neighbors

    return distance

def allNodeDistances(graph):
    '''Calculates distances from each vertex to every other vertex in the graph.
    Returns a dictionary where keys are starting vertices and values are dictionaries of distances to other vertices.'''
    all_distances = {}
    for vertex in graph:
        distances = bfs(graph, vertex)
        all_distances[vertex] = distances
    return all_distances

def distanceDistribution(G):
    '''Computes distribution and percentage distribution of distances in the graph.
    Returns two dictionaries that represent the distribution and percentage distribution of distances.
    G is a dictionary that represents distances from each vertex to every other vertex on the graph.'''
    distribution = {}
    total_distances = 0  #to count total distances for calculating percentage
    for vertex, distances in G.items():
        for distance in distances.values():
            distribution[distance] = distribution.get(distance, 0) + 1
            total_distances += 1

    #calculating percentage distribution
    percentage_distribution = {}
    for distance, count in distribution.items():
        percentage_distribution[distance] = (count / total_distances) * 100

    return distribution, percentage_distribution


# all_distances = allNodeDistances(contents)
# distribution, percentage_distribution = distanceDistribution(all_distances)

# print(f"All Distances: {all_distances}")
# print(f"Distance Distribution: {distribution}")
# print(f"Percentage Distance Distribution: {percentage_distribution}")

def test_large_file():
    '''Test function for the large text file, it calculates the distance distribution and outputs the percentage distribution.'''
    global iterations
    filename = 'edges_2_2.txt'
    large_contents = loadGraph(filename)
    all_distances = allNodeDistances(large_contents)
    large_distribution, large_percentage_distribution = distanceDistribution(all_distances)
    print(large_percentage_distribution)

test_large_file()

'''This network does not satisfy the small world problem because it shows there are 9 degrees of seperation instead of 6.'''