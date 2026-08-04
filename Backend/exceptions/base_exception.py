"""
Adaptive Context Intelligence Engine (ACIE)
Base Exception
"""

from __future__ import annotations

from datetime import datetime
from typing import Any


class ACIEException(Exception):
    """
    Base exception for the entire ACIE project.
    Every custom exception should inherit from this class.
    """

    def __init__(
        self,
        message: str,
        *,
        module: str = "Unknown",
        error_code: str = "ACIE-000",
        details: Any = None
    ) -> None:

        super().__init__(message)

        self.message = message
        self.module = module
        self.error_code = error_code
        self.details = details
        self.timestamp = datetime.now()

    # -------------------------------------------------
    # Convert Exception to Dictionary
    # -------------------------------------------------

    def to_dict(self) -> dict:

        return {

            "error": self.__class__.__name__,

            "message": self.message,

            "module": self.module,

            "error_code": self.error_code,

            "details": self.details,

            "timestamp": self.timestamp.isoformat()

        }

    # -------------------------------------------------
    # String Representation
    # -------------------------------------------------

    def __str__(self) -> str:

        return (

            f"[{self.error_code}] "

            f"{self.module}: "

            f"{self.message}"

        )

    # -------------------------------------------------
    # Developer Representation
    # -------------------------------------------------

    def __repr__(self) -> str:

        return (

            f"{self.__class__.__name__}("

            f"message={self.message!r}, "

            f"module={self.module!r}, "

            f"error_code={self.error_code!r}"

            f")"

        )


# -------------------------------------------------
# Example
# -------------------------------------------------

if __name__ == "__main__":

    try:

        raise ACIEException(

            "Embedding model failed to load.",

            module="Embedding Engine",

            error_code="ACIE-001",

            details={

                "model":

                "BAAI/bge-small-en-v1.5"

            }

        )

    except ACIEException as error:

        print()

        print(error)

        print()

        print(error.to_dict())