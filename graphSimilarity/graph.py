import numpy as np

class Graph:
    'Simple class representing a graph'

    def __init__(self, num_vertices, edges):
        self.num_vertices = num_vertices
        self.edges = edges

    def get_num_vertices(self):
        return self.num_vertices

    def get_edges(self):
        return self.edges

    # currently undirected
    def compute_adjacency_matrix(self):
        adjacency_matrix = np.zeros((self.num_vertices, self.num_vertices))
        for edge in self.edges:
            i, j = edge
            adjacency_matrix[i, j] = 1
            adjacency_matrix[j, i] = 1

        self.adjacency_matrix = adjacency_matrix

    def get_adjacency_matrix(self):
        return self.adjacency_matrix