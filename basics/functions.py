def highest_even(li):
    li2 = []
    for item in li:
        if item % 2 == 0:
            li2.append(item)
    return max(li2)
print(highest_even([10,2,3,4,8,11]))

