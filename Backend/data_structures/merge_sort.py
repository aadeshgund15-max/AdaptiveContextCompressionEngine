"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Merge Sort

DSA Module 4

=====================================================
"""

from Backend.data_structures.analysis import AlgorithmAnalysis

class MergeSort:

    def __init__(self):

        self.analysis = AlgorithmAnalysis()


    # =============================================
    # Public Method
    # =============================================

    def sort(self, arr):

        data = arr.copy()

        self.analysis.start()

        self._merge_sort(data)

        self.analysis.stop()

        return data


    # =============================================
    # Recursive Merge Sort
    # =============================================

    def _merge_sort(self, arr):

        if len(arr) > 1:

            mid = len(arr) // 2

            left = arr[:mid]

            right = arr[mid:]

            self._merge_sort(left)

            self._merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):

                if left[i] <= right[j]:

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


    # =============================================
    # Execution Time
    # =============================================

    def execution_time(self):

        return self.analysis.get_execution_time()


    # =============================================
    # Complexity
    # =============================================

    def show_complexity(self):

        self.analysis.display_complexity("merge sort")


if __name__ == "__main__":

    sample = [38, 27, 43, 3, 9, 82, 10]

    sorter = MergeSort()

    print("Original:", sample)

    print("Sorted:", sorter.sort(sample))

    print("Execution Time:", sorter.execution_time())
