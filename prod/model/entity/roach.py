from prod.model.entity.fish import Fish


class Roach(Fish):
    LENGTH_MIN = 150
    LENGTH_MAX = 350
    WEIGHT_MIN = 150
    WEIGHT_MAX = 450
    NAME = "Roach"

    def __init__(self):
        super().__init__(self.NAME, self.get_length(self.LENGTH_MIN, self.LENGTH_MAX),
                         self.get_weight(self.WEIGHT_MIN, self.WEIGHT_MAX))
