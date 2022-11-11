nu = list(str(14300))

nu.sort(reverse=True)

print(nu)

res = 0

for i in nu:

    res = res * 10 + int(i)

print(res)
