from numpy import number

siz = 4
numb = ['L', 'D', 'D', ' L']
count = 0

for each in range(siz):

    if numb[each] == 'D':

        numb[each] = 'L'

        if each + 2 <= siz:
            numb[each + 1], numb[each + 2] = numb[each + 2], numb[each + 1]

        count += 1

print(count)

# FIZZBUZZ
inp = [12, 36, 54, 60, 72]
for num in inp:
    if num % 3 == 0 and num % 5 == 0:
        print("FIZZBUZZ")
    elif num % 5 == 0:
        print("BUZZ")
    elif num % 3 == 0:
        print("FIZZ")
