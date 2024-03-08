import timeit
import csv
from tabulate import tabulate
import matplotlib.pyplot as plt
from SortingAlgorithms import SortingAlgorithms
from DataGenerator import DataGenerator

class PerformanceMeasurement:
    def measure_time(algorithm, input_data):
        start_time = timeit.default_timer()
        algorithm(input_data)
        return timeit.default_timer() - start_time

    def plot_graph(sizes, times_heap, times_quick, times_merge, times_radix, times_bucket, times_tim):
        plt.plot(sizes, times_heap, label='Heap Sort')
        plt.plot(sizes, times_quick, label='Quick Sort')
        plt.plot(sizes, times_merge, label='Merge Sort')
        plt.plot(sizes, times_radix, label='Radix Sort')
        plt.plot(sizes, times_bucket, label='Bucket Sort')
        plt.plot(sizes, times_tim, label='Tim Sort')
        plt.xlabel('Input Size')
        plt.ylabel('Execution Time (s)')
        plt.title('Sorting Algorithm Performance')
        
        plt.legend()
        plt.show()