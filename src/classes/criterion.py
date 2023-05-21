from .alternative_judgment import AlternativeJudgment
from .aggregated_judgment import AggregatedJudgment
from ..enumerations.criterion_type import CriterionType


class Criterion:
  """Representation of the Criteria used to judge Alternatives in the Model"""
  total_positive_distance = 0  # distance of this criterion to the positive ideal
  total_negative_distance = 0  # distance of this criterion to the negative ideal
  cci = 0  # unnormalized weight
  normalized_cci = 0  # weight (level of importance) of the criterion

  unnormalized_distance = 0
  normalized_distance = 0

  alternative_judgments: list[AlternativeJudgment]
  aggregated_judgments: list[AggregatedJudgment]

  positive_ideal_solution = list[int]  # the two values of the positive ideal solution
  negative_ideal_solution = list[int]  # the two values of the negative ideal solution

  def __init__(self, id: int, description: str, criterion_type: CriterionType) -> None:
    """Initializes a Criterion with it's type and description"""
    self.alternative_judgments = []
    self.aggregated_judgments = []
    self.positive_ideal_solution = []
    self.negative_ideal_solution = []
    self.id = id
    self.description = description
    self.criterion_type = criterion_type

  def calculate_cci(self):
    """Calculates the unnormalized weight by dividing the negative distance by the sum of the distances"""
    self.cci = self.total_negative_distance / (self.total_negative_distance +
                                               self.total_positive_distance)
    return self.cci

  def calculate_normalized_cci(self, total_cci):
    self.normalized_cci = self.cci / total_cci
    return self.normalized_cci

  def generate_aggregated_judgment_table(self, alt):
    min_values = []
    max_values = []
    
    for judgment in self.alternative_judgments:
      if judgment.alternative_id == alt.id:
        min_values.append(judgment.min_value)
        max_values.append(judgment.max_value)

    min_values.sort(reverse=True)
    max_values.sort(reverse=False)

    min = min_values[0]
    max = max_values[0]

    sp = min if min <= max else max
    sq = max if max >= min else min

    print(self.description, alt.name, sp, sq)
    self.add_new_aggregated_judgment(AggregatedJudgment(alt.id, sp, sq))

  def add_new_alternative_judgment(self, alternative_judgment: AlternativeJudgment):
    self.alternative_judgments.append(alternative_judgment)
  
  def add_new_aggregated_judgment(self, aggregated_judgment : AggregatedJudgment):
    self.aggregated_judgments.append(aggregated_judgment)

  def find_positive_solution(self):
    pass

  def find_negative_solution(self):
    pass

  def calculate_ideal_solutions(self):
    """ Loops trough the alternative judgments of this criterion to find the maximum and minimum values
    given to the Alternative """

    if not bool(self.alternative_judgments):
      pass

    max_vq = 0
    min_vp = 999999

    # buscando as soluções ideais positiva e negativa
    for judgment in self.alternative_judgments:
      # se o julgamento tiver o melhor valor...
      if judgment.max_value > max_vq:
        # salva como melhor solução
        max_vq = judgment.max_value

      # se tiver o pior valor...
      elif judgment.min_value < min_vp:
        # salva como pior solução
        min_vp = judgment.min_value

    max_vp_ideal_positive = 0
    min_vq_ideal_negative = 999999

    # buscando os pares de cada solução ideal (+ e -)
    # OBS: estamos considerando todos os critérios como de benefício.
    # Para critérios de custo, a regra para buscar o par é invertida
    for judgment in self.alternative_judgments:
      # se o julgamento tiver um dos melhores valores...
      if (judgment.max_value == max_vq):
        # e tiver o melhor par negativo...
        if (judgment.min_value > max_vp_ideal_positive):
          # salva o par como solução ideal positiva
          max_vp_ideal_positive = judgment.min_value

      # se o julgamento tiver um dos piores valores...
      if (judgment.min_value == min_vp):
        # e tiver o pior par positivo...
        if (judgment.max_value < min_vq_ideal_negative):
          # salva o par como solução ideal negativa
          min_vq_ideal_negative = judgment.max_value

    # salva os valores no próprio objeto
    if (self.criterion_type == CriterionType.BENEFIT):
      self.positive_ideal_solution = [max_vp_ideal_positive, max_vq]
      self.negative_ideal_solution = [min_vp, min_vq_ideal_negative]
    else:
      self.negative_ideal_solution = [max_vp_ideal_positive, max_vq]
      self.positive_ideal_solution = [min_vp, min_vq_ideal_negative]
      
    print(self.description, 'A+', self.positive_ideal_solution, 'A-', self.negative_ideal_solution)