'''
[N]             [R]             [C]
[T] [J]         [S] [J]         [N]
[B] [Z]     [H] [M] [Z]         [D]
[S] [P]     [G] [L] [H] [Z]     [T]
[Q] [D]     [F] [D] [V] [L] [S] [M]
[H] [F] [V] [J] [C] [W] [P] [W] [L]
[G] [S] [H] [Z] [Z] [T] [F] [V] [H]
[R] [H] [Z] [M] [T] [M] [T] [Q] [W]
 1   2   3   4   5   6   7   8   9 
'''

stack1: list = ['N', 'T', 'B', 'S', 'Q', 'H', 'G', 'R']
stack2: list = ['J', 'Z', 'P', 'D', 'F', 'S', 'H']
stack3: list = ['V', 'H', 'Z']
stack4: list = ['H', 'G', 'F', 'J', 'Z', 'M']
stack5: list = ['R', 'S', 'M', 'L', 'D', 'C', 'Z', 'T']
stack6: list = ['J', 'Z', 'H', 'V', 'W', 'T', 'M']
stack7: list = ['Z', 'L', 'P', 'F', 'T']
stack8: list = ['S', 'W', 'V', 'Q']
stack9: list = ['C', 'N', 'D', 'T', 'M', 'L', 'H', 'W']

STACK_LOOKUP: dict = {
    1: stack1,
    2: stack2,
    3: stack3,
    4: stack4,
    5: stack5,
    6: stack6,
    7: stack7,
    8: stack8,
    9: stack9,
}

commands: list = []

def process() -> None:
    with open("day5_input.txt", "r+") as instructions:
        line: str = instructions.readline().rstrip()
        while True:
            if not line:
                break
            # Separated by spaces
            sep: list = line.split(" ")
            # The numbers are at the odd indices
            command: list = []
            # AMOUNT FROM TO
            command.append(int(sep[1]))
            command.append(int(sep[3]))
            command.append(int(sep[5]))
            commands.append(command)
            line = instructions.readline().rstrip()

def do_moves(commands: list) -> str:
    for command in commands:
        AMOUNT: int = command[0]
        FROM: int = command[1]
        TO: int = command[2]
        for i in range(AMOUNT):
            FSTACK = STACK_LOOKUP[FROM]
            TSTACK = STACK_LOOKUP[TO]
            e: str = FSTACK.pop(0)
            TSTACK.insert(0, e)
    toplayer: str = ""
    for j in range(9):
        ISTACK = STACK_LOOKUP[j+1]
        toplayer += ISTACK[0]
    return toplayer

def do_moves_multiples(commands: list) -> str:
    for command in commands:
        AMOUNT: int = command[0]
        FROM: int = command[1]
        TO: int = command[2]
        FSTACK = STACK_LOOKUP[FROM]
        TSTACK = STACK_LOOKUP[TO]
        to_move: list = []
        if AMOUNT != 1:
            to_move = FSTACK[0:AMOUNT]
            to_move.reverse()
        else:
            to_move = FSTACK[0]
        for e in to_move:
            TSTACK.insert(0, e)
        for i in range(AMOUNT):
            FSTACK.pop(0)
    toplayer: str = ""
    for j in range(9):
        ISTACK = STACK_LOOKUP[j+1]
        toplayer += ISTACK[0]
    return toplayer

if __name__ == '__main__':
    process()
    # t: str = do_moves(commands)
    v: str = do_moves_multiples(commands)
    # print(t)
    print(v)
