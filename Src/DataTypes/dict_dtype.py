dict_data = {1:'Name',
             2:'Age',
             3:'Country',
             4:'State',
             5:'Pincode'}

dict_data2 = {6:'Bgroup'}
dict_data3 = {7:'Sex'}

# syntax: dict.update(single arguement)
# params : single arguement
# it'll add dict data to anaother dict data
dict_data.update(dict_data2)
print(dict_data)

# syntax: dict.pop(key)
# params : key
# it'll remove the element by key
print(dict_data.pop(6))
print('after pop funtion, dict_data=',dict_data)

# syntax : dict.copy()
# params: no arguements passed
# it'll cotupy the dict and returns duplicate dict
dict_data4 = dict_data.copy()
print('dict_data4 = ',dict_data4)

# syntax : dict.fromkeys(seq,value)
# params: sequel data, value
# it'll assign
dic_data = dict_data4.fromkeys(dict_data2,None)
print('dict_data5 = ',dic_data)

# syntax: dict.update(another dict)
# params: another dict
# it'll combine two dicts into one and doeesn't return values
dict_data.update(dict_data2)
print('updating Dict_data and dict_data2, dict_data=',dict_data)

# syntax: dict.keys()
# params: no argument
# a new object will return with all keys
print('keys:',dict_data.keys())

# syntax: dict.values()
# params: no argument
# returns a new object with all values
print('values of',dict_data.values())

dict_data[2] = 'Fardeen'
print('updated dict_data = ',dict_data)

# dict..get(), when we are fetching the data, if it is available iin given data, it'll return,
# if its not then it'll retun NONe, by default we can set a value to replace the NONE
# syntax: dict.get(key,default_value)
# params: key,default_value
print(dict_data.get(2,0))

print(dict_data)
print(dict_data.popitem())

print(dict_data.pop(5))
print(dict_data)
