# Subsets - Leetcode-Medium

# Solution-1 -------------------------------------------

nums = [1, 2, 3]

thislist = []
x = len(nums)
for i in range(1 << x):
    thislist.append([nums[j] for j in range(x) if (i & (1 << j))])

print(thislist)

# Solution-2 -------------------------------------------

output = [[]]

for i in nums:
    output += [last_items + [i] for last_items in output]
    # print(output)

print(output)
