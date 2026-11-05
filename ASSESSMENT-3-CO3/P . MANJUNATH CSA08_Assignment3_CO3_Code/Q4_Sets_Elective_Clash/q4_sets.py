import random
import time

ai_elective = {"192311001", "192311004", "192311007", "192311009"}
iot_elective = {"192311002", "192311004", "192311009", "192311010"}
all_students = {f"1923110{i:02d}" for i in range(1, 11)}

both = ai_elective & iot_elective
exactly_one = ai_elective ^ iot_elective
neither = all_students - (ai_elective | iot_elective)

print("clash      :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither    :", sorted(neither))

both_method = ai_elective.intersection(iot_elective)
one_method = ai_elective.symmetric_difference(iot_elective)
neither_method = all_students.difference(ai_elective.union(iot_elective))
print("Set methods match:", both == both_method and exactly_one == one_method and neither == neither_method)

for n in (10000, 100000, 1000000):
    values = list(range(n))
    value_set = set(values)
    target = n - 1
    start = time.perf_counter()
    found_list = target in values
    list_time = time.perf_counter() - start
    start = time.perf_counter()
    found_set = target in value_set
    set_time = time.perf_counter() - start
    print(f"{n} values: list={list_time:.8f}s set={set_time:.8f}s match={found_list == found_set}")

a = {"A", "B", "C"}
b = {"B", "C", "D"}
print("Empty intersection:", set() & b)
print("Identical electives:", a & a)
print("Small case:", sorted(a & b), sorted(a ^ b))
