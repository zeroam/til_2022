from typing import Any

from bs4 import BeautifulSoup


class XMLAdapter:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.soup = soup

    def get(self, key: str, default: Any = None) -> Any | None:
        value = self.soup.find(key)
        if value:
            return value.get_text()
        return default
