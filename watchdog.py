import random

battery = 100.0
NUM_WAYPOINTS = 10

for waypoint in range(1, NUM_WAYPOINTS + 1):
    battery -= random.uniform(1.5, 3.5)
    print(f"Waypoint {waypoint}/{NUM_WAYPOINTS} | Battery: {battery:.1f}%")

    if battery < 75:
        print("[EMERGENCY RETURN TRIGGERED]")
        break
    elif battery < 80:
        print("[CAUTION] Battery below 80%")