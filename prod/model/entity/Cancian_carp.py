from prod.model.entity.fish import Fish


class CancianCarp(Fish):
    LENGTH_MIN = 100
    LENGTH_MAX = 200
    WEIGHT_MIN = 100
    WEIGHT_MAX = 200
    NAME = "Cancian Carp"

    def __init__(self):
        super().__init__(self.NAME, self.get_length(self.LENGTH_MIN, self.LENGTH_MAX),
                         self.get_weight(self.WEIGHT_MIN, self.WEIGHT_MAX))

