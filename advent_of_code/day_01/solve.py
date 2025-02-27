from aocd import get_data
from aocd import submit

get_data = get_data(day=1, year=2024)

list_1, list_2 = [], []

for elem in get_data.split("\n"):
    data1, data_2 = elem.split("   ")
    list_1.append(int(data1))
    list_2.append(int(data_2))

list_1.sort()
list_2.sort()

# Part a
total_sum = 0
for i in range(len(list_1)):
    total_sum += abs(list_1[i] - list_2[i])

submit(total_sum, part="a", day=1, year=2024)

# Part b
total_sum = 0
for elem in list_1:
    total_sum += elem * list_2.count(elem)

submit(total_sum, part="b", day=1, year=2024)
