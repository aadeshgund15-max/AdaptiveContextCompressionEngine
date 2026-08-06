"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Graph Data Structure

DSA Module: Graphs

=====================================================
"""

from Backend.data_structures.analysis import AlgorithmAnalysis

class Graph:

    def __init__(self, directed=False):

        self.directed = directed

        self.adjacency = {}

        self.analysis = AlgorithmAnalysis()


    # =============================================
    # Add Node
    # =============================================

    def add_node(self, node):

        if node not in self.adjacency:

            self.adjacency[node] = []


    # =============================================
    # Add Edge
    # =============================================

    def add_edge(self, source, target):

        self.add_node(source)

        self.add_node(target)

        self.adjacency[source].append(target)

        if not self.directed:

            self.adjacency[target].append(source)


    # =============================================
    # Get Neighbors
    # =============================================

    def get_neighbors(self, node):

        return self.adjacency.get(node, []).copy()


    # =============================================
    # Breadth-First Search
    # =============================================

    def bfs(self, start):

        if start not in self.adjacency:

            return []

        self.analysis.start()

        visited = []

        queue = [start]

        seen = {start}

        while queue:

            current = queue.pop(0)

            visited.append(current)

            for neighbor in self.adjacency[current]:

                if neighbor not in seen:

                    seen.add(neighbor)

                    queue.append(neighbor)

        self.analysis.stop()

        return visited


    # =============================================
    # Depth-First Search
    # =============================================

    def dfs(self, start):

        if start not in self.adjacency:

            return []

        self.analysis.start()

        visited = []

        stack = [start]

        seen = {start}

        while stack:

            current = stack.pop()

            visited.append(current)

            for neighbor in reversed(self.adjacency[current]):

                if neighbor not in seen:

                    seen.add(neighbor)

                    stack.append(neighbor)

        self.analysis.stop()

        return visited


    # =============================================
    # Shortest Path (Unweighted)
    # =============================================

    def shortest_path(self, start, target):

        if start not in self.adjacency or target not in self.adjacency:

            return []

        self.analysis.start()

        queue = [(start, [start])]

        seen = {start}

        while queue:

            current, path = queue.pop(0)

            if current == target:

                self.analysis.stop()

                return path

            for neighbor in self.adjacency[current]:

                if neighbor not in seen:

                    seen.add(neighbor)

                    queue.append((neighbor, path + [neighbor]))

        self.analysis.stop()

        return []


    # =============================================
    # Check Path Exists
    # =============================================

    def has_path(self, start, target):

        return len(self.shortest_path(start, target)) > 0


    # =============================================
    # Display Graph
    # =============================================

    def display(self):

        print("\n===== Graph =====")

        for node, neighbors in self.adjacency.items():

            print(f"{node} -> {neighbors}")

        print("=================\n")


    # =============================================
    # Execution Time
    # =============================================

    def execution_time(self):

        return self.analysis.get_execution_time()


    # =============================================
    # Complexity
    # =============================================

    def show_complexity(self, algorithm):

        self.analysis.display_complexity(algorithm)


if __name__ == "__main__":

    graph = Graph(directed=True)

    graph.add_edge("A", "B")

    graph.add_edge("A", "C")

    graph.add_edge("B", "D")

    graph.add_edge("C", "D")

    graph.add_edge("D", "E")

    print("Neighbors of A:", graph.get_neighbors("A"))

    print("BFS from A:", graph.bfs("A"))

    print("DFS from A:", graph.dfs("A"))

    print("Shortest path A to E:", graph.shortest_path("A", "E"))

    print("Execution Time:", graph.execution_time())

    graph.display()
