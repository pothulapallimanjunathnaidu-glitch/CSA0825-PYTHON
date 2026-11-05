import time


message = ""
for i in range(1, 6):
    message += f"Message line {i}: Your service update is ready.\\n"
print("Using +=:")
print(message)


lines = []
for i in range(1, 6):
    lines.append(f"Message line {i}: Your service update is ready.")
joined_message = "\\n".join(lines)
print("Using join:")
print(joined_message)


name = "Student"
balance = 125.50
sms = f"Hello {name}, your balance is Rs. {balance:.2f}."
print("Formatted SMS:", sms)


def using_plus(n):
    result = ""
    for i in range(n):
        result += f"Line {i}\\n"
    return result


def using_join(n):
    parts = [f"Line {i}" for i in range(n)]
    return "\\n".join(parts)


print("\\nBenchmark results (seconds):")
for n in (1000, 10000, 200000):
    plus_times = []
    join_times = []

    for _ in range(3):
        start = time.perf_counter()
        using_plus(n)
        plus_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        using_join(n)
        join_times.append(time.perf_counter() - start)

    plus_avg = sum(plus_times) / len(plus_times)
    join_avg = sum(join_times) / len(join_times)
    faster = "join" if join_avg < plus_avg else "+="

    print(f"{n}: += average = {plus_avg:.6f}s, "
          f"join average = {join_avg:.6f}s, faster = {faster}")
