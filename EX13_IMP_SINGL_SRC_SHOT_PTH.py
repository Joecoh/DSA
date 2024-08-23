class Graph:
    def __init__(self, vertex, adjgraph):
        self.vertex = vertex
        self.adjgraph = adjgraph

    def minDistance(self, distance, selSource):
        min_distance = float('inf')
        min_index = -1
        for i in range(self.vertex):
            if not selSource[i] and distance[i] < min_distance:
                min_distance = distance[i]
                min_index = i
        return min_index

    def display(self, distance):
        print("0 is the source")
        for i in range(self.vertex):
            print("node 0-{} ---> {}".format(i, distance[i]))

    def dijkstra(self):
        distance = [float('inf')] * self.vertex
        distance[0] = 0
        selSource = [False] * self.vertex
        
        for _ in range(self.vertex):
            min_index = self.minDistance(distance, selSource)
            selSource[min_index] = True
            
            for j in range(self.vertex):
                if (self.adjgraph[min_index][j] > 0 and 
                    not selSource[j] and 
                    distance[j] > distance[min_index] + self.adjgraph[min_index][j]):
                    distance[j] = distance[min_index] + self.adjgraph[min_index][j]
        
        self.display(distance)

# Driver code
no_of_vertex = 6
adjgraph = [
    [0, 1, 0, 0, 3, 0],
    [1, 0, 2, 0, 1, 0],
    [0, 2, 0, 3, 0, 2],
    [0, 0, 3, 0, 0, 1],
    [3, 1, 0, 0, 0, 2],
    [0, 0, 2, 1, 2, 0]
]
obj = Graph(no_of_vertex, adjgraph)
obj.dijkstra()
