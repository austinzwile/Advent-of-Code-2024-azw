def get_reports(puzzle_filename="puzzle_input.txt"):
	with open(puzzle_filename, "r") as f:
		return [list(map(int, line.split())) for line in f if line.strip()]

def get_pairs(report):
	return [(report[i - 1], report[i]) for i in range(1, len(report))]

def get_max_distance_between_pairs(pairs):
	return max([abs(pair[1] - pair[0]) for pair in pairs])

def is_unidirectional(pairs):
	directions = [pair[1] - pair[0] for pair in pairs]
	return all(d > 0 for d in directions) or all(d < 0 for d in directions)

#def is_unidirectional(report):
# 	direction = None
#
#	for i in range(1, len(report)):
#		change = report[i] - report[i - 1]
#		if change > 0:
#			if direction == Trend.DECREASING:
#				return False
#			direction = Trend.INCREASING
#		elif change < 0:
#			if direction == Trend.INCREASING:
#				return False
#			direction = Trend.DECREASING
#		else:
#			return False
#
#	return True

def solve_puzzle(reports):
	number_of_safe_reports = 0
	for report in reports:
		pairs = get_pairs(report)
		if not is_unidirectional(pairs): continue
		if get_max_distance_between_pairs(pairs) > 3: continue
		number_of_safe_reports += 1
	return number_of_safe_reports

def main():
	reports = get_reports()
	answer = solve_puzzle(reports)
	print(f"The answer to the puzzle is: {answer}.")

if __name__ == "__main__":
	main()
