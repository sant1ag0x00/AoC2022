def main():
    with open("input.txt") as f:
        lines = f.readlines()
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
    print(final_list[final_list.index(max(final_list))])

main()