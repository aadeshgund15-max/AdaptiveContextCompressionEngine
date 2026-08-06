"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Algorithm Analysis Module

DSA Module 4

Time Complexity
Space Complexity
Performance Measurement

=====================================================
"""

import time


class AlgorithmAnalysis:

    def __init__(self):

        self.start_time = 0

        self.end_time = 0

        self.execution_time = 0


    # ============================================
    # Start Timer
    # ============================================

    def start(self):

        self.start_time = time.perf_counter()


    # ============================================
    # Stop Timer
    # ============================================

    def stop(self):

        self.end_time = time.perf_counter()

        self.execution_time = self.end_time - self.start_time

        return self.execution_time


    # ============================================
    # Get Execution Time
    # ============================================

    def get_execution_time(self):

        return self.execution_time


    # ============================================
    # Complexity Information
    # ============================================

    def complexity(self, algorithm):

        algorithm = algorithm.lower()

        complexities = {

            "linear search": {
                "time": "O(n)",
                "space": "O(1)"
            },

            "binary search": {
                "time": "O(log n)",
                "space": "O(1)"
            },

            "selection sort": {
                "time": "O(n²)",
                "space": "O(1)"
            },

            "insertion sort": {
                "time": "O(n²)",
                "space": "O(1)"
            },

            "merge sort": {
                "time": "O(n log n)",
                "space": "O(n)"
            },

            "quick sort": {
                "time": "O(n log n)",
                "space": "O(log n)"
            },

            "stack": {
                "time": "O(1)",
                "space": "O(n)"
            },

            "queue": {
                "time": "O(1)",
                "space": "O(n)"
            },

            "linked list": {
                "time": "O(n)",
                "space": "O(n)"
            },

            "binary search tree": {
                "time": "O(log n)",
                "space": "O(n)"
            },

            "avl tree": {
                "time": "O(log n)",
                "space": "O(n)"
            },

            "hashing": {
                "time": "O(1)",
                "space": "O(n)"
            },

            "graph bfs": {
                "time": "O(V + E)",
                "space": "O(V)"
            },

            "graph dfs": {
                "time": "O(V + E)",
                "space": "O(V)"
            }

        }

        return complexities.get(
            algorithm,
            {
                "time": "Unknown",
                "space": "Unknown"
            }
        )


    # ============================================
    # Print Complexity
    # ============================================

    def display_complexity(self, algorithm):

        result = self.complexity(algorithm)

        print("\n==============================")

        print("Algorithm :", algorithm)

        print("Time Complexity :", result["time"])

        print("Space Complexity :", result["space"])

        print("==============================\n")


    # ============================================
    # Display Execution Time
    # ============================================

    def display_execution_time(self):

        print("\nExecution Time :")

        print(f"{self.execution_time:.8f} seconds\n")