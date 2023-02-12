import random
import matplotlib.pyplot as plt

from constants import POPULATION_SIZE, CROSSOVER_PROBABILITY, MUTATION_PROBABILITY, CODE_SEQUENCE_LENGTH
from individual import calc_individual_fitness
from population import create_population
from utils import tournament, clone, crossover, mutation


def main():
    population = create_population(POPULATION_SIZE)

    fitness_values = list(map(calc_individual_fitness, population))

    for individual, fitness_value in zip(population, fitness_values):
        individual.fitness.values = [fitness_value]

    fitness_values = [individual.fitness.values[0] for individual in population]

    max_fitness_values = []
    mean_fitness_values = []

    generation_counter = 0

    # while max(fitness_values) <= 8.6 and generation_counter < 100:
    while generation_counter < 100:
        generation_counter += 1

        # selective selection
        offspring = tournament(population)
        offspring = list(map(clone, offspring))

        # crossover even and odd individuals
        for individual1, individual2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CROSSOVER_PROBABILITY:
                crossover(individual1, individual2)

        # mutation
        for individual in offspring:
            if random.random() < MUTATION_PROBABILITY:
                mutation(individual, 1.0 / CODE_SEQUENCE_LENGTH)

        # calculate the fitness of the offspring
        offspring_fitness_values = map(calc_individual_fitness, offspring)
        for individual, fitness_value in zip(offspring, offspring_fitness_values):
            individual.fitness.values = [fitness_value]

        # update the population and the list of its fitness
        population[:] = offspring
        fitness_values = [individual.fitness.values[0] for individual in population]

        # statistics
        max_fitness = max(fitness_values)
        mean_fitness = sum(fitness_values) / len(population)
        max_fitness_values.append(max_fitness)
        mean_fitness_values.append(mean_fitness)
        best_index = fitness_values.index(max(fitness_values))

        print(f"The population {generation_counter}: Max fitness = {max_fitness}, Mean fitness = {mean_fitness}")
        print("The best individual = ", *population[best_index], "\n")

    # charts
    plt.plot(max_fitness_values, color='red')
    plt.plot(mean_fitness_values, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Max / Mean fitness')
    plt.title('Dependence of max and mean fitness on generation')
    plt.show()


if __name__ == "__main__":
    main()
