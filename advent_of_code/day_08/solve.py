from aocd import get_data, submit
from decimal import Decimal


def spawn_at_colinearity(a, b, grid):
    delta_x = b[0] - a[0]
    delta_y = b[1] - a[1]

    forward_x = b[0] + delta_x
    forward_y = b[1] + delta_y
    if 0 <= forward_x < len(grid) and 0 <= forward_y < len(grid[0]):
        grid[forward_x][forward_y] = "#"

    backward_x = a[0] - delta_x
    backward_y = a[1] - delta_y
    if 0 <= backward_x < len(grid) and 0 <= backward_y < len(grid[0]):
        grid[backward_x][backward_y] = "#"


def calculate_line_coefficient(a, b):
    delta_x = b[0] - a[0]
    delta_y = b[1] - a[1]
    if delta_x == 0:
        return None
    return delta_y / delta_x


def generate_line_points(a, b, original_grid, final_grid):
    x1, y1 = a

    m = Decimal(calculate_line_coefficient(a, b))
    if m is not None:
        c = Decimal(y1) - m * Decimal(x1)
    else:
        c = None

    if m is None:
        for y in range(len(original_grid[0])):
            if 0 <= x1 < len(original_grid):
                final_grid[x1][y] = "#"
    else:
        for x in range(len(original_grid)):
            expected_y = Decimal(m * x + c)

            if abs(expected_y - round(expected_y)) < 1e-10:  # Precision threshold
                y_int = int(round(expected_y))
                if 0 <= x < len(original_grid) and 0 <= y_int < len(original_grid[0]):
                    final_grid[x][y_int] = "#"


def find_couples(grid):
    positions = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            char = grid[row][col]
            if char.isalnum():
                if char not in positions:
                    positions[char] = []
                positions[char].append((row, col))

    for char, char_positions in positions.items():
        for i in range(len(char_positions)):
            for j in range(i + 1, len(char_positions)):
                spawn_at_colinearity(char_positions[i], char_positions[j], grid)


def draw_lines(grid, final_grid):
    positions = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            char = grid[row][col]
            if char.isalnum():
                if char not in positions:
                    positions[char] = []
                positions[char].append((row, col))

    for char, char_positions in positions.items():
        for i in range(len(char_positions)):
            for j in range(i + 1, len(char_positions)):
                generate_line_points(
                    char_positions[i], char_positions[j], grid, final_grid
                )
    print(final_grid)


def count_antennas(grid):
    antennas = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                antennas += 1
    return antennas


def solve_a(data):
    grid = [list(row) for row in data.splitlines()]
    find_couples(grid)
    return count_antennas(grid)


def solve_b(data):
    grid = [list(row) for row in data.splitlines()]
    final_grid = grid.copy()
    draw_lines(grid, final_grid)
    for elem in final_grid:
        print(elem)
        print("\n")
    return count_antennas(final_grid)


if __name__ == "__main__":
    data = get_data(day=8, year=2024)
    result = solve_a(data)
    print(result)
    submit(result, day=8, year=2024, part="a")
    result = solve_b(data)
    print(result)
    submit(result, day=8, year=2024, part="b")
