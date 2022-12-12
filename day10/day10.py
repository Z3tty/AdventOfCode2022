REG: int = 1
cycle: int = 0

instructions: list = []

def process() -> None:
    global instructions
    with open("day10_input.txt", "r+") as cpu:
        line: str = cpu.readline().rstrip()
        lsplit: list = line.split(" ")
        while True:
            if not line:
                break
            if lsplit[0] != 'noop':
                instructions.append(int(lsplit[1]))
            else:
                instructions.append('x')
            line = cpu.readline().rstrip()
            lsplit = line.split(" ")

def clock(instructions: list) -> int:
    global REG, cycle
    block_timer: int = 0
    after_block: int = 0
    total_strength: int = 0
    i: int = 0
    while cycle <= 220 or i < len(instructions):
        if block_timer == 0:
            instr = instructions[i]
            i += 1
            print("({}:{})[UNBLOCKED] fetched instruction {}".format(cycle, i, instr))
            if instr == 'x':
                block_timer = 0
            else:
                block_timer = 1
                after_block = instr
        else:
            block_timer -= 1
            print("({})[BLOCKED] Awaiting execution of {}".format(cycle, instr))
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            print("Cycle: {}, REG: {}".format(cycle, REG))
            total_strength += REG * cycle
        if block_timer == 0 and after_block:
            REG += after_block
            after_block = 0
    return total_strength

def renderCRT(instructions: list) -> None:
    global REG, cycle
    block_timer: int = 0
    after_block: int = 0
    CRT_Screen: list = []
    for i in range(6):
        CRT_Screen.append([])
        for _ in range(40):
            CRT_Screen[i].append('')
    row: int = 0
    column: int = 0
    i: int = 0
    while i < len(instructions):
        CRT_Screen[row][column] = '#' if column in [REG - 1, REG, REG + 1] else '.'
        column += 1
        if column >= 40:
            column = 0
            row += 1
        if block_timer == 0:
            instr = instructions[i]
            i += 1
            if instr == 'x':
                block_timer = 0
            else:
                block_timer = 1
                after_block = instr
        else:
            block_timer -= 1
        cycle += 1
        if block_timer == 0 and after_block:
            REG += after_block
            after_block = 0
    for r in CRT_Screen:
        print("".join(r))

if __name__ == '__main__':
    process()
    # t: int = clock(instructions)
    # print(t)
    renderCRT(instructions)

