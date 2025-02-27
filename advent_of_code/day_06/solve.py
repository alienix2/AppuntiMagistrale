from aocd import get_data
from aocd import submit

visited = []
loops = 0


def go_up(data, position_x, position_y):
    while data[position_x][position_y] != "#":
        data[position_x][position_y] = "X"
        if (position_x, position_y, "up") in visited:
            global loops
            loops += 1
            raise IndexError
        visited.append((position_x, position_y, "up"))
        position_x -= 1
    return position_x + 1, position_y


def go_down(data, position_x, position_y):
    while data[position_x][position_y] != "#":
        data[position_x][position_y] = "X"
        if (position_x, position_y, "down") in visited:
            global loops
            loops += 1
            raise IndexError
        visited.append((position_x, position_y, "down"))
        position_x += 1

    return position_x - 1, position_y


def go_left(data, position_x, position_y):
    while data[position_x][position_y] != "#":
        data[position_x][position_y] = "X"
        if (position_x, position_y, "left") in visited:
            global loops
            loops += 1
            raise IndexError
        visited.append((position_x, position_y, "left"))
        position_y -= 1
    return position_x, position_y + 1


def go_right(data, position_x, position_y):
    while data[position_x][position_y] != "#":
        data[position_x][position_y] = "X"
        if (position_x, position_y, "right") in visited:
            global loops
            loops += 1
            raise IndexError
        visited.append((position_x, position_y, "right"))
        position_y += 1
    return position_x, position_y - 1


def walk_direction(data, position_x, position_y, pointer):
    if pointer == "^":
        return go_up(data, position_x, position_y)
    elif pointer == "V":
        return go_down(data, position_x, position_y)
    elif pointer == "<":
        return go_left(data, position_x, position_y)
    elif pointer == ">":
        return go_right(data, position_x, position_y)


def change_direction(pointer):
    if pointer == "^":
        return ">"
    elif pointer == ">":
        return "V"
    elif pointer == "V":
        return "<"
    elif pointer == "<":
        return "^"


def find_position(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (
                data[i][j] == "^"
                or data[i][j] == "V"
                or data[i][j] == "<"
                or data[i][j] == ">"
            ):
                print(i, j)
                return i, j


def count_x(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "X":
                count += 1
    return count


def solve_a(data):
    position_x, position_y = find_position(data)
    pointer = data[position_x][position_y]
    while True:
        try:
            position_x, position_y = walk_direction(
                data, position_x, position_y, pointer
            )
            pointer = change_direction(pointer)
        except IndexError:
            break

    return count_x(data)


def solve_b():
    global loops
    global visited
    visited = []
    data = get_data(day=6, year=2024)
    original_data = [list(line) for line in data.splitlines()]
    position_x_pointer, position_y_pointer = find_position(original_data)
    for i in range(1, len(original_data)):
        print(i, loops)
        for j in range(len(original_data)):
            data = original_data
            if (i, j) != (position_x_pointer, position_y_pointer):
                data[i][j] = "#"
            position_x, position_y = position_x_pointer, position_y_pointer
            pointer = "^"
            while True:
                try:
                    position_x, position_y = walk_direction(
                        data, position_x, position_y, pointer
                    )
                    pointer = change_direction(pointer)
                except IndexError:
                    visited = []
                    break


if __name__ == "__main__":
    data = get_data(day=6, year=2024)
    data = [list(line) for line in data.splitlines()]
    print(data)
    total_steps = solve_a(data)
    print(total_steps)
    submit(total_steps, part="a", day=6, year=2024)
    solve_b()
    print(loops)
    # submit(total_loops, part="b", day=6, year=2024)
