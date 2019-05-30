# 读取文件判断数量大小

count = 0
with open('C:\\Users\\tao.dai.BWH\\Downloads\\户.txt', 'r') as f:
    for index, line in enumerate(f):
        count += 1
print(count)
