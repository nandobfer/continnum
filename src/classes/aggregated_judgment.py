class AggregatedJudgment:

  sp = int
  sq = int
  positive_distance = float
  negative_distance = float

  def __init__(self, alternative_id: int, sp: int, sq: int):
    self.alternative_id = alternative_id
    self.sp = sp
    self.sq = sq
