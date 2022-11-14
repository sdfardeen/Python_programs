input_string = "2,4,6,8"
som = "16"
num_arr = [int(i) for i in input_string.split(",")]
som = int(som) if type(som) == str and som else 0


def get_combi(num_arr):

	res = []

	t_sum = som

	for i in num_arr:

		if not som:

			return

		t_sum = som

		tmp = i

		tmpres = []

		while t_sum % tmp == 0:

			tmpres.append(tmp)

			t_sum = int(t_sum//tmp)

		if tmpres:

			res.append(tmpres)

	print(res)


get_combi(num_arr)
