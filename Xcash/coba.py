# Initialize the population on day 1
population = 1

# Iterate over days 2 to 50
for day in range(2, 51):
    if day % 3 == 0:  # Thanos appears
        population = population // 2  # Thanos halves the population (rounded down)
    else:  # Dr. Strange appears
        population = population * 3  # Dr. Strange triples the population

# Print the result
print(f"Jumlah penduduk Planet Thanos di hari ke-50 adalah: {population}")
