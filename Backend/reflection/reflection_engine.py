"""
Adaptive Context Intelligence Engine (ACIE)
Reflection Engine
"""

from datetime import datetime


class ReflectionEngine:

    def __init__(self):

        self.duplicate_threshold = 2

        self.low_importance_threshold = 40

        self.frequent_access_threshold = 10

    def find_duplicates(self, memories):

        seen = {}

        duplicates = []

        for memory in memories:

            text = memory["query"].strip().lower()

            if text in seen:

                duplicates.append(memory)

            else:

                seen[text] = memory

        return duplicates

    def find_low_priority(self, memories):

        results = []

        for memory in memories:

            if memory["importance"] < self.low_importance_threshold:

                results.append(memory)

        return results

    def find_frequently_used(self, memories):

        results = []

        for memory in memories:

            if memory["access_count"] >= self.frequent_access_threshold:

                results.append(memory)

        return results

    def find_archivable(self, memories):

        results = []

        today = datetime.now()

        for memory in memories:

            last = datetime.strptime(
                memory["last_accessed"],
                "%Y-%m-%d %H:%M:%S"
            )

            days = (today - last).days

            if days >= 30:

                results.append(memory)

        return results

    def generate_report(self, memories):

        duplicates = self.find_duplicates(memories)

        low_priority = self.find_low_priority(memories)

        frequent = self.find_frequently_used(memories)

        archived = self.find_archivable(memories)

        return {

            "total_memories": len(memories),

            "duplicates": len(duplicates),

            "low_priority": len(low_priority),

            "frequently_used": len(frequent),

            "archivable": len(archived),

            "duplicate_memories": duplicates,

            "low_priority_memories": low_priority,

            "frequently_used_memories": frequent,

            "archivable_memories": archived

        }

    def reflect(self, memories):

        print("\n========== Reflection Report ==========\n")

        report = self.generate_report(memories)

        print("Total Memories :", report["total_memories"])

        print("Duplicates :", report["duplicates"])

        print("Low Priority :", report["low_priority"])

        print("Frequently Used :", report["frequently_used"])

        print("Archivable :", report["archivable"])

        return report


if __name__ == "__main__":

    sample_memories = [

        {
            "query": "Explain vector databases.",

            "importance": 92,

            "access_count": 18,

            "last_accessed": "2026-07-30 10:00:00"
        },

        {
            "query": "Explain vector databases.",

            "importance": 91,

            "access_count": 5,

            "last_accessed": "2026-06-01 09:00:00"
        },

        {
            "query": "Introduction to SQL",

            "importance": 22,

            "access_count": 1,

            "last_accessed": "2026-05-01 08:00:00"
        }

    ]

    engine = ReflectionEngine()

    engine.reflect(sample_memories)