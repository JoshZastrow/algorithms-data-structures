from collections import defaultdict
import sys

class Graph():

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def BFS(self, start):

        # Mark all vertices not visited
        visited = [False] * (len(self.graph))
        x = 0
        # Create a q
        q = []

        # mark the source node as visited
        q.append(start)
        visited[start] = True

        while q:

            # print the start node, remove from q
            start = q.pop(0)
            print(start, end=' ')

            # Get adjacent vertices of start node
            # if it hasn't been visited, visit it
            # add to the q
            for v in self.graph[start]:
                if visited[v] == False:
                    q.append(v)
                    visited[v] = True

class Vertex():

    def __init__(self, key):
        self.ID = key
        self.connectedTo = defaultdict(list)

    def addNeighbor(self,neighbor, weight):
        self.connectedTo[neighbor] = weight

    def connections(self):
        return self.connectedTo.keys()

    def __str__(self):
        return str(self.ID) + " : " + str([x.ID for x in self.connections])

    def weight(self, neighbor):
        return self.connectedTo[neighbor]

class Graph2():

    def __init__(self):
        self.vertices = {}
        self.count = 0

    def addVertex(self, key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        self.count += 1
        return new_vertex

    def getVertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertices

    def addEdge(self, parent, child, cargo):
        if parent not in self.vertices:
            pVertex = self.addVertex(parent)
        if child not in self.vertices:
            cVertex = self.addVertex(child)
        self.vertices[parent].addNeighbor(self.vertices[child], cargo)

    def Vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())


def test_Graph():

        # Driver code
    # Create a graph given in the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal (starting from vertex 2)")
    g.BFS(2)




test_Graph()


# Initialize a function to declare state of node
#   Visted, Visiting, Not Visited

# Function to return true/false if node is found
# Requires a graph object, start and end node

# Create a new linked list 'stack'

# for each node in the graph
#   set the nodes state to be unvisited

# set start node's state to being visited
# add node to stack

# create a node (u)
# while the stack is not empty:
#   remove the top of the stack to the node (u)

#   if the node is not None
#   for each node (v) adjacent to node (u)
#       if the state of node v is unvisited
#           if node v is the destination node
#               DING DING DING WE HAVE A WINNER
#           otherwise, mark this node as visited


def isRoute(curr_node, dest_node):
    '''
    Determines if there is a route between two nodes

    Methodology:
    Starting with one node, check if other node is found.
    Otherwise, mark node as visited and move to next node.
    '''

    if not curr_node:
        return false
    else:
        return isRoute(curr_node.next, dest_node)
