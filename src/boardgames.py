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
        judge(criteria, alternative, dm)

def judge(criteria, alternative, dm):

    game = boardgames[alternative.id-1]

    for index, data in enumerate(game['data']):
        rating = judgeData(game['data'][data], data)
        criteria[index].add_new_alternative_judgment(AlternativeJudgment(alternative.id, dm.id, rating, rating))

    for index, judgement in enumerate(game['judgement']):
        rating = game['judgement'][judgement]
        criteria[index+2].add_new_alternative_judgment(AlternativeJudgment(alternative.id, dm.id, rating[0], rating[1]))

def judgeData(value, data):
    min_value = min(boardgames, key=lambda x:x['data'][data])['data'][data]
    max_value = max(boardgames, key=lambda x:x['data'][data])['data'][data]
    rating = 1 + ((value - min_value) * (5 - 1)) / (max_value - min_value)

    return rating
