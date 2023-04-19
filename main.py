import matplotlib.pyplot as plt
import numpy as np
import csv

from constants import POPULATION_SIZE, CODE_SEQUENCE_LENGTH
from individual import Individual
from population import Population


def main():
    population = Population.generate(POPULATION_SIZE)

    max_fitness_values = []
    mean_fitness_values = []

    best_fitness = 0
    best_individual = None

    generation_counter = 0

    while generation_counter < 50:
        generation_counter += 1

        # you can use roulette method, just uncomment bellow line and delete tournament line
        # offspring = population.roulette()

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
        best_acf = population[best_index].calc_acf()
        best_psl = population[best_index].calc_psl(best_acf)

        if max_fitness > best_fitness:
            best_fitness = max_fitness
            best_individual = Individual.clone(population[best_index])

        if generation_counter == 1 or generation_counter == 3 or generation_counter == 50:
            write_population_to_csv(generation_counter, population)

        print(f"The population {generation_counter}: Max fitness = {max_fitness}, Mean fitness = {mean_fitness}, PSL = {best_psl}")
        print("The best individual = ", *population[best_index], "\n")

    # charts
    show_max_mean_fitness_graph(max_fitness_values, mean_fitness_values)
    show_acf_graph(best_individual)


def show_max_mean_fitness_graph(max_fitness, mean_fitness):
    plt.plot(max_fitness, color='red')
    plt.plot(mean_fitness, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Max / Mean fitness')
    plt.title('Dependence of max and mean fitness on generation')
    plt.show()


def show_acf_graph(individual):
    right_acf = individual.calc_acf()
    left_acf = reversed(right_acf)
    acf = [*left_acf, CODE_SEQUENCE_LENGTH, *right_acf]

    length_of_side = len(right_acf)

    y = np.arange(-length_of_side, length_of_side + 1, 1)

    plt.title('ACF of the best individual')
    plt.grid(True)
    plt.plot(y, acf)
    plt.show()


def write_population_to_csv(population_number, population):
    mode = 'w' if population_number == 1 else 'a'
    with open('populations.csv', mode) as csv_file:
        writer = csv.writer(csv_file, delimiter=';')

        if population_number == 1:
            writer.writerow(['population_number', 'number in population', 'individual', 'PSL'])

        for index, individual in enumerate(population):
            acf = individual.calc_acf()
            psl = individual.calc_psl(acf)

            data = [population_number, index + 1, individual, psl]
            writer.writerow(data)

    csv_file.close()


if __name__ == "__main__":
    main()
