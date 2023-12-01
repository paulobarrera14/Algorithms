# Minimal Spanning Tree Algorithm
def extractMin(verts):
    minIndex = 0
    for v in range(1,len(verts)):
        if verts[v][1] < verts[minIndex][1]:
            minIndex = v
    return verts.pop(minIndex)

def mst(g):
    # Create a list of vertices and their current shortest distances
    # from vertex 0
    # [vertNum, dist]
    nVerts = len(g)
    vertsToProcess = [[i, float("inf"), -1] for i in range(nVerts)]
    # Start at vertex 0 - it has a current shortest distance of 0
    vertsToProcess[0][1] = 0
    # Start with an empty list of processed edges
    mstEdges = []
    while vertsToProcess:
        u = extractMin(vertsToProcess) # Finds vertex 'u' with smallest key value
        if u[2] != -1:
            mstEdges.append([u[0], u[2]]) # [current_vertex, parent_vertex]
        # Examine all potential verts remaining
        for v in range(nVerts):
            # Using list comprehension to find if vertex v is still in vertsToProcess
            inVertsToProcess = any(vert[0] == v for vert in vertsToProcess)
            # Check for edge from u[0] to v and if v is still unprocessed
            if graph[u[0]][v] > 0 and inVertsToProcess:
                v_index = next((index for index, vert in enumerate(vertsToProcess) if vert[0] == v), None)
                # Update the key (distance) if this edge is better
                if v_index is not None and graph[u[0]][v] < vertsToProcess[v_index][1]:
                    vertsToProcess[v_index][1] = graph[u[0]][v]  # Update key
                    vertsToProcess[v_index][2] = u[0]  # Update parent

    # This edge represents which vertex is the root
    mstEdges.insert(0, [0, -1])
    return mstEdges

# Adjacency matrix representation of a graph
# This particular graph is the one from the videos
# The vertices didn't have labels in the videos
# so I'm using the following vertex labels:
#   2
#  / \
# 3---1--7
# | \ |
# 4 | 0--6
#  \|/
#   5
graph = [[0, 7, 0, 0, 0, 10, 15, 0],
[7, 0, 12, 5, 0, 0, 0, 9],
[0, 12, 0, 6, 0, 0, 0, 0],
[0, 5, 6, 0, 14, 8, 0, 0],
[0, 0, 0, 14, 0, 3, 0, 0],
[10, 0, 0, 8, 3, 0, 0, 0],
[15, 0, 0, 0, 0, 0, 0, 0],
[0, 9, 0, 0, 0, 0, 0, 0]]
print(mst(graph))