class Fisherman:

    def __init__(self, first_name, last_name, age, experience, luck):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._experience = experience
        self._luck = luck

    def __repr__(self):
        return f"{self._first_name} " \
               f"{self._last_name}: " \
               f"{self._age} y.o. " \
               f"- luck{self._luck} " \
               f"- experience: {self._experience}" \

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def age(self):
        return self._age

    @property
    def luck(self):
        return self._luck

    @luck.setter
    def luck(self, luck):
        self._luck = luck

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, experience):
        self._experience = experience


class NoviceFisherman(Fisherman):
    MASTER_LEVEL = "Novice"
    def __repr__(self):
        return self.MASTER_LEVEL + " " + super().__repr__()

class AmateurFisherman(Fisherman):
    MASTER_LEVEL = "Amateur"
    def __repr__(self):
        return self.MASTER_LEVEL + " " + super().__repr__()

class ProfessionalFisherman(Fisherman):
    MASTER_LEVEL = "Professional"
    def __repr__(self):
        return self.MASTER_LEVEL + " " + super().__repr__()

class MasterFisherman(Fisherman):
    MASTER_LEVEL = "Master"
    def __repr__(self):
        return self.MASTER_LEVEL + " " + super().__repr__()




