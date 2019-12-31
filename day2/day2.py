import random


def intcode_calc(noun, verb):
    nums = []

    with open("inputs.txt", "r") as f:
        for line in f:
            for num in line.split(","):
                nums.append(int(num))

        nums[1] = noun
        nums[2] = verb

        index = 0

        while True:
            if nums[index] == 1:
                x = nums[index + 1]
                y = nums[index + 2]
                z = nums[index + 3]

                total = nums[x] + nums[y]

            elif nums[index] == 2:
                x = nums[index + 1]
                y = nums[index + 2]
                z = nums[index + 3]

                total = nums[x] * nums[y]

            else:
                break

            nums[z] = total
            index += 4

        return nums[0]


print("Part 1:", intcode_calc(12, 2))


while True:
    noun = random.randrange(0, 100)
    verb = random.randrange(0, 100)
    result = intcode_calc(noun, verb)

    if result == 19690720:
        print("Part 2:", 100 * noun + verb)
        break
