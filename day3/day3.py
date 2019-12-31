data1, data2 = [f.split(",") for f in open("inputs.txt")]


class Wire():
    def __init__(self, x, y, points):
        self.x = x
        self.y = y
        self.points = points


wire1 = Wire(0, 0, set())
wire2 = Wire(0, 0, set())


def step(wire, data):
    for val in data:
        if val[0] == "R":
            for num in range(int(val[1:]) + 1):
                wire.points.add((wire.x + num, wire.y))
            wire.x = wire.x + int(val[1:])

        elif val[0] == "L":
            for num in range(int(val[1:]) + 1):
                wire.points.add((wire.x - num, wire.y))
            wire.x = wire.x - int(val[1:])

        elif val[0] == "U":
            for num in range(int(val[1:]) + 1):
                wire.points.add((wire.x, wire.y + num))
            wire.y = wire.y + int(val[1:])

        elif val[0] == "D":
            for num in range(int(val[1:]) + 1):
                wire.points.add((wire.x, wire.y - num))
            wire.y = wire.y - int(val[1:])


step(wire1, data1)
step(wire2, data2)

results = []

pairs = wire1.points & wire2.points

for point in pairs:
    a, b = point
    if a != 0 and b != 0:
        distance = abs(a - 0) + abs(b - 0)
        results.append(distance)


print("Part 1:", min(results))
