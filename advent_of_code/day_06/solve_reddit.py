grid = {
    x + y * 1j: e
    for y, line in enumerate(open("d06.txt").readlines())
    for x, e in enumerate(line.strip())
}
for k, v in grid.items():
    if v not in ".#":
        pos, d = k, {">": 1, "v": 1j, "<": -1, "^": -1j}[v]
        break

paths, cache, obstacles = set(), set(), set()
while pos in grid:
    paths.add(pos), cache.add((pos, d))
    if grid.get(pos + d) == "#":
        d *= 1j
    else:
        obs = pos + d
        if obs in grid and obs not in paths:
            n_pos, n_d, n_cache = pos, d * 1j, cache.copy()
            while n_pos in grid:
                n_cache.add((n_pos, n_d))
                if grid.get(n_pos + n_d) == "#" or (n_pos + n_d) == obs:
                    n_d *= 1j
                else:
                    n_pos += n_d
                if (n_pos, n_d) in n_cache:
                    obstacles.add(obs)
                    break
        pos += d

print(len(paths))
print(len(obstacles))
