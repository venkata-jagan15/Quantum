import random

# Fitness function
def fitness(x):
    return x * x

# Initial population
population = [random.randint(0, 31) for _ in range(6)]

# Convert to binary
def to_binary(n):
    return format(n, '05b')

# Selection (best 2)
def selection(pop):
    return sorted(pop, key=fitness, reverse=True)[:2]

# Crossover
def crossover(p1, p2):
    b1 = to_binary(p1)
    b2 = to_binary(p2)
    
    point = random.randint(1, 4)
    
    child1 = int(b1[:point] + b2[point:], 2)
    child2 = int(b2[:point] + b1[point:], 2)
    
    return child1, child2

# Mutation
def mutation(x):
    b = list(to_binary(x))
    idx = random.randint(0, 4)
    b[idx] = '1' if b[idx] == '0' else '0'
    return int(''.join(b), 2)

# Genetic Algorithm
for generation in range(5):
    print("\nGeneration", generation)
    print("Population:", population)
    
    # Selection
    p1, p2 = selection(population)
    
    # Crossover
    c1, c2 = crossover(p1, p2)
    
    # Mutation
    c1 = mutation(c1)
    c2 = mutation(c2)
    
    # New population
    population = [p1, p2, c1, c2,
                  random.randint(0, 31),
                  random.randint(0, 31)]

# Final result
best = max(population, key=fitness)
print("\nBest Solution:", best)
print("Fitness Value:", fitness(best))