"""
Adaptive Context Intelligence Engine (ACIE)
LLM Exceptions
"""

from Backend.exceptions.base_exception import ACIEException


# -------------------------------------------------
# Base LLM Exception
# -------------------------------------------------

class LLMException(ACIEException):

    def __init__(

        self,

        message,

        error_code="LLM-000",

        details=None

    ):

        super().__init__(

            message=message,

            module="LLM System",

            error_code=error_code,

            details=details

        )


# -------------------------------------------------
# Provider
# -------------------------------------------------

class ProviderException(LLMException):

    def __init__(

        self,

        message="LLM provider error.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="LLM-001",

            details=details

        )


# -------------------------------------------------
# API Key
# -------------------------------------------------

class APIKeyException(LLMException):

    def __init__(

        self,

        message="API key is missing or invalid.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="LLM-002",

            details=details

        )


# -------------------------------------------------
# Prompt Builder
# -------------------------------------------------

class PromptBuilderException(LLMException):

    def __init__(

        self,

        message="Prompt construction failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="LLM-003",

            details=details

        )


# -------------------------------------------------
# Generation
# -------------------------------------------------

class GenerationException(LLMException):

    def __init__(

        self,

        message="Text generation failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="LLM-004",

            details=details

        )


# -------------------------------------------------
# Response Parser
# -------------------------------------------------

class ResponseParserException(LLMException):

    def __init__(

        self,

        message="Response parsing failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="LLM-005",

            details=details

        )


# -------------------------------------------------
# Router
# -------------------------------------------------

class RouterException(LLMException):

    def __init__(

        self,

        message="Model routing failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="LLM-006",

            details=details

        )


# -------------------------------------------------
# Token Budget
# -------------------------------------------------

class TokenBudgetException(LLMException):

    def __init__(

        self,

        message="Token budget exceeded.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="LLM-007",

            details=details

        )


# -------------------------------------------------
# Example
# -------------------------------------------------

if __name__ == "__main__":

    try:

        raise ProviderException(

            details={

                "provider": "Groq",

                "model": "llama-3.3-70b"

            }

        )

    except LLMException as error:

        print()

        print(error)

        print()

        print(error.to_dict())