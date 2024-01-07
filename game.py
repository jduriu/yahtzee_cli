from game_functions import welcome, start_game, play_game

def main():
  welcome()
  scorecard = start_game()
  play_game(scorecard)

  # Overall game logic



if __name__ == "__main__":
  main()
