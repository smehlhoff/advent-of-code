from math import floor


def calc_fuel(mass):
    return floor((mass / 3) - 2)


with open("inputs.txt", "r") as f:
    total_fuel = [calc_fuel(int(x)) for x in f]
    print("Part 1:", sum(total_fuel))

total_fuel = []


def calc_fuel_recursive(mass):
    x = calc_fuel(mass)

    if x > 0:
        total_fuel.append(x)
        return calc_fuel_recursive(x)
    else:
        return


with open("inputs.txt", "r") as f:
    for x in f:
        calc_fuel_recursive(int(x))
    print("Part 2:", sum(total_fuel))
