from modules.game_functions import welcome, start_game, play_game, finish_game


def main():
    welcome()
    scorecard = start_game()
    play_game(scorecard)
    finish_game(scorecard)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        print("Game closed, Thanks for playing")
