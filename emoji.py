# print("\N{sauropod}")
# print("\N{cat}")
# print("\N{dog}")

# lst = [3, 2, 5, 7, 5]
# for i, x in enumerate(lst):
#     print(i, x)

# def sum_two(nums):
#     lst = dict()
#     for i, x in enumerate(nums):
#         #print(i, x)
#         pass
#     for i, x in enumerate(nums):
#         lst[x] = i
#         print(lst)

# d = [3, 2, 5, 3, 4]
# sum_two(d)

def sum_two(nums, target):
    lst = dict()
    for i, x in enumerate(nums):
        lst[x] = i
        #print(lst)
        return lst

    for i, x in enumerate(nums):
        if (target - x) in lst:
            return(i, lst[target-x])
    return []


d = [1, 2, 3, 4, 5]
t = 9
sum_two(d, t)
