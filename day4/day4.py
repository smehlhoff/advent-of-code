from collections import Counter

puzzle_input = "240298-784956"

start, end = [int(x) for x in puzzle_input.split("-")]


nums = set()
index = 0

while index != 5:
    for x in range(start, end):
        y = list(str(x))

        if y[index] == y[index + 1]:
            nums.add(x)

    index += 1

results = set()

for x in nums:
    y = list(str(x))

    if y[0] <= y[1] <= y[2] <= y[3] <= y[4] <= y[5]:
        results.add(x)

print("Part 1:", len(results))

results2 = set()

for x in results:
    y = list(str(x))
    c = Counter(y)

    if 2 in c.values():
        results2.add(x)


print("Part 2:", len(results2))
