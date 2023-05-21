class AlternativeJudgment:

  def __init__(self, alternative_id: int, decision_maker_id: int, min_value: int, max_value: int):
    self.alternative_id = alternative_id
    self.decision_maker_id = decision_maker_id
    self.max_value = max_value
    self.min_value = min_value
