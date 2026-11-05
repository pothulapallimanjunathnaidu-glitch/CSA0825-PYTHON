import time


def original_message(count):
    message = ""
    for i in range(1, count + 1):
        message += f"Message line {i}: Your service update is ready.\\n"
    return message


def optimized_message(count):
    parts = []
    for i in range(1, count + 1):
        parts.append(f"Message line {i}: Your service update is ready.")
    return "\\n".join(parts) + ("\\n" if count > 0 else "")


print("Optimized message example:")
print(optimized_message(5))


print("\\nBenchmark and output validation:")
for n in (1000, 10000, 200000):
    original_times = []
    optimized_times = []

    for _ in range(3):
        start = time.perf_counter()
        original = original_message(n)
        original_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        optimized = optimized_message(n)
        optimized_times.append(time.perf_counter() - start)

    original_avg = sum(original_times) / len(original_times)
    optimized_avg = sum(optimized_times) / len(optimized_times)
    same = original == optimized

    print(f"{n} lines: original = {original_avg:.6f}s, "
          f"optimized = {optimized_avg:.6f}s, same output = {same}")
