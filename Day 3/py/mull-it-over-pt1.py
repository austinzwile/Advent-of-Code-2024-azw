import re

def read_puzzle_input(filename="../puzzle_input.txt"):
	with open(filename, "r") as f:
		return f.read()

def parse_out_mul_expressions(puzzle_input):
	mul_syntax_regex = r"mul\([0-9]+\,[0-9]+\)"
	mul_expressions = re.findall(mul_syntax_regex, puzzle_input)
	return mul_expressions

def get_mul_args(mul_expression):
	mul_args_regex = r"[0-9]+"
	args = re.findall(mul_args_regex, mul_expression)
	return (args[0], args[1])

def solve_puzzle(mul_expressions):
	mul_expression_results = []
	for expr in mul_expressions:
		x, y = get_mul_args(expr)
		mul_expression_results.append(int(x) * int(y))
	return sum(mul_expression_results)

def main():
	puzzle_input = read_puzzle_input()
	mul_expressions = parse_out_mul_expressions(puzzle_input)
	answer = solve_puzzle(mul_expressions)
	print(answer)

if __name__ == "__main__":
	main()
