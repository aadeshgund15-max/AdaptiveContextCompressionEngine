"""
Adaptive Context Intelligence Engine (ACIE)
Retrieval Result Model
"""


class RetrievalResult:

    def __init__(

        self,

        query,

        expanded_queries=None,

        retrieved_memories=None,

        ranked_memories=None,

        fused_context=None,

        context_window=None

    ):

        self.query = query

        self.expanded_queries = expanded_queries or []

        self.retrieved_memories = retrieved_memories or []

        self.ranked_memories = ranked_memories or []

        self.fused_context = fused_context or []

        self.context_window = context_window or {}

    def to_dict(self):

        return {

            "query": self.query,

            "expanded_queries": self.expanded_queries,

            "retrieved_memories": self.retrieved_memories,

            "ranked_memories": self.ranked_memories,

            "fused_context": self.fused_context,

            "context_window": self.context_window

        }