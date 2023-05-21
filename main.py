from src.classes.decision_maker import DecisionMaker
from src.classes.criterion import Criterion
from src.classes.criterion_judgment import CriterionJudgment
from src.enumerations.criterion_type import CriterionType
from src.classes.model import Model
from src.classes.alternative import Alternative
from src.classes.alternative_judgment import AlternativeJudgment
from src.boardgames import getBoardgames, getCriteria, setCriteria, judge


##################################
# Criação dos objetos no cliente #
##################################

# julgadores
dm1 = DecisionMaker(1, "Dm_1", 0.5)
dm2 = DecisionMaker(2, "Dm_2", 0.5)

# Critérios a serem julgados
cri_custo = Criterion(1, "cost", CriterionType.COST)
cri_complexidade = Criterion(2, "complexity", CriterionType.COST)
cri_jogadores = Criterion(3, "players", CriterionType.BENEFIT)
cri_jogabilidade = Criterion(4, "playability", CriterionType.BENEFIT)

# alternativas
## boardgames.py > getBoardgames()

# Modelinho

# criteria = [cri_custo, cri_jogadores, cri_complexidade, cri_jogabilidade]
criteria = getCriteria()
alternatives = getBoardgames()
decision_makers = [dm1, dm2]
model = Model(5, criteria, alternatives, decision_makers)

#########################################
# Inserção dos julgamentos pelo cliente #
#########################################

# Julgamentos sobre os critérios (linha 21 da tabela)

setCriteria(dm1)
setCriteria(dm2)

# dm1.add_new_criterion_judgment(CriterionJudgment(cri_custo.id, 2, 3))
# dm1.add_new_criterion_judgment(CriterionJudgment(cri_complexidade.id, 2, 3))
# dm1.add_new_criterion_judgment(CriterionJudgment(cri_jogadores.id, 1, 1))
# dm1.add_new_criterion_judgment(CriterionJudgment(cri_jogabilidade.id, 5, 5))

# dm2.add_new_criterion_judgment(CriterionJudgment(cri_custo.id, 3, 4))
# dm2.add_new_criterion_judgment(CriterionJudgment(cri_complexidade.id, 3, 4))
# dm2.add_new_criterion_judgment(CriterionJudgment(cri_jogadores.id, 2, 3))
# dm2.add_new_criterion_judgment(CriterionJudgment(cri_jogabilidade.id, 5, 5))

#################################
# Cálculos feitos pelo servidor #
#################################

# Soluções ideais + e - (linhas 27 e 29 da tabela)

model.calculate_decision_makers_ideal_solution()

# Distâncias positivas e negativas (usadas no cálculo de distâncias)

model.sum_positive_criterion_distance()
model.sum_negative_criterion_distance()

# Normalized CCi

total_normalized_cci = model.calculate_normalized_weight()
#print(total_normalized_cci)

################
# Alternativas #
################

# Julgamentos sobre as alternativas
judge(criteria, dm1, alternatives)
judge(criteria, dm2, alternatives)


# julgamentos agregados
print("Julgamentos agregados")
model.generate_all_aggregated_judgments()

# Soluções ideais
print("SIP e SIN")
model.calculate_criteria_ideal_solution()

print()
print("D+")
model.sum_positive_alternative_distance()
print()
print("D-")
model.sum_negative_alternative_distance()

model.calculate_alternatives_score()

print()
print("Score")
ranking = model.get_alternative_ranking()
for alt in ranking:
  print(alt.name, alt.score)

