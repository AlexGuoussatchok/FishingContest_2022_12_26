from typing import List

from prod.model.entity.fisherman import Fisherman
from prod.model.logic.generate_catch import CatchGenerator
from prod.model.logic.judge import Judge
from prod.util.generate_teams import TeamsCreator


def main():
    num_teams = int(input("Please enter number of teams: "))
    num_people_in_team = int(input("Please enter number of people in the team: "))

    teams: dict[str, List[Fisherman]] = TeamsCreator.create_teams(num_teams, num_people_in_team)
    print("We have the following teams and participants:")
    for team, fishermen in teams.items():
        print(f"Team: {team}")
        print("    ", fishermen)

    max_num_of_fishes_in_catch = 20
    team_to_catch_dict = CatchGenerator(max_num_of_fishes_in_catch).gen_catch(teams)
    for team, fishermen_list in team_to_catch_dict.items():
        print(f"Team {team} got the following catch")
        for fisherman_catch in fishermen_list:
            for fisherman, fishes in fisherman_catch.items():
                print(f"    Fisherman {fisherman.first_name} {fisherman.last_name} got {fishes}")

    teams_to_total_catch = Judge.calculate_team_catches_dict(team_to_catch_dict)

    print()

    winner_team, winners_catch = Judge.calculate_max_catch(teams_to_total_catch)
    losers_team, losers_catch = Judge.calculate_min_catch(teams_to_total_catch)
    print(f"The winner team is: {winner_team} with the catch: {winners_catch / 1_000} kg.")
    print(f"The losers team is: {losers_team} with the catch: {losers_catch / 1_000} kg.")


if __name__ == '__main__':
    main()
