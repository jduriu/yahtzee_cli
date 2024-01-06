class Turn():
  def __init__(self):
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    open_dice = [d1, d2, d3, d4, d5]
    held_dice = []
    rolls = 0

class Scorecard():
  def __init__(self):
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    bonus = 0
    chance = 0
    three_of_kind = 0
    four_of_kind = 0
    full_house = 0
    sm_straight = 0
    lg_straight = 0
    yahtzee = 0
    yahtzee_bonus = 0
    upper_section = [ones, twos, threes, fours, fives, sixes]
    lower_section = [chance, three_of_kind, four_of_kind, full_house, sm_straight, lg_straight, yahtzee]
    scored = [ones, twos, threes, fours, fives, sixes, chance, three_of_kind, four_of_kind, full_house, sm_straight, lg_straight, yahtzee]

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


def explain_game():
  explained = False
  while not explained:
    print("\n")
    print("Yahtzee is a dice game consisting of 5 dice")
    print("The user is able to hold and re-roll dice similar to poker")
    print("\n")
    input("press any key to continue")
    print("\n")
    print("There are various ways to score")
    print("\n")
    input("press any key to continue")
    print("\n")
    print("For basic scores ones -> sixes, the sum of the matching dice after all rolls have been taken for that turn are counted")
    print("Only single score categories can be summed each turn")
    print("\n")
    input("press any key to continue")
    print("\n")
    print("There are also poker style combinations you can score,")
    print("3 of a kind, 4 of a kind, small straight, large straight, and full house")
    print("\n")
    input("press any key to continue")
    print("\n")
    print("There are also some special combinations")
    print("chance and yahtzee")
    print("\n")
    input("press any key to continue")
    print("\n")
    print("Chance is the sum of any combination of dice")
    print("Yahtzee is when all dice are matching")
    print("\n")
    input("press any key to continue")
    print("\n")
    print("Every turn, each player gets 3 rolls")
    print("At any time, a dice value can be 'held' and will not be re-rolled")
    print("At any time, a held dice can be 'released' and will be re-rolled")
    print("\n")
    input("press any key to continue")
    print("\n")
    print("A player does not need to take all 3 rolls before recording a score, however, if a score is recorded, that turn ends")
    print("\n")
    repeat = input("Would you like have these instructions repeated? yes(y) / no(n): ")
    if repeat == "n" or repeat == "no":
      explained = True



def welcome():
  print("Welcome to Yahtzee!")
  knows_rules = input("Do you know the rules yes(y) / no(n): ")

  if knows_rules == "y" or knows_rules == "yes":
    ready = input("Start Game? yes(y) / no(n): ")
    if not ready:
      not_ready = input("Not ready? Would you like to see the instructions? yes(y) / no(n): ")
      if not_ready:
        explain_game()
  else:
    explain_game()

def start_game():
  scorecard = Scorecard()
  while scorecard.scored:
