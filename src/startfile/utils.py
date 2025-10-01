import os
import platform
import subprocess
import webbrowser
from pathlib import Path
from typing import Union


def startfile(value: Union[str, Path]):
    value = str(value)

    if "://" in value:
        url = value
        return webbrowser.open(url)

    path = value

    return startfile_posix(path) if os.name == "posix" else startfile_windows(path)


def startfile_posix(path):
    command = "open" if platform.system() == "Darwin" else "xdg-open"

    try:
        return subprocess.run(
            (command, path), capture_output=True, check=True, text=True
        )
    except subprocess.CalledProcessError as error:
        message = (
            f"Unable to use {command}"
            if error.returncode == 127
            else f"Unable to open {path}"
        )
        raise FileNotFoundError(message) from error


def startfile_windows(path: str):
    # pylint: disable=no-member
    return os.startfile(path)  # type: ignore
