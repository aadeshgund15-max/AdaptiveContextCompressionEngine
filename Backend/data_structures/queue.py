"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Queue Data Structure

DSA Module 1

Linear Queue
Circular Queue

=====================================================
"""


class Queue:

    def __init__(self):

        self.queue = []

    # =============================================
    # Enqueue
    # =============================================

    def enqueue(self, data):

        self.queue.append(data)

    # =============================================
    # Dequeue
    # =============================================

    def dequeue(self):

        if self.is_empty():

            return None

        return self.queue.pop(0)

    # =============================================
    # Front Element
    # =============================================

    def front(self):

        if self.is_empty():

            return None

        return self.queue[0]

    # =============================================
    # Rear Element
    # =============================================

    def rear(self):

        if self.is_empty():

            return None

        return self.queue[-1]

    # =============================================
    # Check Empty
    # =============================================

    def is_empty(self):

        return len(self.queue) == 0

    # =============================================
    # Size
    # =============================================

    def size(self):

        return len(self.queue)

    # =============================================
    # Display Queue
    # =============================================

    def display(self):

        return self.queue


# ==================================================
# Circular Queue
# ==================================================

class CircularQueue:

    def __init__(self, capacity):

        self.capacity = capacity

        self.queue = [None] * capacity

        self.front_index = -1

        self.rear_index = -1

    # =============================================
    # Check Empty
    # =============================================

    def is_empty(self):

        return self.front_index == -1

    # =============================================
    # Check Full
    # =============================================

    def is_full(self):

        return (self.rear_index + 1) % self.capacity == self.front_index

    # =============================================
    # Enqueue
    # =============================================

    def enqueue(self, data):

        if self.is_full():

            print("Queue Overflow")

            return

        if self.is_empty():

            self.front_index = 0

            self.rear_index = 0

        else:

            self.rear_index = (self.rear_index + 1) % self.capacity

        self.queue[self.rear_index] = data

    # =============================================
    # Dequeue
    # =============================================

    def dequeue(self):

        if self.is_empty():

            print("Queue Underflow")

            return None

        value = self.queue[self.front_index]

        if self.front_index == self.rear_index:

            self.front_index = -1

            self.rear_index = -1

        else:

            self.front_index = (self.front_index + 1) % self.capacity

        return value

    # =============================================
    # Front
    # =============================================

    def front(self):

        if self.is_empty():

            return None

        return self.queue[self.front_index]

    # =============================================
    # Rear
    # =============================================

    def rear(self):

        if self.is_empty():

            return None

        return self.queue[self.rear_index]

    # =============================================
    # Display Queue
    # =============================================

    def display(self):

        if self.is_empty():

            print("Queue is Empty")

            return

        i = self.front_index

        elements = []

        while True:

            elements.append(self.queue[i])

            if i == self.rear_index:

                break

            i = (i + 1) % self.capacity

        return elements