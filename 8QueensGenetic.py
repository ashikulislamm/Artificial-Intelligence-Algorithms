import random

# Constants
N_QUEENS = 8
POPULATION_SIZE = 100
MAX_GENERATIONS = 1000
MUTATION_RATE = 0.03


# function to create a random solution
def create_individual():
    return [random.randint(0, N_QUEENS - 1) for _ in range(N_QUEENS)]

# Fitness function
def fitness(individual):
    non_attacking_pairs = 0
    for i in range(N_QUEENS):
        for j in range(i + 1, N_QUEENS):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != j - i:
                non_attacking_pairs += 1
    return non_attacking_pairs

# Selection function
def selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [fitness / total_fitness for fitness in fitnesses]
    selected_index = random.choices(range(POPULATION_SIZE), probabilities)[0]
    return population[selected_index]

# Crossover function
def crossover(parent1, parent2):
    crossover_point = random.randint(0, N_QUEENS - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Mutation function
def mutate(individual):
    if random.random() < MUTATION_RATE:
        mutate_index = random.randint(0, N_QUEENS - 1)
        individual[mutate_index] = random.randint(0, N_QUEENS - 1)

# Main Genetic Algorithm function
def genetic_algorithm():
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    for generation in range(MAX_GENERATIONS):
        fitnesses = [fitness(individual) for individual in population]
        if max(fitnesses) == N_QUEENS * (N_QUEENS - 1) // 2:
            break
        
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        
        population = new_population
        best_fitness = max(fitnesses)
        best_individual = population[fitnesses.index(best_fitness)]
        print(f"Generation {generation}: Best fitness = {best_fitness}")
    
    best_fitness = max(fitnesses)
    best_individual = population[fitnesses.index(best_fitness)]
    return best_individual, best_fitness,generation

if __name__ == "__main__":
    solution, fitness_value,generation = genetic_algorithm()
    if fitness_value == N_QUEENS * (N_QUEENS - 1) // 2:
        print("Solution found!")
    else:
        print("No perfect solution found.")
    print("Best solution:", solution)
    print("Generation : ",generation)
    print("Fitness of best solution:", fitness_value)
