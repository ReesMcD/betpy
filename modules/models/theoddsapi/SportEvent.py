from typing import List
from modules.models.theoddsapi.Bookmaker import Bookmaker

class SportEvent:
    def __init__(self, id: str, sport_key: str, sport_title: str, commence_time: str, home_team: str, away_team: str, bookmakers: List[Bookmaker]):
        self.id = id
        self.sport_key = sport_key
        self.sport_title = sport_title
        self.commence_time = commence_time
        self.home_team = home_team
        self.away_team = away_team
        self.bookmakers = bookmakers
