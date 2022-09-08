import re

# print(re.findall('\d', Str))  # \d匹配任何十进制数
# print(re.findall('\D', Str))  # \D匹配任何非数字字符
# print(re.findall('\s', Str))
# print(re.findall('\w', "123sadiw你好\n!@#$%^^&*【"))

# Str = "a1c a2c a3c abc abdc"
# print(re.findall('a1c', Str))
# print(re.findall('a.c', Str))
# print(re.findall('a..c', Str))
# print(re.findall('a.*?c', Str))
# print(re.findall('a.*c', Str))
#
# Str = "0test4\n\tji1awda6dn7iq10"
# print(re.findall('\d', Str))
# print(re.findall('\d*', Str))
# print(re.findall('\d+', Str))

# Str = "ac abc abbc abbbc a!c adddc"
#
# print(re.findall('a.{1,2}c', Str))
# print(re.findall('a[abc]c', Str))  # 匹配ac之间有a，b，c字符的字符串，这些字符只能出现一个
# print(re.findall('a[abc][b]c', Str))

# Str = "abcde1234"
# print(re.match('dc', Str))
# print(re.match('ab', Str))
# data = re.match('ab', Str)
# print(data.span())
# print(data.group())
#
# print(re.findall('bc', Str))


Str = '<meta charset= "UTF-8">'

print(re.findall('<meta charset= ".*">', Str))
print(re.findall('<meta charset= "(.*)">', Str))
