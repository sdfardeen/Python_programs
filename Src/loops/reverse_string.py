res = ""
input_data = "First program"
for i in range(len(input_data)-1,-1,-1):
    res = res + input_data[i]
print(res)

print("###")

# method using temp
num = "first program"
res = ""
temp = -1
for i in num:
    res = res + num[temp]
    temp = temp-1
print(res)
