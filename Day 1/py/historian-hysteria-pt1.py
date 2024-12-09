def read_puzzle_input(filename="../puzzle_input.txt"):
	with open(filename, "r") as f:
		return f.readlines()

def parse_puzzle_input(puzzle_input):
	left_hand_side  = []
	right_hand_side = []

	for line in puzzle_input:
		lhs, rhs = line.split("   ")
		left_hand_side.append(lhs)
		right_hand_side.append(rhs)

	left_hand_side.sort()
	right_hand_side.sort()

	return (left_hand_side, right_hand_side)

def get_distance(left_hand_side, right_hand_side):
	distance = 0

	for left_element, right_element in zip(left_hand_side, right_hand_side):
		distance += abs(int(left_element) - int(right_element))

	return distance

def main():
	puzzle_input = read_puzzle_input()
	lhs, rhs = parse_puzzle_input(puzzle_input)
	distance = get_distance(lhs, rhs)
	print(distance)

if __name__ == "__main__":
	main()
