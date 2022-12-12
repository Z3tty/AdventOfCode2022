
buf: str = ""

def process() -> None:
    global buf
    with open("day6_input.txt", "r+") as stream:
        buf = stream.readline().rstrip()

def unique(s: str) -> bool:
    b: list = []
    for c in s:
        if c in b:
            return False
        b.append(c)
    return True


def protocol_find_start(stream: str) -> int:
    i = 0
    while i < len(stream) - 4:
        test_string: str = stream[i:i+4]
        if unique(test_string):
            return i+4
        i += 1
    return -1

def message_find_start(stream: str) -> int:
    i = 0
    while i < len(stream) - 14:
        test_string: str = stream[i:i+14]
        if (unique(test_string)):
            return i+14
        i += 1
    return -1

if __name__ == '__main__':
    process()
    t: int = protocol_find_start(buf)
    print(t)
    v: int = message_find_start(buf)
    print(v)
