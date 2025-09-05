import math
n = 6
nums = [4, 8, 7, 2, 8, 9]
total = 0
for i in nums:
    total += i

print(math.ceil(total/n)) # 小数点以下を切り上げ  
print(round(total/n))  # 四捨五入
print(math.floor(total/n))  # 小数点以下を切り捨て  
print(int(total/n))  # 小数点以下を切り捨て
print(total//n)  # 小数点以下を切り捨て
print(total/n)  # 小数点以下も表示
