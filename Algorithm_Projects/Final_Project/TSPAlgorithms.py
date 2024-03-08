import networkx as nx
import random

class TSPAlgorithms:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.graph = None
        self.coordinates = None

    def nearest_neighbor_tour(self):
        start_city = random.choice(list(self.graph.nodes()))
        current_city = start_city
        tour = [current_city]
        unvisited_cities = set(self.graph.nodes())
        unvisited_cities.remove(current_city)
        
        while unvisited_cities:
            nearest_city = min(unvisited_cities, key=lambda city: self.graph[current_city][city]['weight'])
            tour.append(nearest_city)
            unvisited_cities.remove(nearest_city)
            current_city = nearest_city
        
        tour.append(start_city)
        return tour

    def christofides_tour(self):
        mst = nx.minimum_spanning_tree(self.graph)
        odd_degree_vertices = [v for v in mst.nodes() if mst.degree(v) % 2 != 0]
        perfect_matching = nx.max_weight_matching(mst, maxcardinality=True)
        multigraph = mst.copy()
        for u, v in perfect_matching:
            multigraph.add_edge(u, v, weight=self.graph[u][v]['weight'])
        
        eulerian_multigraph = nx.eulerize(multigraph)
        eulerian_circuit = list(nx.eulerian_circuit(eulerian_multigraph))
        
        tour = [eulerian_circuit[0][0]]
        for u, v in eulerian_circuit:
            if v not in tour:
                tour.append(v)
        
        tour.append(tour[0])
        return tour

    def calculate_tour_length(self, tour):
        tour_length = sum(self.graph[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
        return tour_length
