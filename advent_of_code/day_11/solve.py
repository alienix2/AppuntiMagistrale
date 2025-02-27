from aocd import get_data, submit

if __name__ == "__main__":
    data = get_data(day=11).split(" ")
    data = "0 1 10 99 999".split(" ")
    print(data)
    print(solve_a(data))
    # submit(1, part="a", day=11)
    # submit(2, part="b", day=11)
