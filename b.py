import subprocess  
import fileinput  
# 获取用户输入的网址  

url = input("enjoy additional ranges:2606:4700:d0::a29f:c001 -10，162.159.193.1 -162.159.193.10，162.159.192.1 to 162.159.192.10 and 2606:4700:d0::a29f:c001 to 2606:4700:d0::a29f:c010")  

  

# 打开文件进行替换  

with fileinput.FileInput('wgcf-profile.conf', inplace=True, backup='.bak') as file:  

    for line in file:  

        # 用用户输入的网址替换

        print(line.replace('engage.cloudflareclient.com', url), end='')