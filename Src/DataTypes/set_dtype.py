set_data = {1,2,3,4,'a','b','c','d'}
# syntax:set.add(element),
# params:element,
# returns nothing
set_data.add(5)
print(set_data)

# syntax: set.pop(no arguement),
# returns element by its first position
print('poping the element:',set_data.pop())
print('after pop:',set_data)

# syntax: set.remove(element),
# it removes an element from given set
set_data.remove('a')
print('removing an element',set_data)

set_data2 = {1,2,3,4,'a','b','c','d','hey','john','come', 'back'}

# syntax: set.copy(),
# returns another set of data
duplicate_data = set_data.copy()
print(duplicate_data)
duplicate_data.clear()
print('cleared the data of dupicate_data=',duplicate_data)

# syntax: set.discard(element),
# it removes an element from given set
set_data.discard(5)
print('element 5 is removed',set_data)

# syntax: set.issubset(),
# params:takes another set,
# returns bool
# this is not subset becuase there are no elements of set_data in set_data2
print('set_data is subset of set_data2',set_data.issubset(set_data2))

# syntax: set.isdisjoint(),
# params:takes another set,
# returns bool
# this is not subset because there is common element in both datas
print('set_data is disjoint of set_data2 ',set_data.isdisjoint(set_data2))

# syntax: set.issuperset(),
# params:takes another set,
# returns bool
# set_data is not superset of set_data2, because elements of set_data is not from set_data2
print(set_data.issuperset(set_data2))
print(set_data2.issuperset(set_data))

# syntax:set.inersection(),
# params:set1, set2 ... etc,
# returns a set that contains the similarity between two or more sets.
# method intersection is done that which elements are common that'll only displays
print('method intersection',set_data.intersection(set_data2))
print('set_data=',set_data)

# syntax:set.intersection_update(set1, set2 ... etc),
# params:set1, set2 ... etc,
# returns a new set, without unwanted items
set_data.intersection_update(set_data2)
print('intersection_update',set_data)

# syntax:set.difference(set),
# params:set,
# returns a set that contains the difference between two sets.
# method difference is done that which elements are not common that'll only displays
print('method difference',set_data.difference(set_data2))

# syntax:set.difference_update(set),
# params:set,
# returns a new set, without unwanted items
set_data.difference_update(set_data2)
print('after difference_update',set_data)

# syntax:set.symmetric_difference(set),
# params:set,
# returns a set that contains all items from both set
print('method symmetric_difference',set_data.symmetric_difference(set_data2))

# syntax:set.symmetric_difference_update(set),
# params:set,
# updates the original set by removing items that are present in both sets, and inserting the other items.
set_data.symmetric_difference_update(set_data2)
print('after symmetric_difference_update',set_data)

# syntax:set.union(set1, set2...etc),
# params:set1, set2...etc,
# returns a set that contains all items from the original set
set_data.union(set_data2)
print('union of set_data and set_data2',set_data)

# syntax:set.update(set),
# params:set,
# updates the current set, by adding items from another set
set_data.update(set_data2)
print('updated set_data=',set_data)
