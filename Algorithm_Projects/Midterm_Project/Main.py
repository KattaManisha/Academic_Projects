import sys
import csv
from tabulate import tabulate
import matplotlib.pyplot as plt
from SortingAlgorithms import SortingAlgorithms
from DataGenerator import DataGenerator
from PerformanceMeasurement import PerformanceMeasurement
    
if __name__ == "__main__":
    sorting_algorithms = SortingAlgorithms()

    # Display options
    print("Choose an option:")
    print("1. n randomly chosen integers in the range [0...n]")
    print("2. n randomly chosen integers in the range [0...k], k < 1000")
    print("3. n randomly chosen integers in the range [0...n^3 ( n raised to 3)]")
    print("4. n randomly chosen integers in the range [0... log n]")
    print("5. n randomly chosen integers that are multiples of 1000 in the range [0...n]")
    print("6. the in order integers [0...n] where (log n/2) randomly chosen values have been swapped with another value.")

    # Get user input for option
    option = int(input("Enter your choice (1-6): "))

    if option not in range(1, 7):
        print("Invalid option. Exiting.")
        sys.exit()

    input_sizes = [100000, 250000, 500000, 750000, 1000000]
    # input_sizes = [10, 250, 5000, 7500, 10000]
    execution_times_heap = []
    execution_times_quick = []
    execution_times_merge = []
    execution_times_radix = []
    execution_times_bucket = []
    execution_times_tim = []
    data = []

    for algorithm_name, sorting_algorithm in sorting_algorithms.get_all_algorithms().items():  # Remove parentheses here
        execution_times = []
        for size in input_sizes:
            input_data = DataGenerator.generate_random_integers(size, option)
            time_taken = PerformanceMeasurement.measure_time(sorting_algorithm, input_data)
            execution_times.append(time_taken)
        data.append([algorithm_name] + execution_times)
        if algorithm_name == 'Heap Sort':
            execution_times_heap = execution_times
        elif algorithm_name == 'Quick Sort':
            execution_times_quick = execution_times
        elif algorithm_name == 'Merge Sort':
            execution_times_merge = execution_times
        elif algorithm_name == 'Radix Sort':
            execution_times_radix = execution_times
        elif algorithm_name == 'Bucket Sort':
            execution_times_bucket = execution_times
        elif algorithm_name == 'Tim Sort':
            execution_times_tim = execution_times

    # Display data in tabular format
    headers = [""] + [f"{size}" for size in input_sizes]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    # Export data to CSV
    filename = "sorting_algorithm_performance.csv"

    # Write data to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers
        writer.writerow(headers)
        
        # Write data rows
        for row in data:
            writer.writerow(row)

    PerformanceMeasurement.plot_graph(input_sizes, execution_times_heap, execution_times_quick, execution_times_merge, execution_times_radix, execution_times_bucket, execution_times_tim)
    plt.show()
