import random
import math

class DataGenerator:
    def generate_random_integers(n, option):
        if option == 1:
            return [random.randint(0, n) for _ in range(n)]
        elif option == 2:
            k = random.randint(0, 999)
            return [random.randint(0, k) for _ in range(n)]
        elif option == 3:
            return [random.randint(0, n**3) for _ in range(n)]
        elif option == 4:
            return [random.randint(0, int(math.log2(n))) for _ in range(n)]
        elif option == 5:
            return [random.randint(0, n) * 1000 for _ in range(n)]
        elif option == 6:
            arr = [i for i in range(n)]
            for _ in range(int(math.log2(n) / 2)):
                idx1 = random.randint(0, n - 1)
                idx2 = random.randint(0, n - 1)
                arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
            return arr
        else:
            raise ValueError("Invalid option")
