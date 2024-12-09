def read_puzzle_input(filename="../puzzle_input.txt"):
	with open(filename, "r") as f:
		return f.readlines()

def parse_puzzle_input(puzzle_input):
	left_hand_side  = []
	right_hand_side = []

	for line in puzzle_input:
		lhs, rhs = line.split("   ")
		left_hand_side.append(int(lhs))
		right_hand_side.append(int(rhs))

	left_hand_side.sort()
	right_hand_side.sort()

	return (left_hand_side, right_hand_side)

def get_similarity(left_hand_side, right_hand_side):
	similarity = [element * right_hand_side.count(element) for element in left_hand_side]
	return sum(similarity)

def main():
	puzzle_input = read_puzzle_input()
	#puzzle_input = """3   4\n4   3\n2   5\n1   3\n3   9\n3   3""".split("\n")
	lhs, rhs = parse_puzzle_input(puzzle_input)
	similarity = get_similarity(lhs, rhs)
	print(f"The answer is: {similarity}.\n")

if __name__ == "__main__":
	main()
