import re

def read_puzzle_input(filename="../puzzle_input.txt"):
	with open(filename, "r") as f:
		return f.read()

def parse_out_mul_expressions(block):
	mul_syntax_regex = r"mul\([0-9]+\,[0-9]+\)"
	mul_expressions = re.findall(mul_syntax_regex, block)
	return mul_expressions

def get_mul_args(mul_expression):
	mul_args_regex = r"[0-9]+"
	args = re.findall(mul_args_regex, mul_expression)
	return (args[0], args[1])

def get_good_blocks(puzzle_input):
    split_regex = r"(do\(\)|don\'t\(\))"
    segments = re.split(split_regex, puzzle_input)

    mul_enabled = True
    good_blocks = []

    for segment in segments:
        if segment == "do()":
            mul_enabled = True
        elif segment == "don't()":
            mul_enabled = False
        elif mul_enabled:
            good_blocks.append(segment)

    return good_blocks

def solve_puzzle(mul_expressions):
	results = []
	for expression in mul_expressions:
		x, y = get_mul_args(expression)
		results.append(int(x) * int(y))
	return sum(results)

def main():
	puzzle_input = read_puzzle_input()
	good_blocks = get_good_blocks(puzzle_input)

	expressions = []
	for block in good_blocks:
		expressions += parse_out_mul_expressions(block)

	answer = solve_puzzle(expressions)
	print(f"The answer is: {answer}.")

if __name__ == "__main__":
	main()
