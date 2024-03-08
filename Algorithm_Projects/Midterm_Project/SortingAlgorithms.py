class SortingAlgorithms:
    
    def get_all_algorithms(self):
        return {
            'Heap Sort': SortingAlgorithms.heap_sort,
            'Quick Sort': SortingAlgorithms.quick_sort,
            'Merge Sort': SortingAlgorithms.merge_sort,
            'Radix Sort': SortingAlgorithms.radix_sort,
            'Bucket Sort': SortingAlgorithms.bucket_sort,
            'Tim Sort': SortingAlgorithms.tim_sort
        }
        
    def heap_sort(arr):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[l] > arr[largest]:
                largest = l

            if r < n and arr[r] > arr[largest]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(arr)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            heapify(arr, i, 0)

        return arr

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        # Split array in half and recursively sort each half
        mid = len(arr) // 2
        left_half = SortingAlgorithms.merge_sort(arr[:mid])
        right_half = SortingAlgorithms.merge_sort(arr[mid:])

        # Merge sorted halves
        merged = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left_half) and right_idx < len(right_half):
            if left_half[left_idx] < right_half[right_idx]:
                merged.append(left_half[left_idx])
                left_idx += 1
            else:
                merged.append(right_half[right_idx])
                right_idx += 1
        merged.extend(left_half[left_idx:])
        merged.extend(right_half[right_idx:])
        return merged

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return SortingAlgorithms.quick_sort(left) + middle + SortingAlgorithms.quick_sort(right)

    def radix_sort(arr):
        def counting_sort(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = arr[i] // exp
                count[index % 10] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            i = 0
            for i in range(n):
                arr[i] = output[i]

        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            counting_sort(arr, exp)
            exp *= 10
        return arr

    def bucket_sort(arr):
        n = len(arr)
        buckets = [[] for _ in range(n)]

        for num in arr:
            index = min(int(num * n), n - 1)
            buckets[index].append(num)

        for i in range(n):
            buckets[i] = sorted(buckets[i])

        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(bucket)

        return sorted_arr

    def tim_sort(arr):
        def insertion_sort(arr, left=0, right=None):
            if right is None:
                right = len(arr) - 1

            for i in range(left + 1, right + 1):
                key = arr[i]
                j = i - 1
                while j >= left and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

        def merge(arr, l, m, r):
            len1, len2 = m - l + 1, r - m
            left, right = arr[l:m + 1], arr[m + 1:r + 1]
            i, j, k = 0, 0, l

            while i < len1 and j < len2:
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len1:
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len2:
                arr[k] = right[j]
                j += 1
                k += 1

        n = len(arr)
        min_run = 32

        for start in range(0, n, min_run):
            end = min(start + min_run - 1, n - 1)
            insertion_sort(arr, start, end)

        size = min_run
        while size < n:
            for left in range(0, n, size * 2):
                mid = min(n - 1, left + size - 1)
                right = min(n - 1, mid + size)
                merge(arr, left, mid, right)
            size *= 2
        return arr
