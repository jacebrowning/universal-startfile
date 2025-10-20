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

    if platform.system() == "Darwin":
        return startfile_macos(path)

    if platform.system() == "Windows":
        return startfile_windows(path)

    return startfile_linux(path)


def startfile_command(command: str, path: str):
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


def startfile_linux(path: str):
    return startfile_command("xdg-open", path)


def startfile_macos(path: str):
    return startfile_command("open", path)


def startfile_windows(path: str):
    # pylint: disable=no-member
    return os.startfile(path)  # type: ignore
