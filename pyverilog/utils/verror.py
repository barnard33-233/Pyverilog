class PyvError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message="PyvError"):
        self.message = message
        super().__init__(self.message)


class ImplementationError(PyvError):
    """Raised when an unimplemented feature is encountered."""

    def __init__(self, message="ImplementationError"):
        super().__init__(message)


class FormatError(PyvError):
    """Raised when an unsupported format is encountered."""

    def __init__(self, message="FormatError"):
        super().__init__(message)


class DefinitionError(PyvError):
    """Raised when an undefined or invalid scope type is encountered."""

    def __init__(self, message="DefinitionError"):
        super().__init__(message)
