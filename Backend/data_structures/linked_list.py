from __future__ import annotations
from typing import Optional

"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Linked List Implementation

Used for:
- Conversation History
- Memory Timeline
- Sequential Context Storage

DSA Module:
Linear Data Structures

=====================================================
"""


class Node:

    def __init__(self, query, response):

        self.query = query

        self.response = response

        self.next: Optional[Node] = None


class LinkedList:

    def __init__(self):

        self.head: Optional[Node] = None

        self.tail: Optional[Node] = None

        self.size = 0


    # ============================================
    # Insert at End
    # ============================================

    def append(self, query, response):

        new_node = Node(query, response)

        if self.head is None:

            self.head = new_node

            self.tail = new_node

        else:

            # mypy/type-checkers may warn that tail could be None here;
            # since head is not None, tail should also be non-None for a well-formed list
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1


    # ============================================
    # Insert at Beginning
    # ============================================

    def prepend(self, query, response):

        new_node = Node(query, response)

        if self.head is None:

            self.head = new_node

            self.tail = new_node

        else:

            new_node.next = self.head

            self.head = new_node

        self.size += 1


    # ============================================
    # Delete First Node
    # ============================================

    def delete_first(self):

        if self.head is None:

            return None

        deleted = self.head

        self.head = self.head.next

        if self.head is None:

            self.tail = None

        self.size -= 1

        return deleted


    # ============================================
    # Delete Last Node
    # ============================================

    def delete_last(self):

        if self.head is None:

            return None

        if self.head.next is None:

            deleted = self.head

            self.head = None

            self.tail = None

            self.size -= 1

            return deleted

        current = self.head
        assert current is not None

        while current.next is not self.tail:

            next_node = current.next
            assert next_node is not None
            current = next_node

        deleted = self.tail

        current.next = None

        self.tail = current

        self.size -= 1

        return deleted


    # ============================================
    # Search
    # ============================================

    def search(self, query):

        current = self.head

        while current is not None:

            if current.query == query:

                return current

            assert current is not None
            current = current.next

        return None


    # ============================================
    # Get Conversation by Index
    # ============================================

    def get(self, index):

        if index < 0 or index >= self.size:

            return None

        current = self.head

        position = 0

        while current is not None:

            if position == index:

                return current

            current = current.next

            position += 1

        return None


    # ============================================
    # Display
    # ============================================

    def display(self):

        current = self.head

        count = 1

        while current is not None:

            print("--------------------------------")

            print("Conversation :", count)

            print("Query        :", current.query)

            print("Response     :", current.response)

            print("--------------------------------")

            current = current.next

            count += 1


    # ============================================
    # Convert to List
    # ============================================

    def to_list(self):

        conversations = []

        current = self.head

        while current is not None:

            conversations.append({

                "query": current.query,

                "response": current.response

            })

            current = current.next

        return conversations


    # ============================================
    # Count Nodes
    # ============================================

    def count(self):

        return self.size


    # ============================================
    # Check Empty
    # ============================================

    def is_empty(self):

        return self.size == 0


    # ============================================
    # Clear
    # ============================================

    def clear(self):

        self.head = None

        self.tail = None

        self.size = 0