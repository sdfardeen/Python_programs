siz = 4
numb = ['L', 'D', 'D',' L']
count = 0

for each in range(siz):

    if numb[each] == 'D':

        numb[each] = 'L'

        if each+2 <= siz:

            numb[each+1], numb[each+2] = numb[each+2], numb[each+1]

        count += 1

print(count)
