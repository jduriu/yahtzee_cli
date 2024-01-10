from collections import Counter


class Scorecard:
    def __init__(self):
        self.categories = {
            "ones": {"value": 0, "name": "Ones", "function": self.score_upper},
            "twos": {"value": 0, "name": "Twos", "function": self.score_upper },
            "threes": {"value": 0, "name": "Threes", "function": self.score_upper},
            "fours": {"value": 0, "name": "Fours", "function": self.score_upper},
            "fives": {"value": 0, "name": "Fives", "function": self.score_upper},
            "sixes": {"value": 0, "name": "Sixes", "function": self.score_upper},
            "chance": {"value": 0, "name": "Chance"},
            "three_of_kind": {"value": 0, "name": "Three of a kind"},
            "four_of_kind": {"value": 0, "name": "Four of a kind"},
            "full_house": {"value": 0, "name": "Full house"},
            "sm_straight": {"value": 0, "name": "Small straight"},
            "lg_straight": {"value": 0, "name": "Large straight"},
            "yahtzee": {"value": 0, "name": "Yahtzee"},
        }
        self.bonus = 0
        self.yahtzee_bonus = 0
        self.upper_section = ["ones", "twos", "threes", "fours", "fives", "sixes"]
        self.lower_section = [
            "chance",
            "three_of_kind",
            "four_of_kind",
            "full_house",
            "sm_straight",
            "lg_straight",
            "yahtzee",
        ]
        self.not_scored = [
            "ones",
            "twos",
            "threes",
            "fours",
            "fives",
            "sixes",
            "chance",
            "three_of_kind",
            "four_of_kind",
            "full_house",
            "sm_straight",
            "lg_straight",
            "yahtzee",
        ]
        self.category_commands = {
            "1": "ones",
            "2": "twos",
            "3": "threes",
            "4": "fours",
            "5": "fives",
            "6": "sixes",
            "ch": "chance",
            "3k": "three_of_kind",
            "4k": "four_ok_kind",
            "fh": "full_house",
            "sm": "sm_straight",
            "lg": "lg_straight",
            "yz": "yahtzee",
        }

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

    def remove_score(self, category):
        self.not_scored.remove(category)

    def score_upper(self, category, dice, num):
        counts = Counter(dice)
        total = counts[num] * num
        print(f"{total} will be applied to category: {category}")
        confirm = input("Do you want to confirm? yes(y)/no(n): ")
        if confirm == "y" or confirm == "yes":
            category_attributes = self.score_categories.get(category)
            category_attributes["value"] = total
            self.not_scored.remove(category)

    # def score_chance(self, dice):
    #     if self.chance in self.not_scored:
    #         self.chance = sum(dice.values())
    #         self.not_scored.remove(self.chance)

    # def score_three_of_kind(self, dice):
    #     if self.three_of_kind in self.not_scored:
    #         counts = Counter(dice.values())

    def print_scorecard(self):
        print("Current Scorecard:")
        for category, attributes in self.categories.items():
            name = attributes.get("name")
            value = attributes.get("value")
            print(f"{name}: {value}")
        print("\n")
        print(f"Total Score: {self.get_total_score()}")

    def print_score_commands(self):
        print("Category commands:")
        for command, category in self.category_commands.items():
            print(f"{category} --> {command}")

    def enter_score(self, category, dice, num=None):
        if category in self.not_scored:
            if num:
                self.score_upper(dice, num)
                self.remove_score(category)
            else:
                pass
                # category_attributes = self.categories.get(category)
                # category_attributes.function()
        else:
            return
