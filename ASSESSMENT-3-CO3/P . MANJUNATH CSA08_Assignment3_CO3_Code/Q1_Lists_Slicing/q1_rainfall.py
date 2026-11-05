import random
import time

def naive_average(readings):
    return [sum(readings[i:i + 7]) / 7 for i in range(len(readings) - 6)]

def running_average(readings):
    if len(readings) < 7:
        return []
    result = []
    current = sum(readings[:7])
    result.append(current / 7)
    for i in range(7, len(readings)):
        current += readings[i] - readings[i - 7]
        result.append(current / 7)
    return result

readings = [12, 0, 5, 8, 10, 0, 7, 14, 9, 0, 6, 11, 4, 8]
weekly_totals = [sum(readings[i:i + 7]) for i in range(0, len(readings), 7)]
print("Weekly totals:", weekly_totals)

if readings:
    print("Maximum reading and position:", max(readings), readings.index(max(readings)))
    print("Minimum reading and position:", min(readings), readings.index(min(readings)))
print("7-day moving average:", running_average(readings))
print("Dry days (0-based positions):", [i for i, value in enumerate(readings) if value == 0])
print("readings[7:14]:", readings[7:14])
print("readings[-7:]:", readings[-7:])
print("readings[::7]:", readings[::7])

for n in (365, 36500, 365000):
    data = [random.randint(0, 30) for _ in range(n)]
    start = time.perf_counter()
    a = naive_average(data)
    naive_time = time.perf_counter() - start
    start = time.perf_counter()
    b = running_average(data)
    running_time = time.perf_counter() - start
    print(f"{n} readings: naive={naive_time:.6f}s, running={running_time:.6f}s, same={a == b}")

print("Empty list test:", running_average([]))
print("Short list test:", running_average([1, 2, 3, 4, 5]))
