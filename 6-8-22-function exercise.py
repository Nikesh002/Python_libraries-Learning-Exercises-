# print the highest even number from the list

def highest_even(l1):
    high_even = 0
    for i in l1:
        if not i % 2:
            if i >= high_even:
                high_even = i
    return high_even


print(highest_even([10, 2, 3, 4, 8, 11]))


def highest_even1(l1):
    li = sorted(l1)
    for i in range(len(li) - 1, 0, -1):
        if not li[i] % 2:
            return li[i]
    print(" There is no even number present in the given list.")


print(highest_even1([10, 2, 3, 4, 8, 11]))
