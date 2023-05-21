import json
from src.classes.alternative import Alternative
from src.classes.alternative_judgment import AlternativeJudgment

boardgames = json.load(open('boardgames.json'))

def getBoardgames():
    alternatives = []

    for index, game in enumerate(boardgames):
        alternative = Alternative(index+1, game['name'])
        alternatives.append(alternative)

    return alternatives

def setCriterion(criteria, dm, alternatives):
    for alternative in alternatives:
        rating = judge(criteria, alternative)
        criteria.add_new_alternative_judgment(AlternativeJudgment(alternative.id, dm.id, rating, rating))

def judge(criteria, alternative):
    if criteria.description == 'cost':
        return judgePrice(boardgames[alternative.id-1]['price'])

    elif criteria.description == 'complexity':
        return boardgames[alternative.id-1]['complexity'] / 2
        
    elif criteria.description == 'players':
        return judgePrice(boardgames[alternative.id-1]['players'])

    elif criteria.description == 'playability':
        return boardgames[alternative.id-1]['playability'] / 2

def judgePrice(price):
    min_value = min(boardgames, key=lambda x:x['price'])['price']
    max_value = max(boardgames, key=lambda x:x['price'])['price']
    rating = 1 + ((price - min_value) * (5 - 1)) / (max_value - min_value)

    return rating
