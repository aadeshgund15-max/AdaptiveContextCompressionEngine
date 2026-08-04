"""
Adaptive Context Intelligence Engine (ACIE)
Provider Exceptions
"""


class ProviderError(Exception):
    """Base provider exception."""
    pass


class AuthenticationError(ProviderError):
    """Raised when API authentication fails."""
    pass


class InvalidAPIKeyError(AuthenticationError):
    """Raised when an API key is missing or invalid."""
    pass


class RateLimitError(ProviderError):
    """Raised when the provider rate limit is exceeded."""
    pass


class ModelNotFoundError(ProviderError):
    """Raised when the requested model is unavailable."""
    pass


class ConnectionError(ProviderError):
    """Raised when the provider cannot be reached."""
    pass


class ResponseError(ProviderError):
    """Raised when the provider returns an invalid response."""
    pass