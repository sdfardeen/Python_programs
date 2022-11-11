# sum of difference of sibling elements

res = 0
list_one = [20, 30, 50, 90, 100]
for i in range(len(list_one)-1):
    res = res + (list_one[i] - list_one[i+1])
print(res)

# sum in reversing order
result = 0
for i in range(len(list_one)-1, 0, -1):
    result = result + (list_one[i] - list_one[i-1])
print(result)

