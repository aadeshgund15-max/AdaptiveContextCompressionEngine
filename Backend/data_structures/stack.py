"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Stack Implementation

Used for:
- AI Reasoning Trace
- Function Execution History
- Agent Processing Steps

DSA Module:
Stack using Array

=====================================================
"""


class Stack:

    def __init__(self):

        self.items = []


    # ============================================
    # Push
    # ============================================

    def push(self, item):

        self.items.append(item)


    # ============================================
    # Pop
    # ============================================

    def pop(self):

        if self.is_empty():

            return None

        return self.items.pop()


    # ============================================
    # Peek
    # ============================================

    def peek(self):

        if self.is_empty():

            return None

        return self.items[-1]


    # ============================================
    # Check Empty
    # ============================================

    def is_empty(self):

        return len(self.items) == 0


    # ============================================
    # Size
    # ============================================

    def size(self):

        return len(self.items)


    # ============================================
    # Clear Stack
    # ============================================

    def clear(self):

        self.items.clear()


    # ============================================
    # Display
    # ============================================

    def display(self):

        if self.is_empty():

            print("Stack is Empty")
            return

        print("\n===== Stack =====")

        for i in range(len(self.items) - 1, -1, -1):

            print(self.items[i])

        print("=================\n")


    # ============================================
    # Convert to List
    # ============================================

    def to_list(self):

        return self.items.copy()


    # ============================================
    # Search
    # ============================================

    def contains(self, item):

        return item in self.items