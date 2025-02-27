from aocd import get_data, submit
import ray


def can_achieve_target(numbers, target):
    n = len(numbers)
    dp = [[set() for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i].add(numbers[i])

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for left in dp[i][k]:
                    for right in dp[k + 1][j]:
                        dp[i][j].add(left + right)
                        dp[i][j].add(left * right)
                        if target in dp[i][j]:
                            return True
    return target in dp[0][n - 1]


@ray.remote
def solve_line(line):
    try:
        target, numbers = line.split(":")
        numbers = list(map(int, numbers.split()))
        target = int(target)
        if can_achieve_target(numbers, target):
            return target
        else:
            return 0
    except Exception as e:
        return 0


def solve_a_ray(data):
    futures = [solve_line.remote(line) for line in data]
    results = ray.get(futures)
    return sum(results)


if __name__ == "__main__":
    data = get_data(day=7, year=2024).splitlines()
    ray.init()
    result_a = solve_a_ray(data)
