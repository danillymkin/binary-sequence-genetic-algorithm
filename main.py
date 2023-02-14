import matplotlib.pyplot as plt

from constants import POPULATION_SIZE
from population import Population


def main():
    population = Population.generate(POPULATION_SIZE)

    max_fitness_values = []
    mean_fitness_values = []

    generation_counter = 0

    # while max(fitness_values) <= 8.6 and generation_counter < 100:
    while generation_counter < 100:
        generation_counter += 1

        offspring = population.tournament()
        offspring.crossover()
        offspring.mutation()

        offspring.update_fitness_values()

        population[:] = offspring
        fitness_values = [individual.fitness_value for individual in population]

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
