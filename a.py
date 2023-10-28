import subprocess  
import fileinput  
import re  
  
# 获取用户输入的字符串  
user_input = input("请输入不带引号的字符串：")  
  
# 打开文件并读取内容  
with open('wgcf-account.toml', 'r') as file:  
    content = file.read()  
  
# 使用正则表达式匹配带引号的随机字符串并进行替换  
pattern = r"license_key = '[^']*'"  
replacement = f"license_key = '{user_input}'"  
content = re.sub(pattern, replacement, content)  
  
# 写回文件  
with open('wgcf-account.toml', 'w') as file:  
    file.write(content)