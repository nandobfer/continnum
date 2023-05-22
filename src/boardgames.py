import json
from src.classes.alternative import Alternative
from src.classes.alternative_judgment import AlternativeJudgment
from src.enumerations.criterion_type import CriterionType
from src.classes.criterion import Criterion
from src.classes.criterion_judgment import CriterionJudgment

boardgames = json.load(open('boardgames.json'))
criteria = json.load(open('criteria.json'))
_criteria = []

def getBoardgames():
    alternatives = []

    for index, game in enumerate(boardgames):
        alternative = Alternative(index+1, game['name'])
        alternatives.append(alternative)

    return alternatives

def getCriteria():
    for index, criterion in enumerate(criteria):
        cri = Criterion(index+1, criterion['name'], CriterionType.COST if criterion['type'] == 'COST' else CriterionType.BENEFIT)
        _criteria.append(cri)

    return _criteria

def setCriteria(dm):
    for index, criterion in enumerate(_criteria):
        rating = criteria[index]['weight'][dm.id-1]
        dm.add_new_criterion_judgment(CriterionJudgment(criterion.id, rating[0], rating[1]))

def judge(criteria: list[Criterion], dm, alternatives):
    print(f'dm{dm.id}:')
    for alternative in alternatives:
        game = boardgames[alternative.id-1]
        print(game['name'])

        for index, data in enumerate(game['data']):
            rating = judgeData(game['data'][data], data, index)
            # print(f"data_name: {data}, data_value: {game['data'][data]}, rating: {rating}")
            criteria[index].add_new_alternative_judgment(AlternativeJudgment(alternative.id, dm.id, rating, rating))
            print({data: [criteria[index].alternative_judgments[-1].min_value, criteria[index].alternative_judgments[-1].max_value]})

        for index, judgement in enumerate(game['judgement']):
            rating = game['judgement'][judgement][dm.id-1]
            criteria[index+2].add_new_alternative_judgment(AlternativeJudgment(alternative.id, dm.id, rating[0], rating[1]))
            print({judgement: [criteria[index].alternative_judgments[-1].min_value, criteria[index].alternative_judgments[-1].max_value]})
            print(f'should be {rating}')
        
        print('')

def judgeData(value, data, benefit):
    min_value = min(boardgames, key=lambda x:x['data'][data])['data'][data]
    max_value = max(boardgames, key=lambda x:x['data'][data])['data'][data]

    rating = 0
    if benefit:
        rating = 1 + ((value - min_value) * (5 - 1)) / (max_value - min_value)
    else:
        rating = 5 - ((value - min_value) * (5 - 1)) / (max_value - min_value)
    

    return rating

