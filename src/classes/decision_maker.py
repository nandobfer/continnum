import math

from .criterion_judgment import CriterionJudgment

class DecisionMaker:
  """Representation of a Decision Maker (DM) person who apply judgements into the Model"""
  criterion_judgments = list[CriterionJudgment]  # list of criterion judgements made by this DM

  positive_ideal_solution = list[int]  # the two values of the positive ideal solution
  negative_ideal_solution = list[int]  # the two values of the negative ideal solution

  def __init__(self, id: int, name: str, weight: float) -> None:
    self.criterion_judgments = []
    self.positive_ideal_solution = []
    self.negative_ideal_solution = []

    self.id = id
    self.name = name
    self.weight = weight

  def calculate_ideal_solutions(self):
    """ Loops trough the criterion judgments of this DM to find the maximum and minimum values
    given to the Criteria """

    if not bool(self.criterion_judgments):
      pass

    max_sq = 0
    min_sp = 999999

    # buscando as soluções ideais positiva e negativa
    for judgment in self.criterion_judgments:
      # se o julgamento tiver o melhor valor...
      if judgment.sq > max_sq:
        # salva como melhor solução
        max_sq = judgment.sq

      # se tiver o pior valor...
      if judgment.sp < min_sp:
        # salva como pior solução
        min_sp = judgment.sp

    max_sp_ideal_positive = 0
    min_sq_ideal_negative = 99999

    # buscando os pares de cada solução ideal (+ e -)
    for judgment in self.criterion_judgments:
      # se o julgamento tiver um dos melhores valores...
      if (judgment.sq == max_sq):
        # e tiver o melhor par negativo...
        if (judgment.sp > max_sp_ideal_positive):
          # salva o par como solução ideal positiva
          max_sp_ideal_positive = judgment.sp

      # se o julgamento tiver um dos piores valores...
      if (judgment.sp == min_sp):
        # e tiver o pior par positivo...
        if (judgment.sq < min_sq_ideal_negative):
          # salva o par como solução ideal negativa
          min_sq_ideal_negative = judgment.sq

    # salva os valores no próprio objeto
    self.positive_ideal_solution = [max_sp_ideal_positive, max_sq]
    self.negative_ideal_solution = [min_sp, min_sq_ideal_negative]

  def calculate_judgments_positive_distances(self):
    """ Calculates the positive distance for each of the criterion judgments made by this DM """
    for judgment in self.criterion_judgments:
      positive_dist = self.weight * \
        math.sqrt( \
          abs(self.positive_ideal_solution[0] - judgment.sp) + \
          abs(self.positive_ideal_solution[1] - judgment.sq) \
        )

      judgment.positive_distance = positive_dist

  def calculate_judgments_negative_distances(self):
    """ Calculates the negative distance for each of the criterion judgments made by this DM """
    for judgment in self.criterion_judgments:
      negative_dist = self.weight * \
        math.sqrt( \
          abs(self.negative_ideal_solution[0] - judgment.sp) + \
          abs(self.negative_ideal_solution[1] - judgment.sq) \
        )

      judgment.negative_distance = negative_dist

  def add_new_criterion_judgment(self, criterion_judgment: CriterionJudgment):
    """ Add a new criterion judgment to the list of judgments of the DM  """
    self.criterion_judgments.append(criterion_judgment)

  def find_criterion_judgment_by_criterion(self, criterion_id: int):
    for judgment in self.criterion_judgments:
      if judgment.criterion_id == criterion_id:
        return judgment
    return None