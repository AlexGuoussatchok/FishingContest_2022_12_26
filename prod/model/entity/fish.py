import random



class Fish:

    def __init__(self, fish_name, length, weight):
        self._fish_name = fish_name
        self._length = length
        self._weight = weight
        # print(f"{self._fish_name}: WEIGHT={self._weight}")

    @property
    def fish_name(self):
        return self._fish_name

    @fish_name.setter
    def fish_name(self, fish_name):
        self._fish_name = fish_name

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if length > 0:
            self._length = length
        else:
            raise Exception("The weight cannot be less or equal to 0")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self._weight = weight

    @classmethod
    def get_length(cls, length_min, length_max):
        length = random.randint(length_min, length_max)
        return length

    @classmethod
    def get_weight(cls, weight_min, weight_max):
        weight = random.randint(weight_min, weight_max)
        return weight

    def __repr__(self):
        return f"{self._fish_name}: length - {self._length} mm., weight - {self._weight} gr."
