class Alternative:
  """ Representation of a alternative being judged by the DMs """

  total_distance_positive = float
  total_distance_negative = float
  score = float
  ranking_position = int

  def __init__(self, id: int, name: str):
    self.id = id
    self.name = name

  def calculate_score(self):
    self.score = self.total_distance_negative / (self.total_distance_negative + self.total_distance_positive)
    return self.score
