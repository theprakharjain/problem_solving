# Find the Duplicate Number -287- Leetcode-Medium

# Solution-1 -------------------------------------------

nums = [1, 3, 4, 2, 2]

thisdict = {}
answer = 0

for i in range(len(nums)):
    if not thisdict:
        thisdict.update({nums[i]:nums[i]})

    if nums[i] != thisdict.get(nums[i]):
        thisdict.update({nums[i]: nums[i]})
    else:
        answer = thisdict.get(nums[i])

print(answer)


