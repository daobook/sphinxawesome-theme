"""Test utility functions."""
from pathlib import Path
from typing import Union

from bs4 import BeautifulSoup


def parse_html(filename: Union[Path, str]) -> BeautifulSoup:
    """Parse an HTML file into a BeautifulSoup tree."""
    with open(filename) as file_handle:
        tree = BeautifulSoup(file_handle, "html.parser")
    return tree


def read_as_text(filename: Union[Path, str]) -> str:
    """Read a file as text."""
    return Path(filename).read_text()
