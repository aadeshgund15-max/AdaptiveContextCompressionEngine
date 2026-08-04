"""
Adaptive Context Intelligence Engine (ACIE)
Request Processor
"""

import re
from datetime import datetime


class RequestProcessor:

    def __init__(self):

        self.intent_keywords = {

            "coding": [
                "code",
                "python",
                "java",
                "c++",
                "bug",
                "error",
                "program",
                "algorithm",
                "function",
                "class"
            ],

            "math": [
                "solve",
                "equation",
                "integral",
                "derivative",
                "matrix",
                "probability",
                "statistics"
            ],

            "research": [
                "research",
                "paper",
                "survey",
                "compare",
                "analysis",
                "study"
            ],

            "vision": [
                "image",
                "photo",
                "picture",
                "diagram",
                "ocr",
                "detect"
            ],

            "browser": [
                "search",
                "latest",
                "news",
                "internet",
                "website",
                "online"
            ],

            "memory": [
                "remember",
                "recall",
                "previous",
                "history"
            ]

        }

    # --------------------------------------------------
    # Clean Query
    # --------------------------------------------------

    def clean_query(self, query):

        query = query.strip()

        query = re.sub(r"\s+", " ", query)

        return query

    # --------------------------------------------------
    # Detect Intent
    # --------------------------------------------------

    def detect_intent(self, query):

        text = query.lower()

        scores = {}

        for intent, keywords in self.intent_keywords.items():

            score = 0

            for keyword in keywords:

                if keyword in text:

                    score += 1

            scores[intent] = score

        best_intent = "general"

        highest = 0

        for intent, score in scores.items():

            if score > highest:

                highest = score

                best_intent = intent

        return best_intent

    # --------------------------------------------------
    # Estimate Complexity
    # --------------------------------------------------

    def estimate_complexity(self, query):

        words = len(query.split())

        if words < 10:
            return "LOW"

        if words < 30:
            return "MEDIUM"

        return "HIGH"

    # --------------------------------------------------
    # Requires Retrieval
    # --------------------------------------------------

    def requires_retrieval(self, intent):

        retrieval_intents = [

            "research",

            "browser",

            "memory"

        ]

        return intent in retrieval_intents

    # --------------------------------------------------
    # Requires Tools
    # --------------------------------------------------

    def requires_tools(self, intent):

        tool_intents = [

            "coding",

            "browser",

            "vision"

        ]

        return intent in tool_intents

    # --------------------------------------------------
    # Process Request
    # --------------------------------------------------

    def process(self, query):

        cleaned = self.clean_query(query)

        intent = self.detect_intent(cleaned)

        complexity = self.estimate_complexity(cleaned)

        return {

            "query": cleaned,

            "intent": intent,

            "complexity": complexity,

            "requires_retrieval": self.requires_retrieval(intent),

            "requires_tools": self.requires_tools(intent),

            "timestamp": datetime.now().isoformat()

        }


if __name__ == "__main__":

    processor = RequestProcessor()

    result = processor.process(

        "Search latest research papers on adaptive context compression"

    )

    print()

    print(result)