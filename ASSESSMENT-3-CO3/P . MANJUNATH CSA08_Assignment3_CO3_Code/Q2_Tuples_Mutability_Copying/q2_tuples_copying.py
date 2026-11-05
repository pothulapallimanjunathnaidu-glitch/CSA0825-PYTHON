rows = 3
cols = 4

bad = [[0] * cols] * rows
bad[0][1] = 7

good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7

print("bad :", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])

stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print(stops[(13.0418, 80.2341)])

original = [[1, 2], [3, 4]]

alias = original
shallow = original[:]
deep = [row[:] for row in original]

original[0][0] = 99

print("Original:", original)
print("Alias:", alias)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)

item = ([10, 20], 30)
item[0].append(40)

print("Tuple with List:", item)