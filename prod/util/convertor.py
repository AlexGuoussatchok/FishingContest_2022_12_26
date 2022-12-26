from prod.model.entity.fisherman import Fisherman


class Convertor:

    @staticmethod
    def convert_to_string(list_of_participants):
        if not isinstance(list_of_participants, (list, tuple)):
            return "List is empty"

        participants = "List of participants:"

        for fisherman in list_of_participants:
            if isinstance(fisherman, Fisherman):
                participants += "\n" + str(fisherman)

        return participants
