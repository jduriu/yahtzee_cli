from scorecard import Scorecard
from turn import Turn

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

def check_dice_format(user_input):
  if user_input:
    dice = user_input.split(", ")
    for dye in dice:
      if len(dye) == 2:
        if dye[0] == "d" and dye[1].isdigit():
          return dye[1] > 0 and dye[1] < 6
      return False
  return True


def start_game():
  scorecard = Scorecard()
  # while scorecard.scored:
  turn = Turn()
  while turn.rolls < 3:
    rolled_dice = turn.roll_dice()
    turn.print_dice()
    user_input = input("write dice names and press enter: ")
    formatted = check_dice_format(user_input)
    while not formatted:
      print("Whoops, it looks like you typed your answer in the wrong format, please make sure you separate each dice name with a comma and a space")
      user_input = input("please try again: ")
      formatted = check_dice_format(user_input)
    else:
      turn.hold_dice(user_input)
