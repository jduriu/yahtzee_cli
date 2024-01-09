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

  def get_total_score(self):
    return self.get_lower_section_total() + self.get_upper_section_total()

  def record_ones(self, dice):
    total = 0
    [total + 1 for die in dice.values() if die == 1]
    self.ones = total
    self.scored.remove(self.ones)

  def print_scorecard(self):
    print("Current Scorecard:")
    print(f"ones: {self.ones}")
    print(f"twos: {self.twos}")
    print(f"threes: {self.threes}")
    print(f"fours: {self.fours}")
    print(f"fives: {self.fives}")
    print(f"sixes: {self.sixes}")
    print(f"chance: {self.chance}")
    print(f"three of a kind: {self.three_of_kind}")
    print(f"four of a kind: {self.four_of_kind}")
    print(f"small straight: {self.sm_straight}")
    print(f"large straight: {self.lg_straight}")
    print(f"full house: {self.full_house}")
    print(f"yahtzee: {self.yahtzee}")
    print(f"yahtzee bonus: {self.yahtzee_bonus}")
    print("\n")
    print(f"Total Score: {self.get_total_score()}")
