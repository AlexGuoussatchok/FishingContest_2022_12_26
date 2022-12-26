import random
import unittest

from prod.model.entity.Cancian_carp import CancianCarp
from prod.model.entity.fish import Fish
from prod.model.entity.fisherman import Fisherman
from prod.model.entity.perch import Perch
from prod.model.entity.roach import Roach
from prod.model.entity.ruff import Ruff
from prod.model.logic.generate_catch import CatchGenerator
from prod.model.logic.judge import Judge
from prod.util.fisherman_creator import FishermenCreator
from prod.util.generate_teams import TeamsCreator


class MyTestCase(unittest.TestCase):
    RANDOM_SEED = 5

    def setUp(self) -> None:
        random.seed(self.RANDOM_SEED)

    def test_perch(self):
        perch = Perch()
        print(perch)
        self.assertEqual(perch.length, 215)
        self.assertEqual(perch.weight, 294)
        self.assertEqual(perch.fish_name, 'Perch')

    def test_carp(self):
        carp = CancianCarp()
        print(carp)
        self.assertEqual(carp.length, 179)
        self.assertEqual(carp.weight, 132)
        self.assertEqual(carp.fish_name, 'Cancian Carp')

    def test_roach(self):
        roach = Roach()
        self.assertEqual(roach.length, 309)
        self.assertEqual(roach.weight, 280)
        self.assertEqual(roach.fish_name, 'Roach')

    def test_ruff(self):
        perch = Ruff()
        self.assertEqual(perch.length, 159)
        self.assertEqual(perch.weight, 19)
        self.assertEqual(perch.fish_name, 'Ruff')

    def test_generate(self):
        teams = TeamsCreator.create_teams(2, 3)
        print(teams)
        team_to_catch_dict = CatchGenerator(5).gen_catch(teams)
        print(team_to_catch_dict)
        catches = Judge.calculate_team_catches_dict(team_to_catch_dict)
        print(catches)

    def test__num_of_fishes_for_fisherman(self):
        f = Fisherman("a", "b", 5, 2, 3)
        print(FishermenCreator(20).num_of_fishes_for_fisherman(f))

    def _generate_teams(self):
        list_fishes1 = [Fish(Perch.NAME, 10, 500),
                        Fish(Roach.NAME, 20, 300),
                        Fish(Perch.NAME, 25, 250)]
        list_fishes2 = [Fish(Perch.NAME, 10, 500),
                        Fish(CancianCarp.NAME, 25, 450)]
        list_fishes3 = [Fish(Ruff.NAME, 10, 700),
                        Fish(Perch.NAME, 25, 350)]
        list_fishes4 = [Fish(Ruff.NAME, 10, 100),
                        Fish(Ruff.NAME, 20, 100),
                        Fish(Ruff.NAME, 25, 350)]
        f1 = Fisherman("f1", "f1", 30, 20, 100)
        f2 = Fisherman("f2", "f2", 30, 20, 100)
        f3 = Fisherman("f3", "f3", 30, 20, 100)
        f4 = Fisherman("f4", "f4", 30, 20, 100)

        teams = {"t1": [{f1: list_fishes1, f2: list_fishes2}],
                 "t2": [{f3: list_fishes3, f4: list_fishes4}]}
        return teams

    def test_create_team(self):
        teams = self._generate_teams()
        expected = {"t1": 1050 + 950, "t2": 1050 + 550}
        catches = Judge.calculate_team_catches_dict(teams)
        print(catches)
        self.assertEqual(catches, expected)

    def test_max_team(self):
        teams = self._generate_teams()
        catches = Judge.calculate_team_catches_dict(teams)
        team_name, catch = Judge.calculate_max_catch(catches)
        print(f"The winner is {team_name} with the catch {catch}")
        self.assertEqual("t1", team_name)
        self.assertEqual(2000, catch)

    def test_min_team(self):
        teams = self._generate_teams()
        catches = Judge.calculate_team_catches_dict(teams)
        team_name, catch = Judge.calculate_min_catch(catches)
        print(f"The winner is {team_name} with the catch {catch}")
        self.assertEqual("t2", team_name)
        self.assertEqual(1600, catch)


if __name__ == '__main__':
    unittest.main()
