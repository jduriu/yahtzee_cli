class Scorecard():
  def __init__(self):
    self.ones = 0
    self.twos = 0
    self.threes = 0
    self.fours = 0
    self.fives = 0
    self.sixes = 0
    self.bonus = 0
    self.chance = 0
    self.three_of_kind = 0
    self.four_of_kind = 0
    self.full_house = 0
    self.sm_straight = 0
    self.lg_straight = 0
    self.yahtzee = 0
    self.yahtzee_bonus = 0
    self.upper_section = [self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes]
    self.lower_section = [self.chance, self.three_of_kind, self.four_of_kind, self.full_house, self.sm_straight, self.lg_straight, self.yahtzee]
    self.scored = [self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes, self.chance, self.three_of_kind, self.four_of_kind, self.full_house, self.sm_straight, self.lg_straight, self.yahtzee]

  def get_upper_section_total(self):
    subtotal = sum(self.upper_section)
    if subtotal >= 63 and self.bonus == 0:
      self.bonus = 35
    return subtotal + self.bonus

  def get_lower_section_total(self):
    subtotal = sum(self.lower_section)
    if self.yahtzee_bonus:
      return subtotal + (50 * self.yahtzee_bonus)
    return subtotal

  def record_ones(self, dice):
    total = 0
    [total + 1 for die in dice.values() if die == 1]
    self.ones = total
    self.scored.remove(self.ones)


  def print_scorecard(self):
    print("Current Scorecard:")
    print(f"Ones: f{self.ones}")
