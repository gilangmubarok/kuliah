import random

# 1. Inisialisasi Koordinat Kota (x, y)
cities = cities = [
    (0, 0),
    (2, 3),
    (5, 1),
    (7, 4),
    (3, 7),
    (8, 8),
    (1, 6),
    (6, 2),
    (9, 5),
    (4, 9)
]

# Fungsi untuk menghitung jarak Euclidean antara dua kota
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Fungsi untuk menghitung total jarak seluruh rute (termasuk kembali ke kota awal)
def total_distance(route):
    dist = sum(distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))
    dist += distance(cities[route[-1]], cities[route[0]])  # Kembali ke titik awal
    return dist

# 2. Parameter Genetic Algorithm
population_size = 10
num_generations = 10
mutation_rate = 0.1 

# Inisialisasi Populasi Awal (Permutasi acak indeks kota)
population = [random.sample(range(len(cities)), len(cities)) for _ in range(population_size)]

# 3. Main Genetic Algorithm Loop
for generation in range(num_generations):
    # Evaluasi Fitness (Invers dari total jarak)
    fitness_scores = [1 / total_distance(route) for route in population]
    
    # Selection: Tournament Selection
    selected_routes = []
    for _ in range(population_size):
        tournament = random.sample(range(population_size), 5)
        # Ambil pemenang tournament dengan nilai fitness tertinggi
        best_in_tournament = max(tournament, key=lambda idx: fitness_scores[idx])
        selected_routes.append(best_in_tournament)
    
    # Reproduction: Crossover & Mutation
    new_population = []
    for i in range(0, population_size, 2):
        parent1 = population[selected_routes[i]]
        parent2 = population[selected_routes[i + 1]]
        
        # Order Crossover
        crossover_point = random.randint(0, len(cities) - 1)
        child1 = parent1[:crossover_point] + [c for c in parent2 if c not in parent1[:crossover_point]]
        child2 = parent2[:crossover_point] + [c for c in parent1 if c not in parent2[:crossover_point]]
        
        # Swap Mutation
        if random.random() < mutation_rate:
            m1, m2 = random.sample(range(len(cities)), 2)
            child1[m1], child1[m2] = child1[m2], child1[m1]
            child2[m1], child2[m2] = child2[m2], child2[m1]
            
        new_population.extend([child1, child2])
    
    population = new_population

    best_current = min(population, key=total_distance)

    print(
        f"Generation {generation + 1}: "
        f"{total_distance(best_current):.4f}"
    )

# 4. Ambil dan Tampilkan Hasil Terbaik
best_route = min(population, key=total_distance)
best_distance = total_distance(best_route)

print("=== GA TSP OPTIMIZATION RESULT ===")
print("Best Route Found (City Indices):", best_route)
print("Total Minimum Distance          :", round(best_distance, 4))