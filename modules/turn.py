import random

class Turn():
  def __init__(self):
    self.dice = {
      "d1": 0,
      "d2": 0,
      "d3": 0,
      "d4": 0,
      "d5": 0,
    }
    self.free_dice = ["d1", "d2", "d3", "d4", "d5"]
    self.held_dice = []
    self.rolls = 0

  def roll_dice(self):
    self.rolls += 1
    for die in self.free_dice:
      self.dice[die] = random.randint(1, 6)
    print("----------------------------------------------------------------------------")
    print("\n")
    print(f"You have {3 - self.rolls} roll(s) remaining. Would you like, to hold or release any dice?")
    print("List any dice you would like to hold, using the format 'd#, d#, d#': ")
    return self.dice.items()

  def hold_dice(self, user_input):
    dice_inputs = user_input.split(", ")
    if dice_inputs:
      for die in dice_inputs:
        self.free_dice.remove(die)
        self.held_dice.append(die)

  def print_dice(self):
    print("\n")
    print("Free dice:")
    for die in self.free_dice:
      print(f"{die}: {self.dice[die]}")
    print("\n")
    print("Held dice:")
    for die in self.held_dice:
      print(f"{die}: {self.dice[die]}")
    print("\n")

  def release_dice(self, user_input):
    dice_inputs = user_input.split(", ")
    if dice_inputs:
      for die in dice_inputs:
        self.free_dice.append(die)
        self.held_dice.remove(die)
