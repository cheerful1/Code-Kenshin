#获取输入的数字k和字符串
k = int(input())
s = input()#通过切片反转第一段和第二段字符串#注意：python中字符串是不可变的，所以也需要额外空间
s = s[len(s)-k:] + s[:len(s)-k]print(s)