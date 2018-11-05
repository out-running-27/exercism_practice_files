class Allergies(object):
    ALLERGY_TEST = ["eggs", "peanuts", "shellfish", "strawberries",
                    "tomatoes", "chocolate", "pollen", "cats"]

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):

        allergy_list = []

        for val, allergy in enumerate(self.ALLERGY_TEST):
            if 1 << val & self.score:
                allergy_list.append(allergy)

        return allergy_list
