n = 8
# we are taking result as 0, because it's an integer datatype
res = 0

# we are passing 'if' condition
if res > 2:
    # we are iterating in range
    for i in range(1, n+1):
        # passing 'if' condition to satisfy the result
        if n % 1 == 0:
            print("prime")
            # using 'break' keyword to break the iteration when the condition satisfied
            break
        else:
            print("not")
else:
    print("not")
