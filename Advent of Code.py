def day1_1(filename):
    file = open(filename, 'r')
    lines = file.read().splitlines()
    res = 0
    digit = []
    for l in lines:
        digit = []
        for c in l:
            if '0' <= c <= '9':
                digit.append(int(c))
        toadd = digit[0] * 10 + digit[-1]
        res += toadd
    return res

# print(day1_1("test.txt"))
# print(day1_1("input.txt"))

def day1_2(filename):
    file = open(filename, 'r')
    lines = file.read().splitlines()
    res = 0
    for l in lines:
        digit = []
        size = len(l)
        for i in range(size):
            if '0' <= l[i] <= '9':
                digit.append(int(l[i]))
            elif l[i] == 'o':
                if i+2 < size and l[i+1] == 'n' and l[i+2] == 'e':
                    digit.append(1)
                    i += 2
            elif l[i] == 't':
                if i+2 < size and l[i+1] == 'w' and l[i+2] == 'o':
                    digit.append(2)
                    i += 2
                elif i+4 < size and l[i+1] == 'h' and l[i+2] == 'r' and l[i+3] == 'e' and l[i+4] == 'e':
                    digit.append(3)
                    i += 4
            elif l[i] == 'f':
                if i + 3 < size and l[i + 1] == 'o' and l[i + 2] == 'u' and l[i + 3] == 'r':
                    digit.append(4)
                    i += 3
                elif i + 3 < size and l[i + 1] == 'i' and l[i + 2] == 'v' and l[i + 3] == 'e':
                    digit.append(5)
                    i += 3
            elif l[i] == 's':
                if i + 2 < size and l[i + 1] == 'i' and l[i + 2] == 'x':
                    digit.append(6)
                    i += 2
                if i + 4 < size and l[i+1] == 'e' and l[i+2] == 'v' and l[i+3] == 'e' and l[i+4] == 'n':
                    digit.append(7)
                    i += 4
            elif l[i] == 'e' and i+4 < size and l[i+1] == 'i' and l[i+2] == 'g' and l[i+3] == 'h' and l[i+4] == 't':
                digit.append(8)
                i += 4
            elif l[i] == 'n' and i + 3 < size and l[i + 1] == 'i' and l[i + 2] == 'n' and l[i + 3] == 'e':
                digit.append(9)
                i += 3
        toadd = digit[0] * 10 + digit[-1]
        res += toadd
    return res

# print(day1_2("test.txt"))
# print(day1_2("input.txt"))

def day2_1(filename):
    file = open(filename, 'r')
    lines = file.read().splitlines()
    id = 1
    res = 0
    for l in lines:
        size = len(l)
        i = 0
        add = True
        while i < size:
            if l[i] == 'r':
                if '0' <= l[i-3] <= '9':
                    num = l[i-3] + l[i-2]
                    toadd = int(num)
                else:
                    toadd = int(l[i - 2])
                if toadd > 12:
                    add = False
                i += 2
            elif l[i] == 'g':
                if '0' <= l[i-3] <= '9':
                    num = l[i - 3] + l[i - 2]
                    toadd = int(num)
                else:
                    toadd = int(l[i - 2])
                if toadd > 13:
                    add = False
                i += 4
            elif l[i] == 'b':
                if '0' <= l[i-3] <= '9':
                    num = l[i - 3] + l[i - 2]
                    toadd = int(num)
                else:
                    toadd = int(l[i - 2])
                if toadd > 14:
                    add = False
                i += 3
            i += 1
        if add:
            res += id
        id += 1
    return res

# print(day2_1("test.txt"))
# print(day2_1("input.txt"))

def day2_2(filename):
    file = open(filename, 'r')
    lines = file.read().splitlines()
    id = 1
    res = 0
    for l in lines:
        size = len(l)
        i = 0
        rgb = [0,0,0]
        while i < size:
            if l[i] == 'r':
                if '0' <= l[i-3] <= '9':
                    num = l[i-3] + l[i-2]
                    toadd = int(num)
                else:
                    toadd = int(l[i - 2])
                if toadd > rgb[0]:
                    rgb[0] = toadd
                i += 2
            elif l[i] == 'g':
                if '0' <= l[i-3] <= '9':
                    num = l[i - 3] + l[i - 2]
                    toadd = int(num)
                else:
                    toadd = int(l[i - 2])
                if toadd > rgb[1]:
                    rgb[1] = toadd
                i += 4
            elif l[i] == 'b':
                if '0' <= l[i-3] <= '9':
                    num = l[i - 3] + l[i - 2]
                    toadd = int(num)
                else:
                    toadd = int(l[i - 2])
                if toadd > rgb[2]:
                    rgb[2] = toadd
                i += 3
            i += 1
        res += rgb[0] * rgb[1] * rgb[2]
        id += 1
    return res

