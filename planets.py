test_cases = int(input())

for _ in range(test_cases):
    num_planets, max_connections = map(int, input().split())
    
    planet_orbits = list(map(int, input().split()))
    
    orbit_counts = {}
    for orbit in planet_orbits:
        if orbit in orbit_counts:
            orbit_counts[orbit] += 1
        else:
            orbit_counts[orbit] = 1

    total_cost = 0
    for count in orbit_counts.values():
        if count > max_connections:
            total_cost += max_connections
        else:
            total_cost += count

    print(total_cost)
