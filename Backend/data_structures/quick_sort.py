"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Quick Sort

DSA Module 4

=====================================================
"""

from Backend.data_structures.analysis import AlgorithmAnalysis

class QuickSort:

    def __init__(self):

        self.analysis = AlgorithmAnalysis()


    # =============================================
    # Public Method
    # =============================================

    def sort(self, arr):

        data = arr.copy()

        self.analysis.start()

        self.quick_sort(data, 0, len(data) - 1)

        self.analysis.stop()

        return data


    # =============================================
    # Recursive Quick Sort
    # =============================================

    def quick_sort(self, arr, low, high):

        if low < high:

            pivot = self.partition(arr, low, high)

            self.quick_sort(arr, low, pivot - 1)

            self.quick_sort(arr, pivot + 1, high)


    # =============================================
    # Partition Function
    # =============================================

    def partition(self, arr, low, high):

        pivot = arr[high]

        i = low - 1

        for j in range(low, high):

            if arr[j] <= pivot:

                i += 1

                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1


    # =============================================
    # Execution Time
    # =============================================

    def execution_time(self):

        return self.analysis.get_execution_time()


    # =============================================
    # Complexity
    # =============================================

    def show_complexity(self):

        self.analysis.display_complexity("quick sort")