def is_even(num):
    return 'Парне' if num % 2 == 0 else 'Непарне'
print(is_even(3))
print(is_even(4))
print(is_even(5))

def num_list(lst):
    num_list = []
    for num in lst:
        if num % 2 == 0:
            num_list.append(num)
    return  num_list
print(num_list([1, 2, 3, 4]))