"""
Adaptive Context Intelligence Engine (ACIE)
Reasoning Engine
"""

from Backend.reasoning.decision_tree import DecisionTree
from Backend.reasoning.planner import Planner
from Backend.reasoning.chain_of_thought import ChainOfThought
from Backend.reasoning.reflection_reasoner import ReflectionReasoner
from Backend.reasoning.verifier import Verifier
from Backend.reasoning.self_critique import SelfCritique

from Backend.data_structures.stack import Stack


class ReasoningEngine:

    def __init__(self):

        self.decision_tree = DecisionTree()

        self.planner = Planner()

        self.chain_of_thought = ChainOfThought()

        self.reflection = ReflectionReasoner()

        self.verifier = Verifier()

        self.self_critique = SelfCritique()

        # DSA : Stack
        self.reasoning_stack = Stack()

    # -------------------------------------------------

    def process(

        self,

        query,

        retrieved_memories,

        draft_response

    ):

        print("\n========== REASONING ENGINE ==========\n")

        self.reasoning_stack.clear()

        # --------------------------------
        # Decision Tree
        # --------------------------------

        self.reasoning_stack.push("Decision Tree")

        strategy = self.decision_tree.decide(

            query

        )

        # --------------------------------
        # Planning
        # --------------------------------

        self.reasoning_stack.push("Planner")

        plan = self.planner.create_plan(

            query

        )

        # --------------------------------
        # Chain of Thought
        # --------------------------------

        self.reasoning_stack.push("Chain Of Thought")

        reasoning = self.chain_of_thought.reason(

            query,

            retrieved_memories

        )

        # --------------------------------
        # Reflection
        # --------------------------------

        self.reasoning_stack.push("Reflection")

        reflection = self.reflection.reflect(

            reasoning

        )

        # --------------------------------
        # Verification
        # --------------------------------

        self.reasoning_stack.push("Verification")

        verification = self.verifier.verify(

            reasoning,

            retrieved_memories

        )

        # --------------------------------
        # Self Critique
        # --------------------------------

        self.reasoning_stack.push("Self Critique")

        critique = self.self_critique.critique(

            draft_response,

            verification

        )

        # --------------------------------

        reasoning_trace = self.reasoning_stack.to_list()

        return {

            "strategy": strategy,

            "plan": plan["plan"],

            "reasoning": reasoning,

            "reflection": reflection,

            "verification": verification,

            "critique": critique,

            "reasoning_trace": reasoning_trace

        }

    # -------------------------------------------------
    # Display Reasoning Stack
    # -------------------------------------------------

    def show_reasoning_trace(self):

        self.reasoning_stack.display()


if __name__ == "__main__":

    engine = ReasoningEngine()

    memories = [

        {

            "query":

            "Adaptive Context Compression"

        },

        {

            "query":

            "Semantic Retrieval"

        }

    ]

    response = (

        "Adaptive Context Compression "

        "reduces token usage while "

        "preserving important information."

    )

    result = engine.process(

        query="Explain Adaptive Context Compression.",

        retrieved_memories=memories,

        draft_response=response

    )

    print("\n========== RESULT ==========\n")

    print(result)

    print("\n========== REASONING STACK ==========\n")

    engine.show_reasoning_trace()