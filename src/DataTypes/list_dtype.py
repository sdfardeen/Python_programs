li = [12, 23, 34, 45, 56, 67, 78, 89, 90]

# syntax: li.append()
# params : an element which are appending into list
li.append(100)
print("appending 100 into li, li=", li)

# syntax : li.sort()
# params : reverse=true\false
print("counting that howmany tyms that element repeats", li.count(90))
li.sort(reverse=True)
print("sorting the li in descending order:", li)
li.sort()

# syntax : li.insert()
# params : position\index, element
print("sorting the li in ascending order:", li)
li.insert(0, 00)
print("iinserting data,li=", li)

# syntax : li.pop()
# params : postion
# returns an element
p = li.pop(2)
print("deleting the element with position", p)

ex = [0, 1, 2, 3, 4, 5]

# syntax : li.extend()
# params : another list
li.extend(ex)
print("adding two lists into one", li)

# syntax : li.reverse()
# no params
li.reverse()
print("reverse order of li", li)

# syntax : li.index()
# params : element,start,end
# returns : returns the lowest index where the element appears.
i = li.index(2)
print("fetching with index", i)

# syntax : li.copy()
# no params
co = li.copy()
print("copied from li, co=", co)

# syntax : li.clear
# no params
co.clear()
print("clearing the data of co, co=", co)

# syntax : li.remove()
# params : element
li.remove(90)
print("removing particular elelment by its name, li=", li)
lii = ['1', '2', '3', 'a', '4', 'b']
lii.sort()
print(lii)
lii.reverse()
print(lii)
