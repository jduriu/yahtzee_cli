from collections import Counter

class Scorecard():
  def __init__(self):
    self.categories = {
      "ones": {"command": "1", "value": 0, "name": "Ones"},
      "twos": {"command": "2", "value": 0, "name": "Twos"},
      "threes": {"command": "2", "value": 0, "name": "Threes"},
      "fours": {"command": "4", "value": 0, "name": "Fours"},
      "fives": {"command": "5", "value": 0, "name": "Fives"},
      "sixes": {"command": "6", "value": 0, "name": "Sixes"},
      "chance": {"command": "ch", "value": 0, "name": "Chance"},
      "three_of_kind": {"command": "3k", "value": 0, "name": "Three of a kind"},
      "four_of_kind": {"command": "4k", "value": 0, "name": "Four of a kind"},
      "full_house": {"command": "fh", "value": 0, "name": "Full house"},
      "sm_straight": {"command": "sm", "value": 0, "name": "Small straight"},
      "lg_straight": {"command": "lg", "value": 0, "name": "Large straight"},
      "yahtzee": {"command": "yz", "value": 0, "name": "Yahtzee"},
    }
    self.bonus = 0
    self.yahtzee_bonus = 0
    self.upper_section = ["ones", "twos", "threes", "fours", "fives", "sixes"]
    self.lower_section = ["chance", "three_of_kind", "four_of_kind", "full_house", "sm_straight", "lg_straight", "yahtzee"]
    self.scored = ["ones", "twos", "threes", "fours", "fives", "sixes", "chance", "three_of_kind", "four_of_kind", "full_house", "sm_straight", "lg_straight", "yahtzee"]

  def get_upper_section_total(self):
    subtotal = 0
    for score in self.upper_section:
      category = self.categories.get(score)
      subtotal += category.get("value")
    if subtotal >= 63 and self.bonus == 0:
      self.bonus = 35
    return subtotal + self.bonus

  def get_lower_section_total(self):
    subtotal = 0
    for score in self.lower_section:
      category = self.categories.get(score)
      subtotal += category.get("value")
    if self.yahtzee_bonus:
      return subtotal + (50 * self.yahtzee_bonus)
    return subtotal

  def get_total_score(self):
    return self.get_lower_section_total() + self.get_upper_section_total()

  def score_num(self, dice, num):
    scored = False
    # scores = {
    #   1: self.ones,
    #   2: self.twos,
    #   3: self.threes,
    #   4: self.fours,
    #   5: self.fives,
    #   6: self.sixes,
    # }
    while not scored:
      if scores.num in self.scored:
        total = 0
        [total + num for die in dice.values() if die == num]
        scores.num = total
        self.scored.remove(scores.num)
        scored = True
      else:
        return

  def score_chance(self, dice):
    if self.chance in self.scored:
      self.chance = sum(dice.values())
      self.scored.remove(self.chance)


  def score_three_of_kind(self, dice):
    if self.three_of_kind in self.scored:
      counts = Counter(dice.values())


  def print_scorecard(self):
    print("Current Scorecard:")
    for category, attributes in self.categories.items():
      name = attributes.get("name")
      value = attributes.get("value")
      print(f"{name}: {value}")
    print("\n")
    print(f"Total Score: {self.get_total_score()}")
