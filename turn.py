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
    for dye in self.free_dice:
      self.dice[dye] = random.randint(1, 6)
    print(f"You have {3 - self.rolls} rolls remaining. Would you like, to hold any dice?")
    print("List any dice you would like to hold, using the format 'd#, d#, d#': ")
    return self.dice.items()

  def hold_dice(self, user_input):
    dice_inputs = user_input.split(", ")
    for dice in dice_inputs:
      self.free_dice.remove(dice)
      self.held_dice.append(dice)

  def print_dice(self):
    print("Free dice:")
    for dye in self.free_dice:
      print(f"{dye}: {self.dice[dye]}")
    print("Held dice:")
    for dye in self.held_dice:
      print(f"{dye}: {self.dice[dye]}")
