import sys
from typing import List

from prod.model.entity.fish import Fish
from prod.model.entity.fisherman import Fisherman


class Judge:

    @classmethod
    def _calculate_catch_per_team(cls, team_catch: List[dict[Fisherman, List[Fish]]]):
        total_g_per_team = 0
        for fisherman_dict in team_catch:
            for list_fishes in fisherman_dict.values():
                total_g_per_fisherman = 0
                for fish in list_fishes:
                    total_g_per_fisherman += fish.weight
                total_g_per_team += total_g_per_fisherman
        return total_g_per_team

    @classmethod
    def calculate_team_catches_dict(cls, teams: dict[str, List[dict[Fisherman, List[Fish]]]]) -> dict[str, int]:
        catch_per_team = {}
        for team_name, team_catch in teams.items():
            catch_per_team[team_name] = cls._calculate_catch_per_team(team_catch)
        return catch_per_team

    @classmethod
    def calculate_max_catch(cls, teams: dict[str, int]):
        max = 0
        team = ""
        for t, catch in teams.items():
            if catch >= max:
                team = t
                max = catch
        return team, max

    @classmethod
    def calculate_min_catch(cls, teams: dict[str, int]):
        min = sys.maxsize
        team = ""
        for t, catch in teams.items():
            if catch <= min:
                team = t
                min = catch
        return team, min

