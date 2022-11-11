inpe = ")({(}{}{})]["

def count_balance(inp):
    open_count = 0
    for i in inp:
        if i == '(' or i == '{' or i == '[':
            open_count += 1
        elif i == ')' or i == '}' or i == ']':
            open_count -= 1

    # data

    print(open_count)


def patt_balance(inp):
    data = ['{}', '()', '[]']
    while any(x in inp for x in data):
        for br in data:
            inp = inp.replace(br, '')
    return(not inp)

import re
inner_brackets_found = True
ste = "2*3*(4/2)+4*(21/3)"
print(re.sub('[*()/+-]', "", ste))
total_result = 0
while inner_brackets_found:
    ed = re.search("\([^\(\)]+\)", ste)
    if ed!=None:
        expr_with_brackets = ste[ed.start():ed.end()]
        print(ed.start(), ed.end())
        ste = ste.replace(expr_with_brackets, "21")
    else:
        inner_brackets_found = False
        total_result = 45

print(total_result)