import networkx as nx
import matplotlib.pyplot as plt

class PlotGraph:
    def __init__(self, graph, coordinates):
        self.graph = graph
        self.coordinates = coordinates
        self.pos = {i: coordinates[i] for i in range(len(coordinates))}

    def plot_with_tours(self, tours, tour_colors, tour_labels, num_cities):
        plt.figure(figsize=(8, 6))
        nx.draw(self.graph, self.pos, with_labels=True, node_size=300)
        for tour, color, label in zip(tours, tour_colors, tour_labels):
            nx.draw_networkx_edges(self.graph, self.pos, edgelist=[(tour[i], tour[i+1]) for i in range(len(tour) - 1)], edge_color=color, width=2, label=label)
        plt.title(f"Traveling Salesman Problem - Experiment for {num_cities} cities")
        plt.legend(loc='upper right')
        plt.show()
