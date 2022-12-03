elves: list = []

def process() -> None:
    with open("day1_input.txt", "r+") as inp:
        line: str = inp.readline()
        calories: list = []
        while True:
            if not line:
                break
            if line != "\n":
                calories.append(line)
            else:
                elves.append(calories)
                calories = []
            line = inp.readline()
        
def sum(e: list) -> list:
    summed: list = []
    for elf in e:
        partial_sum: int = 0
        for cal in elf:
            partial_sum += int(cal)
        summed.append(partial_sum)
    return summed

if __name__ == '__main__':
    process()
    t: list = sum(elves)
    t.sort()
    t.reverse()
    print(t[0])
    print(t[0] + t[1] + t[2])