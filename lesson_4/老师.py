import re
content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))#输出字符串的长度
result = re.match('^He.*?(\d+).*Demo$', content,re.S)
print(result)
print(result.group(1))
