def string_solution(S: str, T: str):
    """

    :param S:
    :param T:
    :return:
    """
    if not S or not T:
        print("IMPOSSIBLE")
        return 0
    s_Size = len(S)
    t_Size = len(T)
    if s_Size == t_Size:
        if S == T:
            print("EQUAL")
            return 0
        swap_element(S, T, s_Size)
    elif s_Size > t_Size:
        swap_element(S, T, t_Size)
        for j in range(t_Size, s_Size):
            print("REMOVE {}".format(S[j]))

    elif s_Size < t_Size:
        swap_element(S, T, s_Size)
        for j in range(s_Size, t_Size):
            print("INSERT {}".format(T[j]))


def swap_element(S: str, T: str, tell_Size: int):
    """

    :param S:
    :param T:
    :param tell_Size:
    :return:
    """
    data = []
    for i in range(tell_Size):
        if S[i] != T[i]:
            data.append([S[i], T[i]])
    if len(data) != tell_Size:
        for j, k in data:
            print("SWAP element {} with {}".format(j, k))
    else:
        print("IMPOSSIBLE")


# calling the function with inputs
string_solution("arej", "nge")
