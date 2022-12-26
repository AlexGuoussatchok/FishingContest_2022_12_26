from prod.model.entity.fish import Fish


class Perch(Fish):
    LENGTH_MIN = 150
    LENGTH_MAX = 300
    WEIGHT_MIN = 200
    WEIGHT_MAX = 300
    NAME = "Perch"

    def __init__(self):
        super().__init__(self.NAME, self.get_length(self.LENGTH_MIN, self.LENGTH_MAX),
                         self.get_weight(self.WEIGHT_MIN, self.WEIGHT_MAX))
