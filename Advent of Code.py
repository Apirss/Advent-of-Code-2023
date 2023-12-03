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

print(day2_2("test.txt"))
print(day2_2("input.txt"))