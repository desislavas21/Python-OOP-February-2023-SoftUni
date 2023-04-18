from Exercise.ex_6_Formula_1_Manager.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @property
    def sponsors(self):
        return {"Petronas": {
            1: 1000000,
            3: 500000
        },
        "TeamViewer": {
            5: 100000,
            7: 50000
        }}

    @property
    def expenses_for_one_race(self):
        return 200000