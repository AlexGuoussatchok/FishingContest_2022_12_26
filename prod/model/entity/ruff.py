from prod.model.entity.fish import Fish


class Ruff(Fish):
    LENGTH_MIN = 80
    LENGTH_MAX = 185
    WEIGHT_MIN = 15
    WEIGHT_MAX = 25
    NAME = "Ruff"

    def __init__(self):
        super().__init__(self.NAME, self.get_length(self.LENGTH_MIN, self.LENGTH_MAX),
                         self.get_weight(self.WEIGHT_MIN, self.WEIGHT_MAX))
