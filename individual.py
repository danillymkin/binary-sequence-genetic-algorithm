import random

from constants import CODE_SEQUENCE_LENGTH


class Individual(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.fitness_value = self.calc_fitness()

    @staticmethod
    def create():
        return Individual([random.randrange(-1, 2, 2) for i in range(CODE_SEQUENCE_LENGTH)])

    @staticmethod
    def clone(value):
        individual = Individual(value[:])
        individual.fitness_value = value.fitness_value
        return individual

    def mutation(self):
        gene_for_mutation = random.randint(0, CODE_SEQUENCE_LENGTH - 1)
        self[gene_for_mutation] = -1 if self[gene_for_mutation] == 1 else 1

    def calc_fitness(self):
        acf = self.calc_acf()
        psl = self.calc_psl(acf)

        return CODE_SEQUENCE_LENGTH / psl

    def calc_acf(self):
        acf = []

        for k in range(0, len(self) - 1):
            acf_k = 0

            for i in range(k + 1, len(self)):
                acf_k += self[i] * self[i - 1 - k]

            acf.append(acf_k)

        return acf

    def calc_psl(self, acf):
        return max(acf)
