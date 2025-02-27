from aocd import get_data, submit


def extend_memory(elem, position, extended_memory):
    for i in range(int(elem[0])):
        extended_memory.append(str(position))
    for i in range(int(elem[1])):
        extended_memory.append(".")
    return extended_memory


def compact_memory(extended_memory):
    result = extended_memory[:]
    left = 0
    right = len(result) - 1

    while left < right:
        while left < right and result[left] != ".":
            left += 1
        while left < right and result[right] == ".":
            right -= 1
        if left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
    return result


def count_contiguous(extended_memory, right):
    count = 0
    character = extended_memory[right]
    while right >= 0 and extended_memory[right] == character:
        count += 1
        right -= 1
    return count


def count_contiguous_spaces(extended_memory, left):
    count = 0
    while left < len(extended_memory) and extended_memory[left] == ".":
        count += 1
        left += 1
    return count


def find_dots(memory):
    dots = []
    n = len(memory)
    i = 0
    while i < n:
        if memory[i] == ".":
            start = i
            while i < n and memory[i] == ".":
                i += 1
            dots.append((start, i - start))
        else:
            i += 1
    return dots


def compact_memory_contiguous(extended_memory):
    result = extended_memory[:]
    right = len(result) - 1
    while right >= 0:
        dot_positions = find_dots(result)
        while result[right] == ".":
            right -= 1
        contiguous_spaces = count_contiguous(result, right)
        for position, count in dot_positions:
            if count >= contiguous_spaces and position <= right:
                for i in range(contiguous_spaces):
                    result[position + i] = result[right - i]
                    result[right - i] = "."
                break
        right -= contiguous_spaces
    return result


def solve_a(data):
    if len(data) % 2 != 0:
        data += "0"
    original_memory = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
    extended_memory = []
    for position, elem in enumerate(original_memory):
        extended_memory = extend_memory(elem, position, extended_memory)
    extended_memory = compact_memory(extended_memory)
    return sum(
        int(elem) * position
        for position, elem in enumerate(extended_memory)
        if elem != "."
    )


def solve_b(data):
    if len(data) % 2 != 0:
        data += "0"
    original_memory = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
    extended_memory = []
    for position, elem in enumerate(original_memory):
        extended_memory = extend_memory(elem, position, extended_memory)
    extended_memory = compact_memory_contiguous(extended_memory)
    return sum(
        int(elem) * position
        for position, elem in enumerate(extended_memory)
        if elem != "."
    )


data = get_data(day=9, year=2024)
total_a = solve_a(data)
print(total_a)
submit(total_a, day=9, year=2024, part="a")
total_b = solve_b(data)
print(total_b)
submit(total_b, day=9, year=2024, part="b")
