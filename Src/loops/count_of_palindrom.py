def possible_count_of_palindrom(input_data):
    n = len(input_data)
    input_data = list(input_data)

    # loop through character of string
    count = 0
    for i in range(n//2):
        if input_data[i] != input_data[n - i - 1]:
            count += 1

    return count


print(possible_count_of_palindrom('aab'))
