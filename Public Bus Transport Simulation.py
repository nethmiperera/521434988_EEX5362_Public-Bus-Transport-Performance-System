# ------------------------------
# Public Bus Transport Simulation
# ------------------------------

import random
import statistics

# Define simulation parameters
NUM_BUSES = 5
NUM_STOPS = 10
SIMULATION_RUNS = 20  # number of time periods

# Random seed for reproducibility
random.seed(42)

# Initialize data
bus_speeds = [random.uniform(30, 60) for _ in range(NUM_BUSES)]  # km/h
passenger_demand = [random.randint(5, 20) for _ in range(NUM_STOPS)]  # passengers per stop
waiting_times = []
bus_utilization = []

print("🚍 Public Bus Transportation Simulation Started...\n")

# Simulate multiple time periods
for t in range(SIMULATION_RUNS):
    total_wait = 0
    total_util = 0

    for bus_id in range(NUM_BUSES):
        # Random trip delay (minutes)
        delay = random.uniform(0, 10)

        # Passengers served based on speed and delay
        served = max(0, int(random.choice(passenger_demand) - delay / 2))
        waiting = max(0, random.choice(passenger_demand) - served)

        # Utilization: higher if bus serves more passengers
        utilization = served / (served + waiting + 1)

        total_wait += waiting
        total_util += utilization

    waiting_times.append(total_wait / NUM_BUSES)
    bus_utilization.append(total_util / NUM_BUSES)

# Calculate performance metrics
avg_wait_time = statistics.mean(waiting_times)
avg_utilization = statistics.mean(bus_utilization)

print(f"Average passenger waiting time per bus: {avg_wait_time:.2f} minutes")
print(f"Average bus utilization rate: {avg_utilization:.2%}")
print("\n✅ Simulation completed successfully.")

