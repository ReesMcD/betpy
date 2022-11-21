
def no_vig_fair_odds(odds_one: int, odds_two: int) -> list:
    print('no_vig_line')
    prob_one = implied_probability(odds_one);
    prob_two = implied_probability(odds_two);
    total_prob = prob_one + prob_two
    return {
        'odds_one': prob_one / total_prob,
        'odds_two': prob_two / total_prob
    }


def implied_probability(american_odds: int) -> float:
    odds = american_odds_to_decimal(american_odds)
    return (1 / odds) * 100

def american_odds_to_decimal(american_odds: int) -> float:
    if american_odds >= 0:
        return positive_american_odds_to_decimal(american_odds)

    if american_odds < 0:
        return negative_american_odds_to_decimal(american_odds)


def positive_american_odds_to_decimal(american_odds: int) -> float:
    return 1 + (american_odds / 100)


def negative_american_odds_to_decimal(american_odds: int) -> float:
    return 1 - (100 / american_odds)
