"""
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Hash Table

DSA Module: Hashing

=====================================================
"""


class HashTable:

    def __init__(self, capacity=16):

        self.capacity = capacity

        self.size = 0

        self.buckets = [[] for _ in range(capacity)]


    # =============================================
    # Hash Function
    # =============================================

    def _hash(self, key):

        return hash(key) % self.capacity


    # =============================================
    # Insert / Update
    # =============================================

    def insert(self, key, value):

        index = self._hash(key)

        bucket = self.buckets[index]

        for item in bucket:

            if item[0] == key:

                item[1] = value

                return

        bucket.append([key, value])

        self.size += 1


    # =============================================
    # Search
    # =============================================

    def get(self, key):

        index = self._hash(key)

        bucket = self.buckets[index]

        for item in bucket:

            if item[0] == key:

                return item[1]

        return None


    # =============================================
    # Remove
    # =============================================

    def delete(self, key):

        index = self._hash(key)

        bucket = self.buckets[index]

        for i, item in enumerate(bucket):

            if item[0] == key:

                bucket.pop(i)

                self.size -= 1

                return True

        return False


    # =============================================
    # Contains
    # =============================================

    def contains(self, key):

        return self.get(key) is not None


    # =============================================
    # Keys
    # =============================================

    def keys(self):

        return [item[0] for bucket in self.buckets for item in bucket]


    # =============================================
    # Values
    # =============================================

    def values(self):

        return [item[1] for bucket in self.buckets for item in bucket]


    # =============================================
    # Items
    # =============================================

    def items(self):

        return [(item[0], item[1]) for bucket in self.buckets for item in bucket]


    # =============================================
    # Display Table
    # =============================================

    def display(self):

        print("\n===== Hash Table =====")

        for index, bucket in enumerate(self.buckets):

            if bucket:

                print(f"Bucket {index}:", bucket)

        print("======================\n")


if __name__ == "__main__":

    table = HashTable()

    table.insert("user1", "ACIE")

    table.insert("session", 42)

    table.insert("model", "Raptor")

    print("Keys:", table.keys())

    print("Values:", table.values())

    print("Model:", table.get("model"))

    print("Contains user1:", table.contains("user1"))

    print("Delete session:", table.delete("session"))

    table.display()
