from aocd import get_data
from aocd import submit


def distance_direction(a_x, a_y, b_x, b_y):
    if a_x - b_x == 0:
        if a_y - b_y == 1:
            return "vert_down"
        if a_y - b_y == -1:
            return "vert_up"
    if a_y - b_y == 0:
        if a_x - b_x == -1:
            return "horiz_right"
        if a_x - b_x == 1:
            return "horiz_left"
    if a_x - b_x == -1:
        if a_y - b_y == -1:
            return "diag_down_right"
        if a_y - b_y == 1:
            return "diag_up_right"
    if a_x - b_x == 1:
        if a_y - b_y == -1:
            return "diag_down_left"
        if a_y - b_y == 1:
            return "diag_up_left"
    return None


def continue_direction(a_x, a_y, b_x, b_y, direction):
    if direction == "vert_down":
        if a_x - b_x == 0 and a_y - b_y == 1:
            return True
    if direction == "vert_up":
        if a_x - b_x == 0 and a_y - b_y == -1:
            return True
    if direction == "horiz_right":
        if a_x - b_x == -1 and a_y - b_y == 0:
            return True
    if direction == "horiz_left":
        if a_x - b_x == 1 and a_y - b_y == 0:
            return True
    if direction == "diag_down_right":
        if a_x - b_x == -1 and a_y - b_y == -1:
            return True
    if direction == "diag_up_right":
        if a_x - b_x == -1 and a_y - b_y == 1:
            return True
    if direction == "diag_down_left":
        if a_x - b_x == 1 and a_y - b_y == -1:
            return True
    if direction == "diag_up_left":
        if a_x - b_x == 1 and a_y - b_y == 1:
            return True

    return False


def opposite_direction_x(direction):
    if direction == "diag_down_right":
        return "diag_down_left"
    if direction == "diag_up_right":
        return "diag_up_left"

    return None


def opposite_direction_y(direction):
    if direction == "diag_down_right":
        return "diag_up_right"
    if direction == "diag_down_left":
        return "diag_up_left"

    return None


def get_positions(data):
    x_position = []
    m_position = []
    a_position = []
    s_position = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "X":
                x_position.append((i, j))
            if data[i][j] == "M":
                m_position.append((i, j))
            if data[i][j] == "A":
                a_position.append((i, j))
            if data[i][j] == "S":
                s_position.append((i, j))

    return x_position, m_position, a_position, s_position


def calculate_xmas(data):
    x_position, m_position, a_position, s_position = get_positions(data)
    total = 0
    for x in x_position:
        for m in m_position:
            direction = distance_direction(x[0], x[1], m[0], m[1])
            if direction:
                for a in a_position:
                    keep = continue_direction(m[0], m[1], a[0], a[1], direction)
                    if keep:
                        for s in s_position:
                            keep = continue_direction(a[0], a[1], s[0], s[1], direction)
                            if keep:
                                total += 1
    return total


def calculate_mas(data):
    x_position, m_position, a_position, s_position = get_positions(data)
    total = 0
    mas = 0
    for m in m_position:
        for a in a_position:
            direction = distance_direction(m[0], m[1], a[0], a[1])
            if direction in [
                "diag_down_right",
                "diag_up_right",
                "diag_down_left",
                "diag_up_left",
            ]:
                for s in s_position:
                    keep = continue_direction(a[0], a[1], s[0], s[1], direction)
                    if keep:
                        mas += 1

                    if mas == 1:
                        keep = False
                        opposite_x = opposite_direction_x(direction)
                        opposite_y = opposite_direction_y(direction)
                        if opposite_x and data[m[0] + 2][m[1]] == "M":
                            keep = continue_direction(
                                m[0] + 2, m[1], a[0], a[1], opposite_x
                            )
                            if keep:
                                keep = continue_direction(
                                    a[0], a[1], s[0] - 2, s[1], opposite_x
                                )
                                if keep and data[s[0] - 2][s[1]] == "S":
                                    total += 1
                        if opposite_y and data[m[0]][m[1] + 2] == "M":
                            keep = continue_direction(
                                m[0], m[1] + 2, a[0], a[1], opposite_y
                            )
                            if keep and data[s[0]][s[1] - 2] == "S":
                                keep = continue_direction(
                                    a[0], a[1], s[0], s[1] - 2, opposite_y
                                )
                                if keep:
                                    total += 1

                    mas = 0
    return total


if __name__ == "__main__":
    get_data = get_data(day=4, year=2024).splitlines()
    character_data = []
    for row in get_data:
        character_data.append(list(row))
    # Part a
    total = calculate_xmas(character_data)
    print(total)
    submit(total, part="a", day=4, year=2024)
    # Part b
    total = calculate_mas(character_data)
    print(total)
    submit(total, part="b", day=4, year=2024)
