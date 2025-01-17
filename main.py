from src.classes.decision_maker import DecisionMaker
from src.classes.model import Model
from src.boardgames import getBoardgames, getCriteria, setCriteria, judge
import sys, logging

logging.basicConfig(level=logging.DEBUG if '-v' in sys.argv else logging.INFO)

verbose = True 

##################################
# Criação dos objetos no cliente #
##################################

# julgadores
dm1 = DecisionMaker(1, "Dm_1", 0.5)
dm2 = DecisionMaker(2, "Dm_2", 0.5)

# Critérios a serem julgados
## boardgames.py > getCriteria()

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

print('')
print("D+")
model.sum_positive_alternative_distance()
print('')
print("D-")
model.sum_negative_alternative_distance()

model.calculate_alternatives_score()

print('')
print("Score")
ranking = model.get_alternative_ranking()
for alt in ranking:
  print(alt.name, alt.score)

