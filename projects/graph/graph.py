"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # get an id, given by input, for the vertex and store in a set
        self.vertices[vertex_id] = set() # key is ???

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if both verts you're trying to link exist
        if v1 in self.vertices and v2 in self.vertices:
            # add an edge between them
            self.vertices[v1].add(v2)
        else:
            # if not, throw error
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        seen = set()

        q.enqueue(starting_vertex)

        # while q is not empty
        while q.size() > 0:
            v = q.dequeue()

            if v not in seen:
                print(v)

                seen.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack()
        seen = set()

        q.push(starting_vertex)

        # while q is not empty
        while q.size() > 0:
            # store the last vertex taken off stack in v
            v = q.pop()
            # print(f"this is v: {v}")

            # if v has not been seen 
            if v not in seen:
                 
                print(v)
                
                # mark it as seen
                seen.add(v)
                
                # loop though all of v's neighbors 
                for neighbor in self.get_neighbors(v):
                    # and push them to the stack
                    q.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # q = Stack()
        # seen = set()

        # q.push(starting_vertex)
        # base case

        # recursive case

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
		# Create a Set to store visited vertices
        seen = set()

		# While the queue is not empty...
        while q.size() > 0:    
			# Dequeue the first PATH
            v = q.dequeue()
			# Grab the last vertex from the PATH
            last_v = v[-1]
			# If that vertex has not been visited...
            if last_v not in seen:
				# CHECK IF IT'S THE TARGET
                if last_v == destination_vertex:
				  # IF SO, RETURN PATH
                    return v
				# Mark it as visited...
                else:
                    seen.add(last_v)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_v):
				  # COPY THE PATH
				  # APPEND THE NEIGHOR TO THE BACK
                    new_path = v + [neighbor] # this does both

                    q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and enqueue A PATH TO the starting vertex ID
        q = Stack()
        q.push([starting_vertex])
		# Create a Set to store visited vertices
        seen = set()
		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            v = q.pop()
			# Grab the last vertex from the PATH
            last_v = v[-1]
			# If that vertex has not been visited...
            if last_v not in seen:
				# CHECK IF IT'S THE TARGET
                if  last_v == destination_vertex:
				    # IF SO, RETURN PATH
                    return v
				# Mark it as visited...
                else:
                    seen.add(last_v)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_v):
				    # COPY THE PATH
				    # APPEND THE NEIGHOR TO THE BACK
                    new_path = v + [neighbor]

                    q.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
