"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Searching Algorithms

DSA Module 3

Linear Search
Binary Search

=====================================================
"""

from Backend.data_structures.analysis import AlgorithmAnalysis

class Searching:

    def __init__(self):

        self.analysis = AlgorithmAnalysis()

    # ==================================================
    # Linear Search
    # ==================================================

    def linear_search(self, arr, target):

        self.analysis.start()

        for i in range(len(arr)):

            if arr[i] == target:

                self.analysis.stop()

                return i

        self.analysis.stop()

        return -1

    # ==================================================
    # Binary Search
    # ==================================================

    def binary_search(self, arr, target):

        self.analysis.start()

        low = 0
        high = len(arr) - 1

        while low <= high:

            mid = (low + high) // 2

            if arr[mid] == target:

                self.analysis.stop()

                return mid

            elif arr[mid] < target:

                low = mid + 1

            else:

                high = mid - 1

        self.analysis.stop()

        return -1

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