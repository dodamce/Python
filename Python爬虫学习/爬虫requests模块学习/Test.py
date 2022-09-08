# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}*{j}={i * j}', end=' ')
#     print('\n')

# Str = input('输入英文字符串')
# Capital = range('A', 'Z')

# Capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Small = Capital.lower()
# Str = input('输入英文字符串')
# CountCap = {}
# CountSm = {}
# for ch in Str:
#     if Capital.find(ch) != -1:
#         if ch in CountCap:
#             CountCap[ch] += 1
#         else:
#             CountCap[ch] = 1
#     elif Small.find(ch) != -1:
#         if ch in CountSm:
#             CountSm[ch] += 1
#         else:
#             CountSm[ch] = 1
# if CountSm or CountCap:
#     if CountSm:
#         for num in CountSm:
#             print(num + ':' + str(CountSm[num]), end=' ')
#     if CountCap:
#         for num in CountCap:
#             print(num + ':' + str(CountCap[num]), end=' ')
# else:
#     print('字符串中没有字母')

"""
1，1，2，3，5，8，13，21，34，55，89，144，233，377，610，987，1597，2584
"""
begin = 1
end = 1
sum = 1
time = int(input('输入计算几阶斐波那契数列'))
if time <= 2:
    print('1')
else:
    while time > 2:
        sum = begin + end
        begin = end
        end = sum
        time -= 1
    print(sum)
