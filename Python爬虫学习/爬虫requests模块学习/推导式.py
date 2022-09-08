# 列表推导式:[结果 for 变量 in 可迭代对象]

# lists = [i for i in range(1, 10)]
# print(lists)
#
# lists = ["Python%s" % i for i in range(1, 10)]
# print(list)

# 筛选模式推导式
# lists = [i for i in range(100) if i % 2 == 0]
# print(lists)

# names = [["Tom", "Billy", "Jefferson", "Andrew", "Wesley", "Steven", ".Joe"],
#          ["Alice", "Jill", "Ana", "Wendy", "Jennifer", "Sherry", "Eva"]]

# def Count(string):
#     flag = 0
#     for ch in string:
#         if ch == 'e' or ch == 'E':
#             flag += 1
#     if flag == 2:
#         return True
#     else:
#         return False
#
#
# ret = []
# for array in names:
#     for name in array:
#         if Count(name):
#             ret.append(name)
#
# print(ret)

# 推导式
# gen = [name for array in names for name in array if name.count("e") == 2]
# print(gen)

# 字典推导式
names = ["Tom", "Billy", "Jefferson", "Andrew", "Wesley", "Steven", "Joe"]
numbers = [1, 2, 3, 4, 5, 6, 7]
dit = {names[i]: numbers[i] for i in range(len(names))}
print(dit)

