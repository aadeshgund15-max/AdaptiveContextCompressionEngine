"""
Adaptive Context Intelligence Engine (ACIE)
Retrieval Exceptions
"""

from Backend.exceptions.base_exception import ACIEException


# -------------------------------------------------
# Base Retrieval Exception
# -------------------------------------------------

class RetrievalException(ACIEException):

    def __init__(

        self,

        message,

        error_code="RET-000",

        details=None

    ):

        super().__init__(

            message=message,

            module="Retrieval System",

            error_code=error_code,

            details=details

        )


# -------------------------------------------------
# Vector Retrieval
# -------------------------------------------------

class VectorRetrievalException(RetrievalException):

    def __init__(

        self,

        message="Vector retrieval failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="RET-001",

            details=details

        )


# -------------------------------------------------
# Hybrid Retrieval
# -------------------------------------------------

class HybridRetrievalException(RetrievalException):

    def __init__(

        self,

        message="Hybrid retrieval failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="RET-002",

            details=details

        )


# -------------------------------------------------
# Graph Retrieval
# -------------------------------------------------

class GraphRetrievalException(RetrievalException):

    def __init__(

        self,

        message="Knowledge graph retrieval failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="RET-003",

            details=details

        )


# -------------------------------------------------
# Embedding
# -------------------------------------------------

class EmbeddingException(RetrievalException):

    def __init__(

        self,

        message="Embedding generation failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="RET-004",

            details=details

        )


# -------------------------------------------------
# FAISS
# -------------------------------------------------

class FAISSException(RetrievalException):

    def __init__(

        self,

        message="FAISS search failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="RET-005",

            details=details

        )


# -------------------------------------------------
# Ranking
# -------------------------------------------------

class RankingException(RetrievalException):

    def __init__(

        self,

        message="Memory ranking failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="RET-006",

            details=details

        )


# -------------------------------------------------
# Context Window
# -------------------------------------------------

class ContextWindowException(RetrievalException):

    def __init__(

        self,

        message="Context window construction failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="RET-007",

            details=details

        )


# -------------------------------------------------
# Example
# -------------------------------------------------

if __name__ == "__main__":

    try:

        raise HybridRetrievalException(

            details={

                "query":

                "Explain ACIE"

            }

        )

    except RetrievalException as error:

        print()

        print(error)

        print()

        print(error.to_dict())