# print(day2_2("test.txt"))
# print(day2_2("input.txt"))

def got_symbol(symbols, i, j, size_file, size_line):
    if j - 1 >= 0:
        if i-1 >= 0:
            if symbols[i-1][j-1] or symbols[i-1][j]:
                return True
        if i+1 < size_file:
            if symbols[i+1][j - 1] or symbols[i+1][j]:
                return True
        if symbols[i][j - 1]:
            return True
    if j + 1 < size_line:
        if i - 1 >= 0:
            if symbols[i - 1][j+1]:
                return True
        if i + 1 < size_file:
            if symbols[i + 1][j+1]:
                return True
        if symbols[i][j +1]:
            return True
    return False
def day3_1(filename):
    file = open(filename, 'r')
    lines = file.read().splitlines()
    size_file = len(lines)
    size_line = len(lines[0])
    symbols = []
    res = 0
    for i in range(size_file):
        symbols.append([])
        for j in range(size_line):
            if ('0' > lines[i][j] or lines[i][j] > '9') and lines[i][j] != '.':
                symbols[i].append(True)
            else:
                symbols[i].append(False)

    for i in range(size_file):
        j = 0
        while j < size_line:
            if '0' <= lines[i][j] <= '9':
                if j+1 < size_line and '0' <= lines[i][j+1] <= '9':
                    if j + 2 < size_line and '0' <= lines[i][j + 2] <= '9':
                        if got_symbol(symbols, i, j, size_file, size_line) or got_symbol(symbols, i, j+1, size_file, size_line) or got_symbol(symbols, i, j+2, size_file, size_line):
                            num = int(lines[i][j] + lines[i][j+1] + lines[i][j + 2])
                            res += num
                        j += 3
                    else:
                        if got_symbol(symbols, i, j, size_file, size_line) or got_symbol(symbols, i, j+1, size_file, size_line):
                            num = int(lines[i][j] + lines[i][j + 1])
                            res += num
                        j += 2
                else:
                    if got_symbol(symbols, i, j, size_file, size_line):
                        num = int(lines[i][j])
                        res += num
                    j += 1
            else:
                j += 1

    return res


# print(day3_1("test.txt"))
# print(day3_1("input.txt"))

def got_num(lines, i, j, size_file, size_line):
    stock = []
    maxi = i+3
    maxj = j+3
    if i < 0:
        i = 0
    if j < 0:
        j = 0
    if maxi > size_file:
        maxi = size_line
    if maxj > size_line:
        maxj = size_line
    ind = -1
    go = False
    for a in range(i, maxi):
        ind += 1
        for b in range(j, maxj):
            if '0' <= lines[a][b] <= '9':
                debug = lines[a][b]
                num = 0
                for c in range(b-2, b+3):
                    if c < 0:
                        c = 0
                    elif c >= size_line:
                        break
                    elif c+2 < b+3 and lines[a][c+1] == '.' and '0' <= lines[a][c+2] <= '9':
                        continue
                    else:
                        if '0' <= lines[a][c] <= '9':
                            go = True
                            num += int(lines[a][c])
                            num *= 10
                if not stock:
                    stock.append(num // 10)
                elif len(stock) == 1 and num//10 != stock[0]:
                    stock.append(num//10)
    print(stock)
    return stock


def day3_2(filename):
    # Not Working !
    file = open(filename, 'r')
    lines = file.read().splitlines()
    size_file = len(lines)
    size_line = len(lines[0])
    res = 0
    for i in range(size_file):
        j = 0
        while j < size_line:
            if lines[i][j] == '*':
                stock = got_num(lines, i-1, j-1, size_file, size_line)
                if len(stock) == 2:
                    res += stock[0] * stock[1]
            j += 1
    return res

# print(day3_2("test.txt"))
# print(day3_2("input.txt"))
