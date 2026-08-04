"""
Adaptive Context Intelligence Engine (ACIE)
Reasoning Exceptions
"""

from Backend.exceptions.base_exception import ACIEException


# -------------------------------------------------
# Base Reasoning Exception
# -------------------------------------------------

class ReasoningException(ACIEException):

    def __init__(

        self,

        message,

        error_code="REA-000",

        details=None

    ):

        super().__init__(

            message=message,

            module="Reasoning Engine",

            error_code=error_code,

            details=details

        )


# -------------------------------------------------
# Planner
# -------------------------------------------------

class PlanningException(ReasoningException):

    def __init__(

        self,

        message="Planning failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="REA-001",

            details=details

        )


# -------------------------------------------------
# Chain of Thought
# -------------------------------------------------

class ChainOfThoughtException(ReasoningException):

    def __init__(

        self,

        message="Chain of Thought execution failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="REA-002",

            details=details

        )


# -------------------------------------------------
# Reflection
# -------------------------------------------------

class ReflectionException(ReasoningException):

    def __init__(

        self,

        message="Reflection failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="REA-003",

            details=details

        )


# -------------------------------------------------
# Verification
# -------------------------------------------------

class VerificationException(ReasoningException):

    def __init__(

        self,

        message="Verification failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="REA-004",

            details=details

        )


# -------------------------------------------------
# Self Critique
# -------------------------------------------------

class SelfCritiqueException(ReasoningException):

    def __init__(

        self,

        message="Self critique failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="REA-005",

            details=details

        )


# -------------------------------------------------
# Decision Tree
# -------------------------------------------------

class DecisionTreeException(ReasoningException):

    def __init__(

        self,

        message="Decision tree execution failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="REA-006",

            details=details

        )


# -------------------------------------------------
# Strategy Selection
# -------------------------------------------------

class StrategyException(ReasoningException):

    def __init__(

        self,

        message="Reasoning strategy selection failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="REA-007",

            details=details

        )


# -------------------------------------------------
# Example
# -------------------------------------------------

if __name__ == "__main__":

    try:

        raise PlanningException(

            details={

                "query":

                "Explain Adaptive Context Compression"

            }

        )

    except ReasoningException as error:

        print()

        print(error)

        print()

        print(error.to_dict())