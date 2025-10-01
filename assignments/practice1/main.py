import time
from tqdm import tqdm

class Country:
    def __init__(self, name, gold=0, silver=0, bronze=0):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def __repr__(self):
        return f"{self.name}: G{self.gold} S{self.silver} B{self.bronze}"

    def __add__(self, other):
        if self.name == other.name:
            return Country(
                self.name,
                self.gold + other.gold,
                self.silver + other.silver,
                self.bronze + other.bronze
            )

    def __lt__(self, other):
        if self.gold != other.gold:
            return self.gold < other.gold
        elif self.silver != other.silver:
            return self.silver < other.silver
        else:
            return self.bronze < other.bronze

    def __eq__(self, other):
        return self.gold == other.gold and self.silver == other.silver and self.bronze == other.bronze


if __name__ == "__main__":
    events = [
        ("KOR", "gold"),
        ("KOR", "silver"),
        ("USA", "gold"),
        ("USA", "gold"),
        ("USA", "bronze"),
        ("JPN", "gold"),
        ("JPN", "silver"),
        ("CHN", "bronze"),
        ("CHN", "bronze")
    ]

    countries = {}

    for country, medal in tqdm(events, desc="Processing events"):
        time.sleep(0.1)
        if country not in countries:
            countries[country] = Country(country)
        if medal == "gold":
            countries[country].gold += 1
        elif medal == "silver":
            countries[country].silver += 1
        elif medal == "bronze":
            countries[country].bronze += 1

    leaderboard = sorted(countries.values(), reverse=True)

    print("\n=== Medal Leaderboard ===")
    rank = 1
    for c in leaderboard:
        print(f"{rank}. {c}")
        rank += 1
