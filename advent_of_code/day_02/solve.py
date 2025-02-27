from aocd import get_data
from aocd import submit

get_data = get_data(day=2, year=2024).splitlines()

# Part a
safe_elements = 0
for row in get_data:
    row_numbers = list(map(int, row.split(" ")))
    safe = True
    if (
        sorted(row_numbers) != row_numbers
        and sorted(row_numbers, reverse=True) != row_numbers
    ):
        safe = False
    if safe:
        for i in range(len(row_numbers) - 1):
            if (
                abs(row_numbers[i] - row_numbers[i + 1]) > 3
                or abs(row_numbers[i] - row_numbers[i + 1]) < 1
            ):
                safe = False
    if safe:
        safe_elements += 1

submit(safe_elements, part="a", day=2, year=2024)

# Part b
safe_elements = 0
for row in get_data:
    row_numbers = list(map(int, row.split(" ")))
    row_numbers_backup = row_numbers.copy()
    for i in range(len(row_numbers_backup)):
        safe = True
        row_numbers = row_numbers_backup.copy()
        row_numbers.pop(i)
        if (
            sorted(row_numbers) != row_numbers
            and sorted(row_numbers, reverse=True) != row_numbers
        ):
            safe = False
        if safe:
            for i in range(len(row_numbers) - 1):
                if (
                    abs(row_numbers[i] - row_numbers[i + 1]) > 3
                    or abs(row_numbers[i] - row_numbers[i + 1]) < 1
                ):
                    safe = False
        if safe:
            print(row_numbers)
            safe_elements += 1
            break

print(safe_elements)
submit(safe_elements, part="b", day=2, year=2024)
