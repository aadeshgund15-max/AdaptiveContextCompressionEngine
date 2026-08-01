"""
Adaptive Context Intelligence Engine (ACIE)
Episodic Memory Engine
"""

from datetime import datetime


class EpisodicMemory:

    def __init__(self):

        self.episodes = []

    def create_episode(

        self,

        query,

        conversation,

        documents,

        importance,

        confidence,

        decision,

        outcome

    ):

        episode = {

            "episode_id": len(self.episodes) + 1,

            "timestamp": datetime.now().isoformat(),

            "query": query,

            "conversation": conversation,

            "documents": documents,

            "importance": importance,

            "confidence": confidence,

            "decision": decision,

            "outcome": outcome

        }

        self.episodes.append(

            episode

        )

        return episode

    def get_episode(self, episode_id):

        for episode in self.episodes:

            if episode["episode_id"] == episode_id:

                return episode

        return None

    def get_all_episodes(self):

        return self.episodes

    def total_episodes(self):

        return len(self.episodes)

    def search(self, keyword):

        results = []

        keyword = keyword.lower()

        for episode in self.episodes:

            if keyword in episode["query"].lower():

                results.append(

                    episode

                )

        return results

    def print_episode(self, episode):

        print("\n==============================")

        print("Episode ID :", episode["episode_id"])

        print("Timestamp  :", episode["timestamp"])

        print("Query      :", episode["query"])

        print("Importance :", episode["importance"])

        print("Confidence :", episode["confidence"])

        print("Decision   :", episode["decision"])

        print("Outcome    :", episode["outcome"])

        print("==============================")

    def print_all(self):

        print("\n========== EPISODIC MEMORY ==========\n")

        for episode in self.episodes:

            self.print_episode(

                episode

            )


if __name__ == "__main__":

    memory = EpisodicMemory()

    memory.create_episode(

        query="Explain vector databases.",

        conversation=[

            "What are embeddings?",

            "Explain semantic search."

        ],

        documents=[

            "Paper A",

            "Paper B"

        ],

        importance=92,

        confidence=0.96,

        decision="STORE",

        outcome="Stored Successfully"

    )

    memory.create_episode(

        query="Explain context compression.",

        conversation=[

            "Why compress context?"

        ],

        documents=[

            "Research Paper"

        ],

        importance=88,

        confidence=0.93,

        decision="STORE",

        outcome="Stored Successfully"

    )

    memory.print_all()

    print("\nTotal Episodes :")

    print(

        memory.total_episodes()

    )

    print("\nSearch Results :")

    print(

        memory.search(

            "vector"

        )

    )