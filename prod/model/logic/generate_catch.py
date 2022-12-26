import random
from typing import List

from prod.model.entity.fish import Fish
from prod.model.entity.fish_types import fish_types
from prod.model.entity.fisherman import Fisherman
from prod.util.fisherman_creator import FishermenCreator


class CatchGenerator:

    def __init__(self, max_num_fishes):
        self.max_num_fishes = max_num_fishes

    @classmethod
    def _gen_fish(cls, number) -> Fish:
        return fish_types[number % len(fish_types)]()

    def _num_of_fishes_for_fisherman(self, fisherman: Fisherman) -> int:
        return FishermenCreator(self.max_num_fishes).num_of_fishes_for_fisherman(fisherman)

    def _catch_from_fisherman(self, fisherman: Fisherman) -> dict[Fisherman, List[Fish]]:
        num_fishes = self._num_of_fishes_for_fisherman(fisherman)
        catch = {fisherman: []}
        for i in range(num_fishes):
            fish = self._gen_fish(random.randint(0, 100))
            catch[fisherman].append(fish)
        return catch

    def gen_catch(self, teams: dict[str, List[Fisherman]]) -> dict[str, List[dict[Fisherman, List[Fish]]]]:
        catch = {}
        for team_name, team in teams.items():
            catch_per_team = []
            for fisherman in team:
                catch_per_team.append(self._catch_from_fisherman(fisherman))
            catch[team_name] = catch_per_team
        return catch
