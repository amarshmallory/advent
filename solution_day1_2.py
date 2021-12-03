file = "input_day_1.txt"

data = []

for x in open(file, "r"):
	data.append(int(x))

daily_solutions = {}

# day 1
daily_solutions[1] = sum([data[x] > data[x-1] for x in range(1, len(data))])
# day 2
daily_solutions[2] = sum([data[x] > data[x-3] for x in range(3, len(data))])

for key,value in daily_solutions.items():
	print(f"Day {key}: {value}")