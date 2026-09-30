def sum_list():
    list_num = [5,4,6]
    return sum(list_num) // len(list_num)
print(sum_list())

def list2(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

print(list2([1, 2, 2, 3, 4], [2, 4, 6]))