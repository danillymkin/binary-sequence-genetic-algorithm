import random

from constants import MUTATION_PROBABILITY
from individual import Individual
from population import Population


def clone(value: Individual):
    individual = Individual(value[:])
    individual.fitness.values = value.fitness.values
    return individual


def crossover(individual1: Individual, individual2: Individual):
    cutting_point = random.randint(2, len(individual1) - 3)
    individual1[cutting_point:], individual2[cutting_point:] = individual2[cutting_point:], individual1[cutting_point:]


def mutation(individual: Individual, probability_gene_mutation):
    for i in range(len(individual)):
        if random.random() < probability_gene_mutation:
            individual[i] = -1 if individual[i] == 1 else 1


def tournament(population: Population):
    offspring = []
    population_len = len(population)

    for i in range(population_len):
        individual1 = individual2 = individual3 = 0

        while individual1 == individual2 or individual1 == individual3 or individual2 == individual3:
            individual1 = random.randint(0, population_len - 1)
            individual2 = random.randint(0, population_len - 1)
            individual3 = random.randint(0, population_len - 1)

        offspring.append(max([population[individual1], population[individual2], population[individual3]], key=lambda individual: individual.fitness.values[0]))

    return offspring
