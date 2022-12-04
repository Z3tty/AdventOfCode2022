
assignment_pairs: list = []

def process() -> None:
    with open("day4_input.txt", "r+") as pairs:
        line: str = pairs.readline().rstrip()
        while True:
            if not line:
                break
            sep: list = line.split(",")
            assignment_pairs.append(sep)
            line = pairs.readline().rstrip()

def overlap_completely_count(pairs: list) -> int:
    overlaps: int = 0
    for i in range(len(pairs)):
        current_pair: list = pairs[i]
        f: str = current_pair[0]
        s: str = current_pair[1]
        fSplit: list = f.split("-")
        sSplit: list = s.split("-")
        fStart: int = int(fSplit[0])
        fEnd: int = int(fSplit[1])
        sStart: int = int(sSplit[0])
        sEnd: int = int(sSplit[1])
        if (fStart <= sStart and fEnd >= sEnd) or (sStart <= fStart and sEnd >= fEnd):
            overlaps += 1
    return overlaps

def overlap_atall_count(pairs: list) -> int:
    overlaps: int = 0
    for i in range(len(pairs)):
        current_pair: list = pairs[i]
        f: str = current_pair[0]
        s: str = current_pair[1]
        fSplit: list = f.split("-")
        sSplit: list = s.split("-")
        fStart: int = int(fSplit[0])
        fEnd: int = int(fSplit[1])
        sStart: int = int(sSplit[0])
        sEnd: int = int(sSplit[1])
        fR = range(fStart, fEnd +1)
        sR = range(sStart, sEnd +1)
        if (fStart in sR or sStart in fR or fEnd in sR or sEnd in fR):
            overlaps += 1
    return overlaps

if __name__ == '__main__':
    process()
    t: int = overlap_completely_count(assignment_pairs)
    v: int = overlap_atall_count(assignment_pairs)
    print(t)
    print(v)