compartmentOne: list = []
compartmentTwo: list = []

def process() -> None:
    with open("day3_input.txt", "r+") as rucksacks:
        line: str = rucksacks.readline().rstrip()
        while True:
            if not line:
                break
            first: str = ""
            second: str = ""
            n: int = len(line)
            first = line[0 : n // 2]
            second = line[n // 2:] if n % 2 == 0 else line[n //2 +1:]
            compartmentOne.append(first)
            compartmentTwo.append(second)
            line = rucksacks.readline().rstrip()

def priority_sum(e: list) -> int:
    sum: int = 0
    for char in e:
        asc: int = ord(char)
        if asc >= 97 and asc <= 122:
            asc -= 96 # So that lower case characters have a priority from 1->26
        elif asc >= 65 and asc <= 90:
            asc -= 38 # So that upper case characters have a priority from 27->52
        else:
            print("Incorrect ascii\n")
        sum += asc
    return sum

def calculate(f: list, s: list) -> int:
    common: list = []
    filter: list = []
    for i in range(len(f)):
        for char in f[i]:
            if char in s[i] and char not in filter:
                # print("{} from {} in {}\n".format(char, f[i], s[i]))
                common.append(char)
                filter.append(char) # Remove dupes
        filter = []
    return priority_sum(common)

def calculate_badge(f: list, s: list) -> int:
    badges: list = []
    i: int = 0
    while i <= (len(f) - 3):
        sack_0: str = f[i] + s[i]
        sack_1: str = f[i+1] + s[i+1]
        sack_2: str = f[i+2] + s[i+2]
        for char in sack_0:
            if char in sack_1:
                if char in sack_2:
                    print("{} is in all three, added to list".format(char))
                    badges.append(char)
                    break
        i += 3
    print("Found {} badges".format(len(badges)))
    return priority_sum(badges)



if __name__ == '__main__':
    process()
    t: int = calculate(compartmentOne, compartmentTwo)
    v: int = calculate_badge(compartmentOne, compartmentTwo)
    print(t)
    print(v)