from typing import List

from prod.model.entity.fisherman import Fisherman
from prod.util.fisherman_creator import FishermenCreator


class TeamsCreator:

    @classmethod
    def _gen_team_name(cls, i):
        return f"team {i + 1}"

    @classmethod
    def create_teams(cls, num_teams, num_people_in_team) -> dict[str, List[Fisherman]]:
        teams = {}
        for i in range(num_teams):
            teams[cls._gen_team_name(i)] = FishermenCreator.create_participants(num_people_in_team)
        return teams
