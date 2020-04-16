"""
Simple graph implementation
"""
# from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        # TODO
        if vertex in self. vertices:
            print(f'Vertex {vertex} already exsits.')
        else:
            self.vertices[vertex] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2.
        """
        if v1 not in self.vertices:
            print(f'Vertice {v1} is not found.')
        elif v2 not in self.vertices:
            print(f'Vertice {v2} is not found.')
        else:
            self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        neighbors = []
        if vertex_id in self.vertices:
            neighbors = list(self.vertices[vertex_id])
        return neighbors


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        paths = [starting_vertex]
        visited = set()

        while paths:
            vertex = paths.pop(0)
            ### Do something when the vertex is visited.
            print(vertex)
            visited.add(vertex)

            for neighbor in self.get_neighbors(vertex):
                if neighbor in visited:
                    continue
                paths.append(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        paths = [[starting_vertex]]
        visited = []

        while paths:
            path = paths.pop(0)
            vertex = path[-1]
            if vertex in visited:
                continue
            # Do something when the vertex is visited.
            print(vertex)
            visited.append(vertex)

            for i, neighbor in enumerate(self.get_neighbors(vertex)):
                path_new = path.copy()
                path_new.append(neighbor)
                # paths.insert(0, path_new) # [1,2,4,7,6,3,5]
                paths.insert(i, path_new)   # [1,2,3,5,4,6,7]


    def dft_recursive(self, starting_vertex, visited=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if starting_vertex in visited:
            return
        # Do something when the vertex is visited.
        print(starting_vertex)
        visited.append(starting_vertex)

        for vertex in self.get_neighbors(starting_vertex):
            self.dft_recursive(vertex, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        paths = [starting_vertex]
        visited = []

        while paths:
            vertex = paths.pop(0)
            visited.append(vertex)
            if vertex == destination_vertex:
                return visited

            for neighbor in self.get_neighbors(vertex):
                if neighbor in visited:
                    continue
                paths.append(neighbor)


    def bfs_shortest(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """        
        paths = [[starting_vertex]]
        visited = []

        while paths:
            path = paths.pop(0)
            vertex = path[-1]
            if vertex in visited:
                continue
            visited.append(vertex)

            if vertex == destination_vertex:
                return path

            for i, neighbor in enumerate(self.get_neighbors(vertex)):
                path_new = path.copy()
                path_new.append(neighbor)
                paths.append(path_new)
            

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        paths = [[starting_vertex]]
        visited = []

        while paths:
            path = paths.pop(0)
            vertex = path[-1]
            if vertex in visited:
                continue
            visited.append(vertex)

            if vertex == destination_vertex:
                return visited

            for i, neighbor in enumerate(self.get_neighbors(vertex)):
                path_new = path.copy()
                path_new.append(neighbor)
                paths.insert(0, path_new) # [1,2,4,7,6,3,5]
                # paths.insert(i, path_new)   # [1,2,3,5,4,6,7]

            # print(f'visited: {visited}')
            # print(f'paths: {paths}')


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # print(f'visited: {visited}')
        if starting_vertex in visited or destination_vertex in visited:
            return visited
        visited.append(starting_vertex)

        for vertex in self.get_neighbors(starting_vertex):
            visited = self.dfs_recursive(vertex, destination_vertex, visited)

        return visited


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    # https://raw.githubusercontent.com/Nov05/pictures/master/pic001/Sketch.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 6)
    graph.add_edge(4, 7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(7, 6)

    print('graph:', graph.vertices)
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''

    print('bft:')
    graph.bft(1)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''

    print('dft:')
    graph.dft(1)
    print('dft_recursive:')
    graph.dft_recursive(1)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''

    print('bfs:', graph.bfs(1, 6))
    '''
    Valid BFS path:
        [1, 2, 4, 6]
        [1, 2, 3, 4, 5, 6]
    '''

    print('bfs_shortest:', graph.bfs_shortest(1, 6))
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''

    print('dfs:', graph.dfs(1, 6))
    print('dfs_recursive:', graph.dfs_recursive(1, 6))
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
        [1, 2, 3, 5, 4, 6]
    '''
    print('dfs_recursive:', graph.dfs_recursive(1, 2, visited=[]))