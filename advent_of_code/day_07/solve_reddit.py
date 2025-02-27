from collections import defaultdict
from aocd import get_data, submit


def op1(a, b):
    return a + b


def op2(a, b):
    return a * b


def op3(a, b):
    return int(str(a) + str(b))


def solve_equation(equation, target, operations):
    allResults = defaultdict(set)

    allResults[0] = {equation[0]}

    for i in range(1, len(equation)):
        possibleResults = set()
        for prevResult in allResults[i - 1]:
            for op in operations:
                result = op(prevResult, equation[i])

                if result <= target:
                    possibleResults.add(result)

        if len(possibleResults) == 0:
            break
        allResults[i] = possibleResults

    return target in allResults[len(equation) - 1]


def solve_a(data):
    operations = [op1, op2]
    result = 0
    for line in data:
        target, numbers = line.split(":")
        target = int(target)
        numbers = list(map(int, numbers.split()))
        if solve_equation(numbers, target, operations):
            result += target
    return result


def solve_b(data):
    operations = [op1, op2, op3]
    result = 0
    for line in data:
        target, numbers = line.split(":")
        target = int(target)
        numbers = list(map(int, numbers.split()))
        if solve_equation(numbers, target, operations):
            result += target
    return result


if __name__ == "__main__":
    operations = [op1, op2]
    result = 0
    data = get_data(day=7, year=2024).splitlines()

    result = solve_a(data)
    submit(result, day=7, year=2024, part="a")
    result = solve_b(data)
    submit(result, day=7, year=2024, part="b")
