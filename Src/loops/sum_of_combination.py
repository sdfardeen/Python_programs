input_string = "2,4,6,8"
som = "16"
num_ar = [int(i) for i in input_string.split(",")]
som = int(som) if type(som) == str and som else 0


def get_combi(num_ar):

	res = []

	tsum = som

	for i in num_ar:

		if not som:

			return

		tsum = som

		tmp = i

		tmpres = []

		while tsum % tmp == 0:

			tmpres.append(tmp)

			tsum = int(tsum//tmp)

		if tmpres:

			res.append(tmpres)

	print(res)


get_combi(num_ar)
