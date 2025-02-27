from aocd import get_data, submit


def parse_to_graph(data):
    graph = {}
    rows, cols = len(data), len(data[0])
    for line_number, line in enumerate(data):
        for position, char in enumerate(line):
            graph[(line_number, position)] = char
    return graph, rows, cols


def get_neighbors(node, rows, cols):
    row, col = node
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]
    return [
        (row + dr, col + dc)
        for dr, dc in directions
        if 0 <= row + dr < rows and 0 <= col + dc < cols
    ]


def find_trail_unique(
    graph, start, end, visited, current_trail, rows, cols, nine_positions
):
    if graph[start] == end:
        if graph[start] == "9":
            nine_positions.add(start)
        return [current_trail + [start]], nine_positions

    trails = []
    for neighbor in get_neighbors(start, rows, cols):
        if neighbor not in visited and graph[neighbor] == chr(ord(graph[start]) + 1):
            trails.extend(
                find_trail_unique(
                    graph,
                    neighbor,
                    end,
                    visited | {neighbor},
                    current_trail + [neighbor],
                    rows,
                    cols,
                    nine_positions,
                )
            )
    return trails, nine_positions


def find_trail(graph, start, end, visited, current_trail, rows, cols):
    if graph[start] == end:
        return [current_trail + [start]]

    trails = []
    for neighbor in get_neighbors(start, rows, cols):
        if neighbor not in visited and graph[neighbor] == chr(ord(graph[start]) + 1):
            trails.extend(
                find_trail(
                    graph,
                    neighbor,
                    end,
                    visited | {neighbor},  # Add neighbor to visited
                    current_trail + [neighbor],
                    rows,
                    cols,
                )
            )
    return trails


def calculate_trails_a(data):
    graph, rows, cols = parse_to_graph(data)
    all_trails = 0
    for node, char in graph.items():
        if char == "0":
            _, nine_positions = find_trail_unique(
                graph, node, "9", {node}, [node], rows, cols, set()
            )
            all_trails += len(nine_positions)
    return all_trails


def calculate_trails_b(data):
    graph, rows, cols = parse_to_graph(data)
    total_trails = 0
    for node, char in graph.items():
        if char == "0":
            trails = find_trail(graph, node, "9", {node}, [node], rows, cols)
            total_trails += len(trails)
    return total_trails


def solve_a(data):
    total = calculate_trails_a(data)
    return total


def solve_b(data):
    total = calculate_trails_b(data)
    return total


if __name__ == "__main__":
    data = get_data(day=10, year=2024).splitlines()
    result = solve_a(data)
    print(result)
    submit(result, part="a", day=10, year=2024)
    result = solve_b(data)
    print(result)
    submit(result, part="b", day=10, year=2024)
