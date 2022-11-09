from importlib.metadata import PackageNotFoundError, version

from .utils import startfile

try:
    __version__ = version("universal-startfile")
except PackageNotFoundError:
    __version__ = "(local)"

del PackageNotFoundError
del version
