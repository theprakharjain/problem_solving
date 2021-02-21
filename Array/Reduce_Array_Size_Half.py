# Reduce Array Size to The Half - Leetcode-Medium
import collections

# First Solution ----------------------------------------------------

# arr = [9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]
# arr = [1000, 1000, 3, 7]
# arr = [7,7,7,7,7,7]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def minSetSize(arr):
    element_count = 1
    answer = 0
    half_len = 0
    element_count_list = []

    # sorting the array
    arr.sort()

    # counting the number of same and different elements in the array and
    # appending them in into the element_count_list
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            element_count += 1
        else:
            element_count_list.append(element_count)
            element_count = 1

    # Handling the corner case if all the elements are unique example- [7,7,7,7,7,7]
    # or all the *end* elements are the same example- [3,7,1000,1000]
    if len(element_count_list) == 0 or element_count > 1:
        element_count_list.append(element_count)

    # arranging the elements count list in the descending order
    element_count_list.sort(reverse=True)

    # Itirating through the elements count list and
    # incrementing the answer count with the increment in every element needed to cut the list in half
    for x in element_count_list:
        if (x >= len(arr)/2):
            answer = 1
            break

        if (half_len < len(arr)/2):
            half_len = half_len + x
            answer += 1

    print(answer)

# minSetSize(a)


# Second Solution ------------------------------------------------

# We need to import the *collections* module for it

total_count = 0

arr_mc = collections.Counter(arr).most_common()

for i in range(len(arr_mc)):
    total_count += arr_mc[i][1]
    if total_count >= len(arr)/2:
        print(i + 1)
        break
