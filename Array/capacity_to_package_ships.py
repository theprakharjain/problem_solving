# Capacity to ship packages within D days - Leetcode-Medium

# Solution-1 ------------------------------------------- [Binary Search]

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5

low = max(weights)
high = sum(weights)

while low < high:
    mid = low + ((high - low)//2)
    current = 0
    day = 1

    for w in weights:
        if current + w > mid:
            day += 1
            current = 0

        current += w

    if day > D:
        low = mid + 1
    else:
        high = mid

print(low)
