from individual import create_individual


class Population(list):
    def __init__(self, *args):
        super().__init__(*args)


def create_population(size=0):
    return Population([create_individual() for i in range(size)])
