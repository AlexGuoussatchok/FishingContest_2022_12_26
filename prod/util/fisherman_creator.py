import random
from typing import List

from prod.model.entity.fisherman import Fisherman
from prod.model.entity.fisherman import NoviceFisherman
from prod.model.entity.fisherman import AmateurFisherman
from prod.model.entity.fisherman import ProfessionalFisherman
from prod.model.entity.fisherman import MasterFisherman


class FishermenCreator:
    NAMES = ("James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda", "David", "Elizabeth",
             "William", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen",
             "Christopher", "Lisa", "Daniel", "Nancy", "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra",
             "Donald", "Ashley", "Steven", "Kimberly", "Paul", "Andrew", "Joshua", "Kenneth", "Kevin", "Brian",
             "George", "Timothy", "Ronald", "Edward", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas")

    LASTNAMES = ("Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
                 "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor",
                 "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez",
                 "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright",
                 "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Hall",
                 "Rivera", "Campbell", "Mitchell", "Carter", "Roberts")

    MIN_AGE = 16
    MAX_AGE = 80
    EXPERIENCE_MIN = 1
    EXPERIENCE_MAX = 5
    LUCK_MIN = 1
    LUCK_MAX = 5

    def __init__(self, max_num_fishes):
        self.max_num_fishes = max_num_fishes

    def num_of_fishes_for_fisherman(self, fisherman: Fisherman) -> int:
        luck = fisherman.luck / self.LUCK_MAX
        experience = fisherman.experience / self.EXPERIENCE_MAX
        # print(luck, experience)
        num_fishes = int((luck * 30 + experience * 70) * random.randint(0, 100)) % self.max_num_fishes
        # num_fishes = 3
        return num_fishes

    @classmethod
    def _get_Fisherman(cls, first_name, last_name, age, luck, experience):
        if experience < 2:
            return NoviceFisherman(first_name, last_name, age, luck, experience)
        if 2 <= experience < 3:
            return AmateurFisherman(first_name, last_name, age, luck, experience)
        if 3 <= experience < 4:
            return ProfessionalFisherman(first_name, last_name, age, luck, experience)
        return MasterFisherman(first_name, last_name, age, luck, experience)

    @classmethod
    def _create_participant(cls) -> Fisherman:
        first_name = random.choice(cls.NAMES)
        last_name = random.choice(cls.LASTNAMES)
        age = random.randint(cls.MIN_AGE, cls.MAX_AGE)
        experience = round(random.uniform(cls.EXPERIENCE_MIN, cls.EXPERIENCE_MAX), 3)
        luck = round(random.uniform(cls.LUCK_MIN, cls.LUCK_MAX), 3)
        return cls._get_Fisherman(first_name, last_name, age, experience, luck)

    @classmethod
    def create_participants(cls, quantity) -> List[Fisherman]:
        return [cls._create_participant() for _ in range(quantity)]
