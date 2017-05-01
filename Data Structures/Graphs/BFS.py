from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, parent, child):
        self.graph[parent].append(child)

    def BFS(self, root):

        queue = []
        visited = [False] * len(self.graph)
        parents = defaultdict(list)

        queue.append(root)

        visited[root] = True

        while queue:

            curr_parent = queue.pop(0)
            print(curr_parent, end=' ')

            for child in self.graph[curr_parent]:

                visited[curr_parent] = True

                if not visited[child]:
                    parents[child] = curr_parent
                    queue.append(child)
                    visited[child] == True

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


