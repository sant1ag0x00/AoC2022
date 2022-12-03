import string

def first_part()->int:
    priority_sum = 0
    with open("input.txt") as f:
        lines = f.readlines()
    for line in lines:
        priority = 0
        line.removesuffix("\n")
        first_half = slice(0,len(line)//2)
        second_half = slice(len(line)//2,len(line))
        for char1 in line[first_half]:
            for char2 in line[second_half]:
                if char1 == char2:
                    if char1.isupper(): priority += 26
                    char1.lower()
                    priority += ord(char1) - 96
        priority_sum += priority
    return priority_sum


print(string.ascii_lowercase.index('a'))
print(first_part())
print(ord('b') - 96)