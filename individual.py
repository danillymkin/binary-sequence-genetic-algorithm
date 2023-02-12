import random

from constants import CODE_SEQUENCE_LENGTH
from fitness_max import FitnessMax


class Individual(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.fitness = FitnessMax()


def create_individual():
    return Individual([random.randrange(-1, 2, 2) for i in range(CODE_SEQUENCE_LENGTH)])


def calc_individual_fitness(individual: Individual):
    acf = calc_individual_acf(individual)
    psl = get_individual_psl(acf)

    # if psl > 5:
    #     return 0

    return CODE_SEQUENCE_LENGTH / psl


def calc_individual_acf(individual: Individual):
    acf = []

    for k in range(0, len(individual) - 1):
        acf_k = 0

        for i in range(k + 1, len(individual)):
            acf_k += individual[i] * individual[i - 1 - k]

        acf.append(acf_k)

    return acf


def get_individual_psl(acf):
    return max(acf)
