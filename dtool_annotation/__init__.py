"""dtool_annotation package."""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("dtool-annotation")
except PackageNotFoundError:
    # Package is not installed.
    __version__ = "unknown"
