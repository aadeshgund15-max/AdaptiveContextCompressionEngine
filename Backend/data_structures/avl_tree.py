from __future__ import annotations
from typing import Optional, List

from Backend.data_structures.analysis import AlgorithmAnalysis
"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

AVL Tree

DSA Module: Trees

=====================================================
"""


class AVLNode:

    def __init__(self, value):

        self.value = value

        self.left: Optional[AVLNode] = None

        self.right: Optional[AVLNode] = None

        self.height = 1


class AVLTree:

    def __init__(self):

        self.root: Optional[AVLNode] = None

        self.analysis = AlgorithmAnalysis()


    # ============================================
    # Public Insert
    # ============================================

    def insert(self, value):

        self.analysis.start()

        self.root = self._insert_node(self.root, value)

        self.analysis.stop()

        return self.root


    def _insert_node(self, node: Optional[AVLNode], value) -> AVLNode:

        if node is None:

            return AVLNode(value)

        if value < node.value:

            node.left = self._insert_node(node.left, value)

        else:

            node.right = self._insert_node(node.right, value)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        return self._balance(node)


    # ============================================
    # Public Delete
    # ============================================

    def delete(self, value) -> bool:

        self.analysis.start()

        self.root, deleted = self._delete_node(self.root, value)

        self.analysis.stop()

        return deleted


    def _delete_node(self, node: Optional[AVLNode], value):

        if node is None:

            return None, False

        deleted = False

        if value < node.value:

            node.left, deleted = self._delete_node(node.left, value)

        elif value > node.value:

            node.right, deleted = self._delete_node(node.right, value)

        else:

            deleted = True

            if node.left is None:

                return node.right, deleted

            elif node.right is None:

                return node.left, deleted

            else:

                successor = self._get_min_node(node.right)

                assert successor is not None
                node.value = successor.value

                node.right, _ = self._delete_node(node.right, successor.value)

        if node is None:

            return None, deleted

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        return self._balance(node), deleted


    # ============================================
    # Search
    # ============================================

    def search(self, value) -> Optional[AVLNode]:

        return self._search_node(self.root, value)


    def _search_node(self, node: Optional[AVLNode], value) -> Optional[AVLNode]:

        if node is None:

            return None

        if value == node.value:

            return node

        if value < node.value:

            return self._search_node(node.left, value)

        return self._search_node(node.right, value)


    # ============================================
    # Traversals
    # ============================================

    def inorder(self) -> List:

        return self._traverse_inorder(self.root)


    def _traverse_inorder(self, node: Optional[AVLNode]) -> List:

        result: List = []

        if node is not None:

            result.extend(self._traverse_inorder(node.left))

            result.append(node.value)

            result.extend(self._traverse_inorder(node.right))

        return result


    def preorder(self) -> List:

        return self._traverse_preorder(self.root)


    def _traverse_preorder(self, node: Optional[AVLNode]) -> List:

        result: List = []

        if node is not None:

            result.append(node.value)

            result.extend(self._traverse_preorder(node.left))

            result.extend(self._traverse_preorder(node.right))

        return result


    def postorder(self) -> List:

        return self._traverse_postorder(self.root)


    def _traverse_postorder(self, node: Optional[AVLNode]) -> List:

        result: List = []

        if node is not None:

            result.extend(self._traverse_postorder(node.left))

            result.extend(self._traverse_postorder(node.right))

            result.append(node.value)

        return result


    # ============================================
    # Height and Balance
    # ============================================

    def height(self) -> int:

        return self._height(self.root)


    def _height(self, node: Optional[AVLNode]) -> int:

        return node.height if node is not None else 0


    def _get_balance(self, node: Optional[AVLNode]) -> int:

        if node is None:

            return 0

        return self._height(node.left) - self._height(node.right)


    # ============================================
    # Rotation Helpers
    # ============================================

    def _right_rotate(self, z: AVLNode) -> AVLNode:

        y = z.left

        assert y is not None

        t3 = y.right

        y.right = z

        z.left = t3

        z.height = 1 + max(self._height(z.left), self._height(z.right))

        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y


    def _left_rotate(self, z: AVLNode) -> AVLNode:

        y = z.right

        assert y is not None

        t2 = y.left

        y.left = z

        z.right = t2

        z.height = 1 + max(self._height(z.left), self._height(z.right))

        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y


    def _balance(self, node: AVLNode) -> AVLNode:
        balance = self._get_balance(node)

        if balance > 1:
            left_child = node.left
            if left_child is None:
                return node

            if self._get_balance(left_child) < 0:
                node.left = self._left_rotate(left_child)

            return self._right_rotate(node)

        if balance < -1:
            right_child = node.right
            if right_child is None:
                return node

            if self._get_balance(right_child) > 0:
                node.right = self._right_rotate(right_child)

            return self._left_rotate(node)

        return node

    # ============================================
    # Minimum / Maximum
    # ============================================

    def get_min(self):

        node = self._get_min_node(self.root)

        return node.value if node else None


    def _get_min_node(self, node: Optional[AVLNode]) -> Optional[AVLNode]:

        while node and node.left is not None:

            node = node.left

        return node


    def get_max(self):

        node = self._get_max_node(self.root)

        return node.value if node else None


    def _get_max_node(self, node: Optional[AVLNode]) -> Optional[AVLNode]:

        while node and node.right is not None:

            node = node.right

        return node


    # ============================================
    # Empty Check
    # ============================================

    def is_empty(self) -> bool:

        return self.root is None


    # ============================================
    # Display Tree
    # ============================================

    def display(self):

        print("\n===== AVL Tree =====")

        self._display_node(self.root, 0)

        print("====================\n")


    def _display_node(self, node: Optional[AVLNode], level: int):

        if node is None:

            return

        self._display_node(node.right, level + 1)

        print("    " * level + str(node.value))

        self._display_node(node.left, level + 1)


    # ============================================
    # Timing and Complexity
    # ============================================

    def execution_time(self):

        return self.analysis.get_execution_time()


    def show_complexity(self):

        self.analysis.display_complexity("avl tree")


if __name__ == "__main__":

    tree = AVLTree()

    for value in [30, 20, 40, 10, 25, 35, 50, 5, 15]:

        tree.insert(value)

    print("Inorder:", tree.inorder())

    print("Preorder:", tree.preorder())

    print("Postorder:", tree.postorder())

    print("Min:", tree.get_min())

    print("Max:", tree.get_max())

    print("Height:", tree.height())

    print("Search 25:", tree.search(25) is not None)

    print("Delete 20:", tree.delete(20))

    print("Inorder after delete:", tree.inorder())

    tree.display()

    print("Execution Time:", tree.execution_time())
