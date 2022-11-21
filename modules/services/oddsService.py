import requests


def getOdds(sport):
    URL = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=6170065581e09cf0f220b220b090e51a&regions=us&markets=h2h,spreads,totals&oddsFormat=decimal"
    r = requests.get(url=URL)
    return r.json()
