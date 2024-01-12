from collections import Counter


class Scorecard:
    def __init__(self):
        self.categories = {
            "ones": {"value": 0, "name": "Ones", "function": self.score_upper},
            "twos": {"value": 0, "name": "Twos", "function": self.score_upper},
            "threes": {"value": 0, "name": "Threes", "function": self.score_upper},
            "fours": {"value": 0, "name": "Fours", "function": self.score_upper},
            "fives": {"value": 0, "name": "Fives", "function": self.score_upper},
            "sixes": {"value": 0, "name": "Sixes", "function": self.score_upper},
            "chance": {"value": 0, "name": "Chance", "function": self.score_chance},
            "three_of_kind": {"value": 0, "name": "Three of a kind", "function": self.score_three_of_kind},
            "four_of_kind": {"value": 0, "name": "Four of a kind", "function": self.score_four_of_kind},
            "full_house": {"value": 0, "name": "Full house", "function": self.score_full_house},
            "sm_straight": {"value": 0, "name": "Small straight", "function": self.score_straight},
            "lg_straight": {"value": 0, "name": "Large straight", "function": self.score_straight},
            "yahtzee": {"value": 0, "name": "Yahtzee", "function": self.score_yahtzee},
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
            "4k": "four_of_kind",
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

    def confirm_and_score(self, category, score):
        name = self.categories.get(category)["name"]
        print(f"{score} will be applied to category: {name}")
        confirm = input("Do you want to confirm? yes(y)/no(n): ").lower()
        if confirm == "y" or confirm == "yes":
            self.categories[category]["value"] = score
            self.not_scored.remove(category)

    def score_upper(self, category, dice, num):
        counts = Counter(dice.values())
        score = counts[num] * num
        self.confirm_and_score(category, score)

    def score_chance(self, category, dice):
        score = 0
        score = sum(dice.values())
        self.confirm_and_score(category, score)

    def score_three_of_kind(self, category, dice):
        nums = set(dice.values())
        counts = Counter(dice.values())
        for num in nums:
            if counts[num] >= 3:
                score = sum(dice.values())
                self.confirm_and_score(category, score)

    def score_four_of_kind(self, category, dice):
        nums = set(dice.values())
        counts = Counter(dice.values())
        for num in nums:
            if counts[num] >= 4:
                score = sum(dice.values())
                self.confirm_and_score(category, score)

    def score_full_house(self, category, dice):
        nums = set(dice.values())
        counts = Counter(dice.values())
        three = False
        two = False
        for num in nums:
            if counts[num] == 3:
                three = True
            if counts[num] == 2:
                two = True
        if three and two:
            self.confirm_and_score(category, 25)

    def score_straight(self, category, dice):
        nums = sorted(dice.values())
        l, r = 0, 1
        count = 1
        straight_length = 1
        while r < len(nums):
            if nums[r] == nums[l] + count:
                r += 1
                count += 1
            else:
                if count > straight_length:
                    straight_length = count
                l = r
                r += 1
                count = 1
        if count > straight_length:
            straight_length = count
        if straight_length == 5 and category == "lg_straight":
            self.confirm_and_score(category, 40)
        elif straight_length >= 4 and category == "sm_straight":
            self.confirm_and_score(category, 30)

    def score_yahtzee(self, category, dice):
        nums = list(dice.values())
        num = nums[0]
        counts = Counter(dice.values())
        if counts[num] == 5:
            self.confirm_and_score(category, 50)

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
                self.score_upper(category, dice, num)
            else:
                category_attributes = self.categories.get(category)
                category_attributes["function"](category, dice)
        elif category == "yahtzee":
            print("You got a yahtzee bonus!")
            self.yahtzee_bonus += 1
