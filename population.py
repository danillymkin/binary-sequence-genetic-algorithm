from individual import Individual


class Population(list):
    def __init__(self, *args):
        super().__init__(*args)


def create_population(size=0):
    return Population([Individual.create() for i in range(size)])
