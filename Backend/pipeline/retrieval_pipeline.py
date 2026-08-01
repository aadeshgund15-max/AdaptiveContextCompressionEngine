"""
Adaptive Context Intelligence Engine (ACIE)
Retrieval Pipeline
"""

from Backend.query_expansion.query_expander import QueryExpander
from Backend.hybrid.hybrid_retriever import HybridRetriever
from Backend.graph_retriever.graph_retriever import GraphRetriever
from Backend.multi_hop.multi_hop_retriever import MultiHopRetriever
from Backend.retrieval_ranking.retrieval_ranker import RetrievalRanker
from Backend.fusion.context_fusion import ContextFusion
from Backend.context_builder.context_window_builder import ContextWindowBuilder

from Backend.retrieval.retrieval_result import RetrievalResult


class RetrievalPipeline:

    def __init__(self):

        self.query_expander = QueryExpander()

        self.hybrid_retriever = HybridRetriever()

        self.graph_retriever = GraphRetriever()

        self.multi_hop = MultiHopRetriever()

        self.ranker = RetrievalRanker()

        self.fusion = ContextFusion()

        self.context_builder = ContextWindowBuilder()

    # ---------------------------------
    # Complete Retrieval Pipeline
    # ---------------------------------

    def retrieve(

        self,

        query,

        memories,

        token_budget=100

    ):

        print("\n========== RETRIEVAL PIPELINE ==========\n")

        # -------------------------------
        # Query Expansion
        # -------------------------------

        expanded_queries = self.query_expander.expand(

            query

        )

        # -------------------------------
        # Hybrid Retrieval
        # -------------------------------

        hybrid_results = self.hybrid_retriever.retrieve(

            query,

            top_k=5

        )

        # -------------------------------
        # Graph Retrieval
        # -------------------------------

        graph_results = self.graph_retriever.retrieve(

            query,

            memories,

            top_k=5

        )

        ranked_memories = graph_results["expanded_memories"]

        # -------------------------------
        # Multi-Hop Retrieval
        # -------------------------------

        graph = {}

        for memory in ranked_memories:

            graph[memory["query"]] = []

        self.multi_hop.load_graph(

            graph

        )

        multi_hop = self.multi_hop.retrieve(

            start_node=query,

            max_hops=2

        )

        # -------------------------------
        # Ranking
        # -------------------------------

        ranked = self.ranker.rank(

            ranked_memories

        )

        # -------------------------------
        # Context Fusion
        # -------------------------------

        fusion_input = []

        for memory in ranked:

            fusion_input.append(

                {

                    "text": memory["query"],

                    "ranking_score": memory["ranking_score"]

                }

            )

        fusion = self.fusion.fuse(

            fusion_input

        )

        # -------------------------------
        # Context Window
        # -------------------------------

        context_window = self.context_builder.build(

            fusion["fused_context"],

            token_budget

        )

        # -------------------------------
        # Final Result
        # -------------------------------

        result = RetrievalResult(

            query=query,

            expanded_queries=expanded_queries,

            retrieved_memories=hybrid_results,

            ranked_memories=ranked,

            fused_context=fusion["fused_context"],

            context_window=context_window

        )

        return result.to_dict()


if __name__ == "__main__":

    memories = [

        {

            "id": 1,

            "query": "Adaptive Context Compression",

            "importance": 95,

            "confidence": 0.94,

            "decision": "STORE",

            "created_at": "",

            "last_accessed": "",

            "access_count": 1,

            "state": "ACTIVE",

            "ranking_score": 77

        },

        {

            "id": 2,

            "query": "Semantic Retrieval",

            "importance": 90,

            "confidence": 0.91,

            "decision": "STORE",

            "created_at": "",

            "last_accessed": "",

            "access_count": 1,

            "state": "ACTIVE",

            "ranking_score": 74

        }

    ]

    pipeline = RetrievalPipeline()

    result = pipeline.retrieve(

        query="Adaptive Context Compression",

        memories=memories,

        token_budget=100

    )

    print("\n========== RESULT ==========\n")

    print(result)