class Allergies(object):

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        allergy_test = ["eggs", "peanuts", "shellfish", "strawberries",
                        "tomatoes", "chocolate", "pollen", "cats"]
        allergy_list = []

        for val, allergy in enumerate(allergy_test):
            if 2**val & self.score:
                allergy_list.append(allergy)

        return allergy_list
