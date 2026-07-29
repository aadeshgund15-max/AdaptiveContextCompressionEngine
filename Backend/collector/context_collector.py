"""
Adaptive Context Intelligence Engine (ACIE)
Context Collector Module
"""

from datetime import datetime


class ContextCollector:
    """
    Collects and organizes context from different sources.
    """

    def __init__(self):
        self.context = {}

    def collect(self, query, conversation=None, documents=None):
        """
        Collect context information.

        Parameters:
            query (str): User query
            conversation (list): Previous conversation history
            documents (list): Retrieved documents

        Returns:
            dict: Structured context object
        """

        if conversation is None:
            conversation = []

        if documents is None:
            documents = []

        self.context = {
            "query": query,
            "conversation": conversation,
            "documents": documents,
            "timestamp": datetime.now().isoformat()
        }

        return self.context


if __name__ == "__main__":

    collector = ContextCollector()

    context = collector.collect(
        query="Explain context compression.",
        conversation=[
            "What is Retrieval-Augmented Generation?"
        ],
        documents=[
            "Research Paper A",
            "Research Paper B"
        ]
    )

    print(context)