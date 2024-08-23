class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []  # Store the resulting MST
        i, e = 0, 0  # Index variables for sorted edges and result
        self.graph = sorted(self.graph, key=lambda item: item[2])  # Sort edges based on weight

        parent = []
        rank = []

        # Initialize parent and rank arrays
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Process edges in sorted order
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)

            # If including this edge does not form a cycle
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)

        # Print the resulting MST
        for u, v, weight in result:
            print("Edge: {} - {} Weight: {}".format(u, v, weight))

# Driver code
g = Graph(5)
g.add_edge(0, 1, 8)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, 9)
g.add_edge(1, 3, 11)
g.add_edge(2, 3, 15)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 7)

g.kruskal()
