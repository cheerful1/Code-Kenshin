def replace_digits(s):
    result = []
    for char in s:
        if char.isdigit():
            result.append('number')
        else:
            result.append(char)
    return ''.join(result)

# 示例输入
s = input().strip()
# 处理并输出结果
print(replace_digits(s))