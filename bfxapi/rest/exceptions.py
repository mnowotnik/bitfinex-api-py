from .. exceptions import BfxBaseException

__all__ = [
    "BfxRestException",

    "RequestParametersError",
    "ResourceNotFound",
    "InvalidAuthenticationCredentials"
]

class BfxRestException(BfxBaseException):
    """
    Base class for all custom exceptions in bfxapi/rest/exceptions.py.
    """

    pass

class ResourceNotFound(BfxRestException):
    """
    This error indicates a failed HTTP request to a non-existent resource.
    """

    pass

class RequestParametersError(BfxRestException):
    """
    This error indicates that there are some invalid parameters sent along with an HTTP request.
    """

    pass

class InvalidAuthenticationCredentials(BfxRestException):
    """
    This error indicates that the user has provided incorrect credentials (API-KEY and API-SECRET) for authentication.
    """

    pass

class UnknownGenericError(BfxRestException):
    """
    This error indicates an undefined problem processing an HTTP request sent to the APIs.
    """

    pass