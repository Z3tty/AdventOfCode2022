directories: dict = {'/' : 0}

def process() -> None:
    with open("day7_input.txt", "r+") as terminal:
        line: str = terminal.readline().rstrip()
        lsplit: list = line.split(" ")
        current_directory: str = ''
        current_path: str = ''
        while True:
            if not line:
                break
            if lsplit[0] == '$': # Command
                # 0 contains the $, 1 contains the command, 2 contains the dir in the case of a cd
                # The terminal only utilizes cd and ls
                if lsplit[1] == 'cd':
                    if lsplit[2] != '..':
                        current_directory = lsplit[2]
                        current_path += ('-' + current_directory) if current_path != '' else current_directory
                    else:
                        path: list = current_path.split('-')
                        temp: str = "/"
                        i: int = 1
                        while i < len(path) - 1:
                            # print("TEMP: " + temp)
                            # print("CUR DIR: " + path[i])
                            temp += '-' + path[i]
                            i += 1
                        current_directory = path[len(path) -2]
                        current_path = temp
                elif lsplit[1] == 'ls':
                    # If we've listed the contents of a directory, then go through those contents
                    pass
            elif lsplit[0] == 'dir': # No need to do anything here
                pass
            else: # It is a file
                path = current_path.split('-')
                for d in path:
                    if d in directories.keys():
                        directories[d] += int(lsplit[0]) # Add the size to all previous dirs aswell
                    else:
                        directories[d] = int(lsplit[0])
            print(line)
            line = terminal.readline().rstrip()
            lsplit = line.split(" ")


def total_size(dirs: dict, size_limit: int) -> int:
    total: int = 0
    for d in dirs.keys():
        if dirs[d] <= size_limit:
            total += dirs[d]
    return total

if __name__ == '__main__':
    process()
    t: int = total_size(directories, 100000)
    print(t)

