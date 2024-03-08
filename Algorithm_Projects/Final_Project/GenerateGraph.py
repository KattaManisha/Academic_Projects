import numpy as np
import networkx as nx
import random

class GenerateGraph:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.graph = None
        self.coordinates = None

    def generate_random_graph(self):
        np.random.seed(42)
        coordinates = np.random.rand(self.num_cities, 2)
        distances = np.linalg.norm(coordinates[:, np.newaxis] - coordinates[np.newaxis, :], axis=-1)
        self.graph = nx.from_numpy_array(distances)
        self.coordinates = coordinates

    def assign_random_weights(self):
        for u, v in self.graph.edges():
            self.graph[u][v]['weight'] = random.randint(1, 100)
