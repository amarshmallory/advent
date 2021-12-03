file = "input.txt"

data = []

for x in open(file, "r"):
	data.append(int(x))

solutions = {}

# part 1
solutions[1] = sum([data[x] > data[x-1] for x in range(1, len(data))])
# part 2
solutions[2] = sum([data[x] > data[x-3] for x in range(3, len(data))])

for key,value in solutions.items():
	print(f"Question {key}: {value}")