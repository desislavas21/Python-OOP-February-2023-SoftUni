from Exercise.ex_6_Formula_1_Manager.formula_teams.red_bull_team import RedBullTeam
from Exercise.ex_6_Formula_1_Manager.formula_teams.mercedes_team import MercedesTeam
from typing import List


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team: List[RedBullTeam] or None = None
        self.mercedes_team: List[MercedesTeam] or None = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name != "Red Bull" and team_name != "Mercedes":
            raise ValueError("Invalid team name!")
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        self.mercedes_team = MercedesTeam(budget)
        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")
        better_position = ""
        if red_bull_pos < mercedes_pos:
            better_position = "Red Bull"
        else:
            better_position = "Mercedes"
        red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return f"Red Bull: {red_bull_revenue}. " \
               f"Mercedes: {mercedes_revenue}. " \
               f"{better_position} is ahead at the" \
               f" {race_name} race."


# Example
f1_season = F1SeasonApp()

print(f1_season.register_team_for_season("Red Bull", 2000000))
print(f1_season.register_team_for_season("Mercedes", 2500000))
print(f1_season.new_race_results("Nurburgring", 1, 7))
print(f1_season.new_race_results("Silverstone", 10, 1))
