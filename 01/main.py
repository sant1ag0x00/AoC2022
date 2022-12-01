#function that takes the number of elves from the top as a parameter and returns the sum of their calories
def get_caloriecount(topx: int):
    with open("input.txt") as f:
        lines = f.readlines()
    calorie_sum = 0
    temp_list = []
    final_list = []
    for entry in lines:
        if entry == '\n':
            final_list.append(temp_list)
            temp_list = []
        else:
            entry.removesuffix('\n')
            temp_list.append(int(entry))
    for elf in final_list:
        final_list[final_list.index(elf)] = sum(elf)
    #print(final_list[final_list.index(max(final_list))])
    final_list.sort()
    for i in range(topx):
        calorie_sum += final_list.pop()
    print(calorie_sum)

get_caloriecount(3)