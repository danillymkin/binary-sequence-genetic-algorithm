from individual import Individual


class Population(list):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def create(size=0):
        return Population([Individual.create() for i in range(size)])
