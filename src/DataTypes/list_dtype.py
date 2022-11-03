def list_functions():
    list1 = [1, 2, 3, 4]
    list2 = [34, 54, 65, 76]
    list3 = ['hi', 'hlo', 'im']

    list1.append(5)
    print(list1)

    list2.sort()
    print(list2)
    list2.sort(reverse=True)
    print("Li:", list2)

    print("g:", list2.count(34))

    print("pop:", list2.pop(0))
    print(list2)

    list3.reverse()
    print(list3)

    list3.insert(2, 32)
    print(list3)

    print(list2.count(2))



list_functions()

li = [12,23,34,45,56,67,78,89,90]
li.append(100)
print("appending 100 into li, li=",li)

print("counting that howmany tyms that element repeats",li.count(90))
li.sort(reverse=True)
print("sorting the li in descending order:",li)
li.sort()
print("sorting the li in ascending order:",li)
li.insert(0,00)
print("iinserting data,li=",li)
p = li.pop(2)
print("deleting the element with position",p)
ex = [0,1,2,3,4,5]
li.extend(ex)
print("adding two lists into one",li)
li.reverse()
print("reverse order of li", li)
i = li.index(2)
print("fetching with index", i)
co = li.copy()
print("copied from li, co=",co)
co.clear()
print("clearing the data of co, co=",co)
li.remove(90)
print("removing particular elelment by its name, li=",li)
lii = ['1','2','3','a','4','b']
lii.sort()
print(lii)
lii.reverse()
print(lii)
