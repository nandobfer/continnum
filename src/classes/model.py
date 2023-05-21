from .criterion import Criterion
from .decision_maker import DecisionMaker
from .alternative import Alternative

# from enumerations.five_linguistic_terms import FiveLinguisticTerms
# from enumerations.seven_linguistic_terms import SevenLinguisticTerms


class Model:
  """ Representation of the entire Model being created, which has access to all
    Decision Makers, Criteria, Alternatives and Judgements and can calculate the
    final alternative ranking by score """

  normalized_cci = float

  def __init__(
    self,
    number_of_terms: int,
    criteria: list[Criterion],
    alternatives: list[Alternative],
    decision_makers: list[DecisionMaker]
  ) -> None:
    self.number_of_terms = number_of_terms
    self.criteria = criteria
    self.alternatives = alternatives
    self.decision_makers = decision_makers

  def calculate_decision_makers_ideal_solution(self):
    for dm in self.decision_makers:
      dm.calculate_ideal_solutions()

  def calculate_criteria_ideal_solution(self):
    for cri in self.criteria:
      cri.calculate_ideal_solutions()

  def sum_positive_criterion_distance(self):
    """ Calculates the positive distance for all criteria """
    for cri in self.criteria:
      total_positive_distance = 0

      for dm in self.decision_makers:
        dm.calculate_judgments_positive_distances()
        criterion_judgment = dm.find_criterion_judgment_by_criterion(cri.id)
        total_positive_distance += criterion_judgment.positive_distance

      cri.total_positive_distance = total_positive_distance

  def sum_negative_criterion_distance(self):
    """ Calculates the negative distance for all criteria """
    for cri in self.criteria:
      total_negative_distance = 0

      for dm in self.decision_makers:
        dm.calculate_judgments_negative_distances()
        criterion_judgment = dm.find_criterion_judgment_by_criterion(cri.id)
        total_negative_distance += criterion_judgment.negative_distance

      cri.total_negative_distance = total_negative_distance

  def calculate_normalized_weight(self):
    total_cci = 0
    total_normalized_cci = 0

    for cri in self.criteria:
      total_cci += cri.calculate_cci()

    for cri in self.criteria:
      total_normalized_cci += cri.calculate_normalized_cci(total_cci)
      print(cri.description, cri.cci, cri.normalized_cci)

    print()
    self.normalized_cci = total_normalized_cci
    return self.normalized_cci

  def generate_all_aggregated_judgments(self):
    for cri in self.criteria:
      for alt in self.alternatives:
        cri.generate_aggregated_judgment_table(alt)
      print()

  def sum_positive_alternative_distance(self):
    for alt in self.alternatives:
      total_distance_positive = 0
    
      for cri in self.criteria:
        for judgment in cri.aggregated_judgments:
          if (judgment.alternative_id != alt.id):
            continue
          
          total_distance_positive += \
            cri.normalized_cci * ( 0.5 * \
              ( abs(cri.positive_ideal_solution[0] - judgment.sp) + \
                abs(cri.positive_ideal_solution[1] - judgment.sq) \
              ) \
            )
          
      alt.total_distance_positive = total_distance_positive
      print(alt.name, alt.total_distance_positive)

  def sum_negative_alternative_distance(self):
    for alt in self.alternatives:
      total_distance_negative = 0
    
      for cri in self.criteria:
        for judgment in cri.aggregated_judgments:
          if (judgment.alternative_id != alt.id):
            continue
          
          total_distance_negative += \
            cri.normalized_cci * ( 0.5 * \
              ( abs(cri.negative_ideal_solution[0] - judgment.sp) + \
                abs(cri.negative_ideal_solution[1] - judgment.sq) \
              ) \
            )
          
      alt.total_distance_negative = total_distance_negative
      print(alt.name, alt.total_distance_negative)

  def calculate_alternatives_score(self):
    for alt in self.alternatives:
      alt.calculate_score()
      
  def get_alternative_ranking(self):
    sorted_list = sorted(self.alternatives, key=lambda alternative: alternative.score, reverse=True)
    return sorted_list