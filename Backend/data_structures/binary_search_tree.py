from __future__ import annotations
from typing import Optional, List

"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Binary Search Tree

DSA Module: Trees

=====================================================
"""


class TreeNode:

    def __init__(self, value):

        self.value = value

        self.left: Optional[TreeNode] = None

        self.right: Optional[TreeNode] = None


class BinarySearchTree:

    def __init__(self):

        self.root: Optional[TreeNode] = None


    # ============================================
    # Insert Value
    # ============================================

    def insert(self, value):

        if self.root is None:

            self.root = TreeNode(value)

            return

        self._insert_node(self.root, value)


    def _insert_node(self, node: TreeNode, value):

        if value < node.value:

            if node.left is None:

                node.left = TreeNode(value)

            else:

                self._insert_node(node.left, value)

        else:

            if node.right is None:

                node.right = TreeNode(value)

            else:

                self._insert_node(node.right, value)


    # ============================================
    # Search Value
    # ============================================

    def search(self, value) -> Optional[TreeNode]:

        return self._search_node(self.root, value)


    def _search_node(self, node: Optional[TreeNode], value) -> Optional[TreeNode]:

        if node is None:

            return None

        if value == node.value:

            return node

        if value < node.value:

            return self._search_node(node.left, value)

        return self._search_node(node.right, value)


    # ============================================
    # Delete Value
    # ============================================

    def delete(self, value) -> bool:

        self.root, deleted = self._delete_node(self.root, value)

        return deleted


    def _delete_node(self, node: Optional[TreeNode], value):

        if node is None:

            return None, False

        if value < node.value:

            node.left, deleted = self._delete_node(node.left, value)

            return node, deleted

        if value > node.value:

            node.right, deleted = self._delete_node(node.right, value)

            return node, deleted

        # Node to delete found
        if node.left is None:

            return node.right, True

        if node.right is None:

            return node.left, True

        successor = self._get_min_node(node.right)

        assert successor is not None
        node.value = successor.value

        node.right, _ = self._delete_node(node.right, successor.value)

        return node, True


    # ============================================
    # Traversals
    # ============================================

    def inorder(self) -> List:

        return self._traverse_inorder(self.root)


    def _traverse_inorder(self, node: Optional[TreeNode]) -> List:

        result: List = []

        if node is not None:

            result.extend(self._traverse_inorder(node.left))

            result.append(node.value)

            result.extend(self._traverse_inorder(node.right))

        return result


    def preorder(self) -> List:

        return self._traverse_preorder(self.root)


    def _traverse_preorder(self, node: Optional[TreeNode]) -> List:

        result: List = []

        if node is not None:

            result.append(node.value)

            result.extend(self._traverse_preorder(node.left))

            result.extend(self._traverse_preorder(node.right))

        return result


    def postorder(self) -> List:

        return self._traverse_postorder(self.root)


    def _traverse_postorder(self, node: Optional[TreeNode]) -> List:

        result: List = []

        if node is not None:

            result.extend(self._traverse_postorder(node.left))

            result.extend(self._traverse_postorder(node.right))

            result.append(node.value)

        return result


    # ============================================
    # Minimum / Maximum
    # ============================================

    def get_min(self):

        node = self._get_min_node(self.root)

        return node.value if node else None


    def _get_min_node(self, node: Optional[TreeNode]) -> Optional[TreeNode]:

        while node and node.left is not None:

            node = node.left

        return node


    def get_max(self):

        node = self._get_max_node(self.root)

        return node.value if node else None


    def _get_max_node(self, node: Optional[TreeNode]) -> Optional[TreeNode]:

        while node and node.right is not None:

            node = node.right

        return node


    # ============================================
    # Tree Height
    # ============================================

    def height(self) -> int:

        return self._height(self.root)


    def _height(self, node: Optional[TreeNode]) -> int:

        if node is None:

            return 0

        return 1 + max(self._height(node.left), self._height(node.right))


    # ============================================
    # Check Empty
    # ============================================

    def is_empty(self) -> bool:

        return self.root is None


    # ============================================
    # Display Tree
    # ============================================

    def display(self):

        print("\n===== Binary Search Tree =====")

        self._display_node(self.root, 0)

        print("==============================\n")


    def _display_node(self, node: Optional[TreeNode], level: int):

        if node is None:

            return

        self._display_node(node.right, level + 1)

        print("    " * level + str(node.value))

        self._display_node(node.left, level + 1)


if __name__ == "__main__":

    tree = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:

        tree.insert(value)

    print("Inorder:", tree.inorder())

    print("Preorder:", tree.preorder())

    print("Postorder:", tree.postorder())

    print("Min:", tree.get_min())

    print("Max:", tree.get_max())

    print("Height:", tree.height())

    print("Search 60:", tree.search(60) is not None)

    print("Delete 30:", tree.delete(30))

    print("Inorder after delete:", tree.inorder())

    tree.display()
