#name = "test"
#if name == name[::-1]:
    #print("palindrom")

#else:
    #print("false")

def is_palindrom(name):
    if name == name[::-1]:
        return ("is_palindrom")

    else:
        return ("not palindrom")

print(is_palindrom("lol"))
print(is_palindrom([1,4,3,2,1]))
print(is_palindrom([1,2,3,[4,5],3,2,1]))
print(is_palindrom([1,[2,3],4,[3,2],1]))