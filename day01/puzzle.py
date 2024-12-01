from collections import Counter

def get_data(filename: str) -> tuple[list[int],list[int]]:
    with open(filename, 'r') as fin:
        dat = fin.readlines()
    list1: list[int] = []
    list2: list[int] = []
    for line in dat:
        a,b = line.split("   ")
        list1.append(int(a))
        list2.append(int(b))
    return (list1,list2)


list1,list2 = get_data("input.txt")
list1.sort()
list2.sort()
list_diff = 0
list_freqs = 0
list2_counts = Counter(list2)
for i in range(len(list1)):
    list_diff += abs(list2[i] - list1[i])
    list_freqs += list1[i] * list2_counts[list1[i]]
print(f"Part 1: {list_diff}")
print(f"Part 2: {list_freqs}")
