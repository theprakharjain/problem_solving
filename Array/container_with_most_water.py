# Container With Most Water - Leetcode-Medium

# Solution-1 ------------------------------------------- [Time Limit exceeds in this one]

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [1, 2]
thisdict = {}
answer = 0

for i in range(len(height)):
    j = {i+1:height[i]}
    thisdict.update(j)

# print(thisdict)

for i in range (len(height)):
    for k in range (len(height)):
        if (thisdict.get(k+1) <= height[i] and k+1 != i+1):
            max_vol = thisdict.get(k+1) * abs(((k+1)-(i+1)))
            if max_vol > answer:
                answer = max_vol

print(answer)

# Solution-2 ------------------------------------------- [Two Pointer Method]
size = len(height)
total_breadth = size-1

right = total_breadth
left = 0
area = 0

for breadth in range (total_breadth, 0, -1):
    if (height[left] < height[right]):
        area = max(area, breadth * height[left])
        left += 1
    else:
        area = max(area, breadth * height[right])
        right -= 1

print(area)


