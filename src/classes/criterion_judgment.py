class CriterionJudgment:
  """Representation of the DM's judgement about the weight of the Criterion"""

  positive_distance = float
  negative_distance = float

  def __init__(self, criterion_id: int, sp: int, sq: int) -> None:
    self.criterion_id = criterion_id  # criterion being judged by the DecisionMaker
    self.sp = sp  # "lower" value of the fuzzy judgement
    self.sq = sq  # "higher" value of the fuzzy judgement
