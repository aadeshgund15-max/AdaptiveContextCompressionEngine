"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Sorting Algorithms

DSA Module 4

Selection Sort
Insertion Sort
Merge Sort
Quick Sort

=====================================================
"""

from Backend.data_structures.analysis import AlgorithmAnalysis

class Sorting:

    def __init__(self):

        self.analysis = AlgorithmAnalysis()


    # ==================================================
    # Selection Sort
    # ==================================================

    def selection_sort(self, arr):

        data = arr.copy()

        self.analysis.start()

        n = len(data)

        for i in range(n):

            minimum = i

            for j in range(i + 1, n):

                if data[j] < data[minimum]:

                    minimum = j

            data[i], data[minimum] = data[minimum], data[i]

        self.analysis.stop()

        return data


    # ==================================================
    # Insertion Sort
    # ==================================================

    def insertion_sort(self, arr):

        data = arr.copy()

        self.analysis.start()

        for i in range(1, len(data)):

            key = data[i]

            j = i - 1

            while j >= 0 and data[j] > key:

                data[j + 1] = data[j]

                j -= 1

            data[j + 1] = key

        self.analysis.stop()

        return data


    # ==================================================
    # Merge Sort
    # ==================================================

    def merge_sort(self, arr):

        data = arr.copy()

        self.analysis.start()

        self._merge_sort(data)

        self.analysis.stop()

        return data


    def _merge_sort(self, arr):

        if len(arr) > 1:

            mid = len(arr) // 2

            left = arr[:mid]

            right = arr[mid:]

            self._merge_sort(left)

            self._merge_sort(right)

            i = 0

            j = 0

            k = 0

            while i < len(left) and j < len(right):

                if left[i] < right[j]:

                    arr[k] = left[i]

                    i += 1

                else:

                    arr[k] = right[j]

                    j += 1

                k += 1

            while i < len(left):

                arr[k] = left[i]

                i += 1

                k += 1

            while j < len(right):

                arr[k] = right[j]

                j += 1

                k += 1


    # ==================================================
    # Quick Sort
    # ==================================================

    def quick_sort(self, arr):

        data = arr.copy()

        self.analysis.start()

        self._quick_sort(data, 0, len(data) - 1)

        self.analysis.stop()

        return data


    def _quick_sort(self, arr, low, high):

        if low < high:

            pivot = self.partition(arr, low, high)

            self._quick_sort(arr, low, pivot - 1)

            self._quick_sort(arr, pivot + 1, high)


    def partition(self, arr, low, high):

        pivot = arr[high]

        i = low - 1

        for j in range(low, high):

            if arr[j] <= pivot:

                i += 1

                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1


    # ==================================================
    # Execution Time
    # ==================================================

    def execution_time(self):

        return self.analysis.get_execution_time()


    # ==================================================
    # Complexity
    # ==================================================

    def show_complexity(self, algorithm):

        self.analysis.display_complexity(algorithm)