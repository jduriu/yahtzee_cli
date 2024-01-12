from modules.scorecard import Scorecard
from modules.turn import Turn


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
        print(
            "For basic scores ones -> sixes, the sum of the matching dice after all rolls have been taken for that turn are counted"
        )
        print("Only single score categories can be summed each turn")
        print("\n")
        input("press any key to continue")
        print("\n")
        print("There are also poker style combinations you can score,")
        print(
            "3 of a kind, 4 of a kind, small straight, large straight, and full house"
        )
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
        print(
            "A player does not need to take all 3 rolls before recording a score, however, if a score is recorded, that turn ends"
        )
        print("\n")
        repeat = input(
            "Would you like have these instructions repeated? yes(y) / no(n): "
        )
        if repeat == "n" or repeat == "no":
            explained = True


def welcome():
    print("Welcome to Yahtzee!")
    knows_rules = input("Do you know the rules yes(y) / no(n): ")

    if knows_rules == "y" or knows_rules == "yes":
        ready = input("Start Game? yes(y) / no(n): ")
        if not ready:
            not_ready = input(
                "Not ready? Would you like to see the instructions? yes(y) / no(n): "
            )
            if not_ready:
                explain_game()
    else:
        explain_game()


def check_dice_format(user_input):
    checked = []
    if user_input:
        dice = user_input.split(", ")
        for die in dice:
            if len(die) == 2 and die not in checked:
                if die[0] == "d" and die[1].isdigit():
                    if int(die[1]) > 0 and int(die[1]) < 6:
                        checked.append(die)
        return len(dice) == len(checked)


def start_game():
    scorecard = Scorecard()
    return scorecard


def play_game(scorecard):
    while scorecard.not_scored:
        turn = take_turn(scorecard)
        record_score(turn, scorecard)


def take_turn(scorecard):
    turn = Turn()
    while True:
        if turn.rolls == 2:
            turn.print_all_dice()
            return turn
        turn.roll_dice()
        re_roll = False
        while not re_roll:
            turn.print_dice()
            print("""
            Roll Commands:
            'hold' --> hold dice values
            'release' --> release dice values
            'roll' --> re-roll non-held dice
            'score' --> score with current dice
            """)
            roll_operations = {
                "hold": turn.hold_dice,
                "release": turn.release_dice,
            }
            operation = input("Enter a command: ")
            if operation in roll_operations:
                user_input = input(f"write dice names to {operation} and press enter: ")
                formatted = check_dice_format(user_input)
                while not formatted:
                    print(
                        "Whoops, it looks like you typed your answer in the wrong format, please make sure you separate each dice name with a comma and a space"
                    )
                    user_input = input("please try again: ")
                    formatted = check_dice_format(user_input)
                roll_operations[operation](user_input)
            elif operation == "roll":
                re_roll = True
            elif operation == "score":
                return turn
            elif operation == "scorecard":
                scorecard.print_scorecard()
            else:
                print(
                    "Whoops, it looks like you entered an incorrect operation try again"
                )


def record_score(turn, scorecard):
    scored = False
    score_length = len(scorecard.not_scored)
    yahtzee_bonus = scorecard.yahtzee_bonus
    commands = {
        "scorecard": scorecard.print_scorecard,
        "dice": turn.print_all_dice,
        "categories": scorecard.print_score_commands,
    }

    while not scored:
        print(
            """
            Commands:
            'scorecard' --> view scorecard
            'dice' --> view current turn dice
            'categories' --> view a list of score category commands
            or
            Enter a category command to record score
            """
        )
        user_input = input("Enter command: ")
        if user_input in commands:
            commands[user_input]()
        elif user_input in scorecard.category_commands:
            category = scorecard.category_commands.get(user_input)
            if user_input.isdigit():
                scorecard.enter_score(category, turn.dice, int(user_input))
            else:
                scorecard.enter_score(category, turn.dice)
            if len(scorecard.not_scored) != score_length or scorecard.yahtzee_bonus > yahtzee_bonus:
                print(f"{category} scored!")
                scored = True
        else:
            print(
                """That command isn't available or the category was
                already scored, please try again"""
            )
