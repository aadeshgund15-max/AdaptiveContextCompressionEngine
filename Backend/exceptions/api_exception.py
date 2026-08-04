"""
Adaptive Context Intelligence Engine (ACIE)
API Exceptions
"""

from Backend.exceptions.base_exception import ACIEException


# -------------------------------------------------
# Base API Exception
# -------------------------------------------------

class APIException(ACIEException):

    def __init__(

        self,

        message,

        error_code="API-000",

        details=None

    ):

        super().__init__(

            message=message,

            module="FastAPI",

            error_code=error_code,

            details=details

        )


# -------------------------------------------------
# Validation
# -------------------------------------------------

class ValidationException(APIException):

    def __init__(

        self,

        message="Validation failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="API-001",

            details=details

        )


# -------------------------------------------------
# Authentication
# -------------------------------------------------

class AuthenticationException(APIException):

    def __init__(

        self,

        message="Authentication failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="API-002",

            details=details

        )


# -------------------------------------------------
# Authorization
# -------------------------------------------------

class AuthorizationException(APIException):

    def __init__(

        self,

        message="Authorization failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="API-003",

            details=details

        )


# -------------------------------------------------
# Request
# -------------------------------------------------

class RequestException(APIException):

    def __init__(

        self,

        message="Invalid request.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="API-004",

            details=details

        )


# -------------------------------------------------
# Pipeline
# -------------------------------------------------

class PipelineException(APIException):

    def __init__(

        self,

        message="Pipeline execution failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="API-005",

            details=details

        )


# -------------------------------------------------
# Endpoint
# -------------------------------------------------

class EndpointException(APIException):

    def __init__(

        self,

        message="Endpoint execution failed.",

        details=None

    ):

        super().__init__(

            message=message,

            error_code="API-006",

            details=details

        )


# -------------------------------------------------
# Example
# -------------------------------------------------

if __name__ == "__main__":

    try:

        raise PipelineException(

            details={

                "endpoint": "/chat"

            }

        )

    except APIException as error:

        print()

        print(error)

        print()

        print(error.to_dict())