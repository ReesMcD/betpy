from typing import List
from modules.models.theoddsapi.Market import Market

class Bookmaker:
    def __init__(self, key: str, title: str, last_update: str, markets: List[Market]):
        self.key = key
        self.title = title
        self.last_update = last_update
        self.markets = markets
