from pkg_resources import DistributionNotFound, get_distribution

from .utils import startfile

try:
    __version__ = get_distribution("universal-startfile").version
except DistributionNotFound:
    __version__ = "(local)"

del DistributionNotFound
del get_distribution
