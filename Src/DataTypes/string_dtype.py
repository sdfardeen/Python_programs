def string_functions():
    str_data = "Im fardeen"

    # syntax : str.capitalize()
    # no params
    # it'll capitalize the first letter
    print("Capt", str_data.capitalize())

    # syntax: str.casefold()
    # no params
    # it converts upper case letter to lower case
    print("casefold:", str_data.casefold())

    # syntax : str.center()
    # params: takes an integer element
    # it creates the given string into the center, default to center is "space"
    str_center = str_data.center(15)
    print(str_center)

    # syntax: str.count()
    # params: element in data
    # str.count(), const the string how many times' inn the given string
    print("count", str_data.count("e"))

    # syntax: str.encode()
    # params:encoding=encoding(optional), errors=errors(optional)
    # returns in bytes
    print("encode", str_data.encode())

    # syntax : str.isalnum()
    # no params
    # returns boolean dtype)
    print("isalnum:", str_data.isalnum())
    # syntax : str.isalpha()
    # no params
    # returns boolean dtype)
    print("isalpha:", str_data.isalpha())

    # syntax: str.removeprefix()
    # Parameters: prefix– prefix string that we are checking for.
    # Return: Returns the copy of the string with the prefix removed(if present), else the original string
    print("removeprefix:", str_data.removeprefix('Im'))

    # syntax : str.endswith()
    # params : string that we are checking for
    # returns boolean dtype
    print("endswith:", str_data.endswith('f'))

    # syntax : str.isnumeric()
    # no params
    # returns boolean dtype
    print("isnumeric:", str_data.isnumeric())


string_functions()
