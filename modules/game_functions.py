from modules.scorecard import Scorecard
from modules.turn import Turn


def explain_game():
    explained = False
    steps = [
        [
            "Yahtzee is a dice game consisting of 5 dice.",
            "The user is able to hold and re-roll dice similar to poker.",
        ],
        ["There are various ways to score!"],
        [
            "For basic scores ones -> sixes, the sum of the matching dice after all rolls have been taken for that turn are counted.",  # noqa
            "Only single score categories can be summed each turn.",
        ],
        [
            "There are also poker style combinations you can score,",
            "3 of a Kind, 4 of a Kind, Small Straight, Large Straight, and Full House",  # noqa
        ],
        ["There are also some special combinations,", "Chance and Yahtzee"],
        [
            "Chance is the sum of any combination of dice.",
            "Yahtzee is when all dice are matching.",
        ],
        [
            "Every turn, each player gets 3 rolls.",
            "At any time, a dice value can be 'held' and will not be re-rolled.",  # noqa
            "At any time, a held dice can be 'released' and will be re-rolled.",  # noqa
        ],
        [
            "A player does not need to take all 3 rolls before recording a score, however, if a score is recorded, that turn ends."  # noqa
        ],
    ]
    while not explained:
        for step in steps:
            print("\n")
            for line in step:
                print("// " + line)
            print("\n")
            input("press any key to continue ")

        repeat = input(
            "Would you like have these instructions repeated? yes(y) / no(n): "
        )
        if repeat == "n" or repeat == "no":
            explained = True
    print("\n")
    print("Good luck!!")


def welcome():
    print("\n")
    print("/////////////////// Welcome to Yahtzee! /////////////////////")
    print("\n")
    ready_commands = ["yes", "y"]
    ready = False

    knows_rules = input("Do you know the rules yes(y) / no(n): ").lower()
    if knows_rules in ready_commands:
        user_input = input("Start Game? yes(y) / no(n): ").lower()
        if user_input in ready_commands:
            ready = True
        if not ready:
            not_ready = input(
                "Not ready? Would you like to see the instructions? yes(y) / no(n): "  # noqa
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
        print("\n")
        print(
            f"-------------------- You are on turn #{scorecard.turn_number} ---------------------"  # noqa
        )
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
            print(
                """
            Roll Commands:
                'hold' --> hold dice values
                'release' --> release dice values
                'roll' --> re-roll non-held dice
                'score' --> score with current dice
                'scorecard' --> see current scorecard
            """
            )
            roll_operations = {
                "hold": turn.hold_dice,
                "release": turn.release_dice,
            }
            operation = input("Enter a command: ")
            if operation in roll_operations:
                user_input = input(f"write dice names to {operation} and press enter: ")  # noqa
                formatted = check_dice_format(user_input)
                while not formatted:
                    print(
                        "Whoops, it looks like you typed your answer in the wrong format, please make sure you separate each dice name with a comma and a space"  # noqa
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
                    "Whoops, it looks like you entered an incorrect operation try again"  # noqa
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

    print("\n")
    print("Ready to score!")
    print("\n")

    while not scored:
        print(
            """
            Commands:
                'scorecard' --> view scorecard
                'dice' --> view current turn dice
                'categories' --> view a list of score category commands
            or:
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
            if (
                len(scorecard.not_scored) != score_length
                or scorecard.yahtzee_bonus > yahtzee_bonus
            ):
                print(f"{category} scored!")
                scored = True
        else:
            print(
                "That command isn't available or the category was already scored, please try again"  # noqa
            )


def finish_game(scorecard):
    print("\n")
    print("-------------------- Game completed! ---------------------")
    print("\n")
    print("Your final scorecard is: ")
    scorecard.print_scorecard()
    print("\n")
    print("///////////////////// THANKS FOR PLAYING! ////////////////////")
