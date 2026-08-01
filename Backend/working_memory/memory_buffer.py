"""
Adaptive Context Intelligence Engine (ACIE)
Memory Buffer
"""

from collections import deque


class MemoryBuffer:

    def __init__(self, capacity=10):

        self.capacity = capacity

        self.buffer = deque(maxlen=capacity)

    def add_memory(self, memory):

        self.buffer.append(memory)

    def get_memories(self):

        return list(self.buffer)

    def get_latest(self):

        if len(self.buffer) == 0:

            return None

        return self.buffer[-1]

    def clear(self):

        self.buffer.clear()

    def size(self):

        return len(self.buffer)

    def is_empty(self):

        return len(self.buffer) == 0

    def is_full(self):

        return len(self.buffer) == self.capacity


if __name__ == "__main__":

    buffer = MemoryBuffer(capacity=5)

    buffer.add_memory("Memory 1")
    buffer.add_memory("Memory 2")
    buffer.add_memory("Memory 3")
    buffer.add_memory("Memory 4")
    buffer.add_memory("Memory 5")

    print("\nCurrent Buffer\n")

    print(buffer.get_memories())

    print("\nLatest Memory\n")

    print(buffer.get_latest())

    print("\nBuffer Size\n")

    print(buffer.size())