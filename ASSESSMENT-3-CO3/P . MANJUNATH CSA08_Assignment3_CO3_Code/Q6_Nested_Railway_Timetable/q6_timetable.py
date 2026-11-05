import random
import time

timetable = {
    "12601": {"name": "Chennai Express", "stops": [("Chennai", "06:00", "06:10"), ("Vijayawada", "12:00", "12:05"), ("Howrah", "22:00", "22:10")], "days": {"Mon", "Wed", "Fri"}},
    "12602": {"name": "Kaveri Express", "stops": [("Chennai", "07:00", "07:10"), ("Bengaluru", "12:00", "12:10"), ("Mysuru", "15:00", "15:10")], "days": {"Tue", "Thu", "Sat"}},
    "12603": {"name": "Coastal Express", "stops": [("Chennai", "08:00", "08:10"), ("Nellore", "10:00", "10:05"), ("Vijayawada", "13:00", "13:10")], "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}},
    "12604": {"name": "Hill Express", "stops": [("Bengaluru", "09:00", "09:10"), ("Salem", "12:00", "12:05"), ("Coimbatore", "15:00", "15:10")], "days": {"Sun"}},
    "12605": {"name": "Southern Express", "stops": [("Chennai", "10:00", "10:10"), ("Salem", "14:00", "14:05"), ("Coimbatore", "17:00", "17:10")], "days": {"Mon", "Wed", "Fri"}}
}

def find_trains(data, station, day):
    found = []
    for number, details in data.items():
        if day in details["days"]:
            for stop, arrival, departure in details["stops"]:
                if stop.lower() == station.lower():
                    found.append((number, details["name"], departure))
    return sorted(found, key=lambda item: item[2])

for number, details in timetable.items():
    print(number, details["name"])
    for stop in details["stops"]:
        print(" ", stop)
print("Trains at Chennai on Monday:", find_trains(timetable, "Chennai", "Mon"))
print("Unknown station:", find_trains(timetable, "Unknown", "Mon"))
print("Not running that day:", find_trains(timetable, "Bengaluru", "Mon"))
print("Third station departure:", timetable["12601"]["stops"][2][2])

index = {}
for number, details in timetable.items():
    for station, arrival, departure in details["stops"]:
        index.setdefault(station.lower(), []).append(number)
print("Station index:", index)

for n in (100, 1000, 10000):
    data = {}
    for i in range(n):
        train_no = str(10000 + i)
        stops = [(f"Station{j}", "08:00", "08:05") for j in range(10)]
        data[train_no] = {"name": f"Train{i}", "stops": stops, "days": {"Mon", "Wed"}}
    station_index = {}
    for train_no, details in data.items():
        for station, arrival, departure in details["stops"]:
            station_index.setdefault(station.lower(), []).append(train_no)
    target = "Station5"
    start = time.perf_counter()
    scan = [train for train, details in data.items() if any(s.lower() == target.lower() for s, a, d in details["stops"])]
    scan_time = time.perf_counter() - start
    start = time.perf_counter()
    indexed = station_index.get(target.lower(), [])
    index_time = time.perf_counter() - start
    print(f"{n} trains: scan={scan_time:.6f}s index={index_time:.8f}s matches={len(indexed)}")
