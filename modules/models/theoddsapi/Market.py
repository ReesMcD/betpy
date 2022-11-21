from typing import List
from modules.models.theoddsapi.Outcome import Outcome

class Market:
    def __init__(self, key: str, outcomes: List[Outcome]):
        self.key = key
        self.outcomes = outcomes
