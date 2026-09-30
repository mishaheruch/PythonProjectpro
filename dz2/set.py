def set_ob(set1, set2):
    return set1 | set2

print(set_ob({1, 2}, {3}))

def set_pid(set1, set2):
    return set1.issubset(set2)

print(set_pid({1, 2}, {1, 2, 3}))