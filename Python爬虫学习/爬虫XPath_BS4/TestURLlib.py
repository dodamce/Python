import urllib.request

url = 'https://www.baidu.com/'

response = urllib.request.urlopen(url)

data = response.read()  # 二进制数据，写入时使用二进制写入
print(type(data))

file = open('baidu.html', 'wb')
file.write(data)
file.close()

print(data)

# print(response.read().decode('utf-8'))
#
# print(type(response))
