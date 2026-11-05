import random
import string
import time
from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]
STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in text.lower().translate(str.maketrans("", "", string.punctuation)).split():
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

def group_by_district(records):
    groups = {}
    for district, complaint in records:
        groups.setdefault(district, []).append(complaint)
    return groups

print(top(frequencies(calls, STOP), 3))
records = [("Chennai", "Seeds delayed"), ("Madurai", "Water shortage"), ("Chennai", "Fertiliser issue")]
groups = group_by_district(records)
print("Complaints by district:", {key: len(value) for key, value in groups.items()})
print("District complaint lists:", groups)
print("Empty text:", frequencies([""], STOP))
print("Case and punctuation:", frequencies(["SEEDS, seeds! Price."], STOP))
counts = frequencies(calls, STOP)
print("keys:", list(counts.keys()))
print("values:", list(counts.values()))
print("items:", list(counts.items()))

vocabulary = ["seed", "water", "crop", "price", "loan", "fertiliser"]
for n in (1000, 10000, 100000):
    data = [" ".join(random.choices(vocabulary, k=8)) for _ in range(n)]
    start = time.perf_counter()
    result = frequencies(data, set())
    dict_time = time.perf_counter() - start
    start = time.perf_counter()
    counter_result = Counter(word for line in data for word in line.split())
    counter_time = time.perf_counter() - start
    words = set(word for line in data for word in line.split())
    start = time.perf_counter()
    slow_result = {word: sum(line.split().count(word) for line in data) for word in words}
    list_count_time = time.perf_counter() - start
    print(f"{n} complaints: dict={dict_time:.6f}s Counter={counter_time:.6f}s list.count={list_count_time:.6f}s")
    print("Results match:", result == counter_result == slow_result)
