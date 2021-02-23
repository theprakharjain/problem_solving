# Combination Sum - Leetcode-Medium

# Solution-1 -------------------------------------------

matrix = [2, 3, 6, 7]
target = 7


results = []
matrix.sort(reverse=True)


def generate(remains=target, combination=[]):
		if remains < 0:
			return
		if not remains:
			results.append(combination)
			return
		last_used = combination[-1] if combination else matrix[0]
		for c in matrix:
			if c > last_used:
				continue
			generate(remains - c, combination + [c])

generate()
print(results)
