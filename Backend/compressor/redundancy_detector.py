"""
Adaptive Context Intelligence Engine (ACIE)
Redundancy Detector
"""


class RedundancyDetector:

    def remove_duplicates(self, memories):

        unique = []

        seen = set()

        for memory in memories:

            cleaned = memory.strip().lower()

            if cleaned not in seen:

                seen.add(cleaned)

                unique.append(memory)

        return unique


if __name__ == "__main__":

    detector = RedundancyDetector()

    memories = [

        "Explain adaptive context compression.",

        "Explain adaptive context compression.",

        "Explain Semantic Compression.",

        "Explain semantic compression.",

        "Memory optimization techniques.",

        " memory optimization techniques. "

    ]

    print("Original Memories:")

    for memory in memories:

        print("-", memory)

    compressed = detector.remove_duplicates(memories)

    print("\nAfter Removing Duplicates:")

    for memory in compressed:

        print("-", memory)