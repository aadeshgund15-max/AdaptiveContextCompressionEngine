"""
Adaptive Context Intelligence Engine (ACIE)
Inference Engine
"""


class InferenceEngine:

    def __init__(self):

        pass

    # ---------------------------------
    # Extract Facts
    # ---------------------------------

    def extract_facts(self, reasoning):

        context = reasoning["context"]

        facts = []

        for line in context.split("\n"):

            line = line.strip()

            if line:

                facts.append(

                    line.replace("- ", "")

                )

        return facts

    # ---------------------------------
    # Detect Missing Information
    # ---------------------------------

    def detect_gaps(self, facts):

        gaps = []

        if len(facts) == 0:

            gaps.append(

                "No supporting memories found."

            )

        if len(facts) < 3:

            gaps.append(

                "Limited evidence available."

            )

        return gaps

    # ---------------------------------
    # Generate Inference
    # ---------------------------------

    def infer(

        self,

        query,

        facts,

        gaps

    ):

        confidence = 0.5

        if len(facts) >= 3:

            confidence = 0.90

        elif len(facts) == 2:

            confidence = 0.75

        elif len(facts) == 1:

            confidence = 0.60

        return {

            "query": query,

            "facts": facts,

            "knowledge_gaps": gaps,

            "confidence": confidence,

            "conclusion":

                "Inference generated using retrieved evidence."

        }

    # ---------------------------------
    # Complete Pipeline
    # ---------------------------------

    def process(

        self,

        reasoning

    ):

        print("\n========== INFERENCE ENGINE ==========\n")

        facts = self.extract_facts(

            reasoning

        )

        gaps = self.detect_gaps(

            facts

        )

        inference = self.infer(

            reasoning["query"],

            facts,

            gaps

        )

        return inference


if __name__ == "__main__":

    reasoning = {

        "query":

            "Explain Adaptive Context Compression",

        "context":

            "- Adaptive Context Compression reduces token usage.\n"

            "- Semantic Retrieval improves search.\n"

            "- Knowledge Graph links memories.\n"

    }

    engine = InferenceEngine()

    result = engine.process(

        reasoning

    )

    print("\n========== RESULT ==========\n")

    print(result)