from GenerateGraph import GenerateGraph
from TSPAlgorithms import TSPAlgorithms
from PlotGraph import PlotGraph

# Experiment settings
num_cities_list = [5, 10, 15]  # Varying number of cities for experimentation

for num_cities in num_cities_list:
    print(f"Experimenting with {num_cities} cities:")
    generate_graph = GenerateGraph(num_cities)
    generate_graph.generate_random_graph()
    generate_graph.assign_random_weights()
    
    tsp_algorithms = TSPAlgorithms(num_cities)
    tsp_algorithms.graph = generate_graph.graph
    tsp_algorithms.coordinates = generate_graph.coordinates
    
    nn_tour = tsp_algorithms.nearest_neighbor_tour()
    nn_tour_length = tsp_algorithms.calculate_tour_length(nn_tour)
    
    print("Nearest Neighbor Tour:", nn_tour)
    print("Nearest Neighbor Tour Length:", nn_tour_length)
    
    christofides_tour = tsp_algorithms.christofides_tour()
    christofides_tour_length = tsp_algorithms.calculate_tour_length(christofides_tour)
    print("Christofides Tour:", christofides_tour)
    print("Christofides Tour Length:", christofides_tour_length)
    
    plot_graph = PlotGraph(generate_graph.graph, generate_graph.coordinates)
    plot_graph.plot_with_tours([nn_tour, christofides_tour], ['r', 'b'], ['Nearest Neighbor Tour', 'Christofides Tour'], num_cities)