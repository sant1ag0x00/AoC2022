#https://adventofcode.com/2022/day/2
#function that calculates the score in the most lazy inelegant way possible, I'm really tired
def first_part()->int:
    score = 0
    with open("input.txt") as f:
        lines = f.readlines()
    for line in lines:
        match line:
            case "A X\n":
                score += 4
            case "A Y\n":
                score += 8
            case "A Z\n":
                score += 3
            case "B X\n":
                score += 1
            case "B Y\n":
                score += 5
            case "B Z\n":
                score += 9
            case "C X\n":
                score += 7
            case "C Y\n":
                score += 2
            case "C Z\n":
                score += 6
    return score

def second_part():
    score = 0
    with open("input.txt") as f:
        lines = f.readlines()
    for line in lines:
        match line:
            case "A X\n":
                score += 3
            case "A Y\n":
                score += 4
            case "A Z\n":
                score += 8
            case "B X\n":
                score += 1
            case "B Y\n":
                score += 5
            case "B Z\n":
                score += 9
            case "C X\n":
                score += 2
            case "C Y\n":
                score += 6
            case "C Z\n":
                score += 7
    return score
    

print(first_part())
print(second_part())