import random

robot_name = input("Enter robot name: ")

distance_km = 0
direction = "Forward"

print(f"\n🤖 Robot {robot_name} started moving (KM by KM with Random Events)")

# Robot tries to move 10 km
for km in range(1, 11):

    event = random.choice(["human", "obstacle", "none"])

    if event == "human":
        print(f"Human detected → {robot_name} is waiting")
        print(f"Distance remains: {distance_km} km")

    elif event == "obstacle":
        direction = random.choice(["Left", "Right"])
        distance_km += 1
        print(f"Obstacle detected → Direction changed to {direction}")
        print(f"{robot_name} moved 1 km")
        print(f"Total distance: {distance_km} km")

    else:
        distance_km += 1
        print(f"{robot_name} moved 1 km in {direction}")
        print(f"Total distance: {distance_km} km")

print(f"\n✅ {robot_name} travelled total distance: {distance_km} km")
