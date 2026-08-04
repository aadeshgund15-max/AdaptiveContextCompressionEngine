"""
Adaptive Context Intelligence Engine (ACIE)
Memory Exceptions
"""

from Backend.exceptions.base_exception import ACIEException


# -------------------------------------------------
# Base Memory Exception
# -------------------------------------------------

class MemoryException(ACIEException):

    def __init__(

        self,

        message,

        error_code="MEM-000",

        details=None

    ):

        super().__init__(

            message=message,

            module="Memory System",

            error_code=error_code,

            details=details

        )


# -------------------------------------------------
# Memory Storage
# -------------------------------------------------

class MemoryStorageException(MemoryException):

    def __init__(

        self,

        message="Failed to store memory.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="MEM-001",

            details=details

        )


# -------------------------------------------------
# Memory Retrieval
# -------------------------------------------------

class MemoryRetrievalException(MemoryException):

    def __init__(

        self,

        message="Failed to retrieve memory.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="MEM-002",

            details=details

        )


# -------------------------------------------------
# Memory Compression
# -------------------------------------------------

class MemoryCompressionException(MemoryException):

    def __init__(

        self,

        message="Memory compression failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="MEM-003",

            details=details

        )


# -------------------------------------------------
# Memory Reflection
# -------------------------------------------------

class MemoryReflectionException(MemoryException):

    def __init__(

        self,

        message="Reflection engine failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="MEM-004",

            details=details

        )


# -------------------------------------------------
# Knowledge Graph
# -------------------------------------------------

class KnowledgeGraphException(MemoryException):

    def __init__(

        self,

        message="Knowledge graph operation failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="MEM-005",

            details=details

        )


# -------------------------------------------------
# Working Memory
# -------------------------------------------------

class WorkingMemoryException(MemoryException):

    def __init__(

        self,

        message="Working memory operation failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="MEM-006",

            details=details

        )


# -------------------------------------------------
# Long-Term Memory
# -------------------------------------------------

class LongTermMemoryException(MemoryException):

    def __init__(

        self,

        message="Long-term memory operation failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="MEM-007",

            details=details

        )


# -------------------------------------------------
# Example
# -------------------------------------------------

if __name__ == "__main__":

    try:

        raise MemoryStorageException(

            details={

                "database":

                "acie_memory.db"

            }

        )

    except MemoryException as error:

        print()

        print(error)

        print()

        print(error.to_dict())
        