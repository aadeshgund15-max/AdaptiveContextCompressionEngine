"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Complete DSA Testing

=====================================================
"""
import os
import sys

CURRENT_DIR = os.path.dirname(__file__)
BACKEND_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))

sys.path.insert(0, BACKEND_DIR)

from data_structures.linked_list import LinkedList
from data_structures.stack import Stack
from data_structures.queue import Queue, CircularQueue
from data_structures.hash_table import HashTable
from data_structures.binary_search_tree import BinarySearchTree
from data_structures.avl_tree import AVLTree
from data_structures.graph import Graph
from data_structures.searching import Searching
from data_structures.sorting import Sorting
from data_structures.merge_sort import MergeSort
from data_structures.quick_sort import QuickSort


# ====================================================
# LINKED LIST
# ====================================================

print("\n==============================")
print("LINKED LIST")
print("==============================")

ll = LinkedList()

ll.append("Hello", "Hi")
ll.append("AI", "Artificial Intelligence")
ll.append("Hash", "Hashing")

ll.display()

search_result = ll.search("AI")
print("Search AI :", search_result.response if search_result else None)
print("Total :", ll.count())


# ====================================================
# STACK
# ====================================================

print("\n==============================")
print("STACK")
print("==============================")

stack = Stack()

stack.push("Step 1")
stack.push("Step 2")
stack.push("Step 3")

stack.display()

print("Peek :", stack.peek())
print("Pop :", stack.pop())
stack.display()


# ====================================================
# QUEUE
# ====================================================

print("\n==============================")
print("QUEUE")
print("==============================")

queue = Queue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print(queue.display())

print("Front :", queue.front())
print("Rear :", queue.rear())

print("Removed :", queue.dequeue())

print(queue.display())


# ====================================================
# CIRCULAR QUEUE
# ====================================================

print("\n==============================")
print("CIRCULAR QUEUE")
print("==============================")

cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

print(cq.display())

print("Removed :", cq.dequeue())

print(cq.display())


# ====================================================
# HASH TABLE
# ====================================================

print("\n==============================")
print("HASH TABLE")
print("==============================")

table = HashTable()

table.insert("user", "Aadesh")
table.insert("project", "ACIE")
table.insert("language", "Python")

table.display()

print("Project :", table.get("project"))

table.delete("language")

table.display()


# ====================================================
# BINARY SEARCH TREE
# ====================================================

print("\n==============================")
print("BINARY SEARCH TREE")
print("==============================")

bst = BinarySearchTree()

for value in [50,30,70,20,40,60,80]:
    bst.insert(value)

print("Inorder :", bst.inorder())
print("Height :", bst.height())

bst.delete(30)

print("After Delete :", bst.inorder())


# ====================================================
# AVL TREE
# ====================================================

print("\n==============================")
print("AVL TREE")
print("==============================")

avl = AVLTree()

for value in [30,20,40,10,25,35,50]:
    avl.insert(value)

print("Inorder :", avl.inorder())
print("Height :", avl.height())

avl.delete(20)

print("After Delete :", avl.inorder())

avl.display()


# ====================================================
# GRAPH
# ====================================================

print("\n==============================")
print("GRAPH")
print("==============================")

graph = Graph(True)

graph.add_edge("A","B")
graph.add_edge("A","C")
graph.add_edge("B","D")
graph.add_edge("C","D")
graph.add_edge("D","E")

graph.display()

print("BFS :", graph.bfs("A"))
print("DFS :", graph.dfs("A"))
print("Shortest :", graph.shortest_path("A","E"))


# ====================================================
# SEARCHING
# ====================================================

print("\n==============================")
print("SEARCHING")
print("==============================")

search = Searching()

numbers = [2,5,8,11,15,20,25]

print("Linear :", search.linear_search(numbers,15))
print("Binary :", search.binary_search(numbers,15))

print("Execution :", search.execution_time())


# ====================================================
# SORTING
# ====================================================

print("\n==============================")
print("SORTING")
print("==============================")

sort = Sorting()

data = [8,3,5,2,9,1]

print("Selection :", sort.selection_sort(data))
print("Insertion :", sort.insertion_sort(data))
print("Merge :", sort.merge_sort(data))
print("Quick :", sort.quick_sort(data))

print("Execution :", sort.execution_time())


# ====================================================
# MERGE SORT CLASS
# ====================================================

print("\n==============================")
print("MERGE SORT CLASS")
print("==============================")

merge = MergeSort()

print(merge.sort([9,4,7,2,5,1]))

print("Execution :", merge.execution_time())


# ====================================================
# QUICK SORT CLASS
# ====================================================

print("\n==============================")
print("QUICK SORT CLASS")
print("==============================")

quick = QuickSort()

print(quick.sort([12,5,8,1,10,2]))

print("Execution :", quick.execution_time())


print("\n========================================")
print("ALL DSA MODULES EXECUTED SUCCESSFULLY")
print("========================================")