OppPlay: list = []
YouPlay: list = []

def process() -> None:
    with open("day2_input.txt", "r+") as strat:
        line: str = strat.readline()
        while True:
            if not line:
                break
            tokens: list = line.split(" ")
            OppPlay.append(tokens[0].rstrip())
            YouPlay.append(tokens[1].rstrip())
            line = strat.readline()

def calculate_score(o: list, y: list) -> int:
    total_score: int = 0
    for i in range(len(o)): # I pray every night for switch statements in python
        if o[i] == 'A':
            if y[i] == 'X': # Rock V Rock
                total_score += 4
            elif y[i] == 'Y': # Rock V Paper
                total_score += 8
            else: # Rock V Scissors
                total_score += 3
        elif o[i] == 'B':
            if y[i] == 'X': # Paper V Rock
                total_score += 1
            elif y[i] == 'Y': # Paper V Paper
                total_score += 5
            else: # Paper V Scissors
                total_score += 9
        elif o[i] == 'C':
            if y[i] == 'X': # Scissor V Rock
                total_score += 7
            elif y[i] == 'Y': # Scissor V Paper
                total_score += 2
            else: # Scissor V Scissors
                total_score += 6
    return total_score

def calculate_strat(o: list, y: list) -> int:
    total_score: int = 0
    for i in range(len(o)):
        if y[i] == 'Z': # Have to win, +6
            if o[i] == 'A': # They play rock
                # We play paper, +2
                total_score += 8
            elif o[i] == 'B': # They play paper
                # We play scissor, +3
                total_score += 9
            else: # They play scissor
                # We play rock, +1
                total_score += 7
        elif y[i] == 'Y': # Have to draw, +3
            if o[i] == 'A': # They play rock
                # We play rock, +1
                total_score += 4
            elif o[i] == 'B': # They play paper
                # We play paper, +2
                total_score += 5
            else: # They play scissor
                # We play scissor, +3
                total_score += 6
        else: # We have to lose, +0
            if o[i] == 'A': # They play rock
                # We play scissor, +3
                total_score += 3
            elif o[i] == 'B': # They play paper
                # We play rock, +1
                total_score += 1
            else: # They play scissor
                # We play paper, +2
                total_score += 2
    return total_score

if __name__ == '__main__':
    process()
    t: int = calculate_score(OppPlay, YouPlay)
    v: int = calculate_strat(OppPlay, YouPlay)
    print(t)
    print(v)