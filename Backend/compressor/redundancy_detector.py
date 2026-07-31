"""
Adaptive Context Intelligence Engine (ACIE)
Redundancy Detector
"""


class RedundancyDetector:
    """
    Removes duplicate sentences while preserving order.
    """

    def __init__(self):
        pass

    def remove_duplicates(self, sentences):

        unique_sentences = []
        seen = set()

        for sentence in sentences:

            cleaned = sentence.strip()

            if cleaned and cleaned not in seen:

                seen.add(cleaned)
                unique_sentences.append(cleaned)

        return unique_sentences


if __name__ == "__main__":

    detector = RedundancyDetector()

    sample = [

        "Vector databases store embeddings.",

        "Embeddings improve semantic search.",

        "Vector databases store embeddings.",

        "Adaptive Context Compression reduces tokens.",

        "Embeddings improve semantic search."

    ]

    print("Original Sentences:\n")

    for sentence in sample:
        print("-", sentence)

    result = detector.remove_duplicates(sample)

    print("\nAfter Removing Duplicates:\n")

    for sentence in result:
        print("-", sentence)