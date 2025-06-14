# Create a function that merges two sorted arrays into one final sorted array
# eg: merge_sorted_array([0, 3, 4, 31], [4, 6, 30])
# == [0, 3, 4, 4, 6, 30, 31]

# Time Complexity : O(n*m)
# Space Complexity : O(n+m)
def merge_naive(arr1, arr2):
    arr_large = arr1 if len(arr1) > len(arr2) else arr2
    arr_small = arr1 if arr_large == arr2 else arr2

    curr_small_index = 0

    output = []

    for i in range(len(arr_large)):
        while curr_small_index < len(arr_small) and arr_small[curr_small_index] < arr_large[i]:
            output.append(arr_small[curr_small_index])
            curr_small_index += 1
        output.append(arr_large[i])

    return output

# Time Complexity : O((n+m) log(n+m)) (`sorted` complexity)
# Space Complexity : O(1)
def merge_native(arr1, arr2):
    arr1.extend(arr2)
    return sorted(arr1)

# Time Complexity : O(n+m)
# Space Complexity : O(n+m)
def merge_combine(arr1, arr2):
    i = 0
    j = 0

    output = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1

    if i == len(arr1):
        output.extend(arr2[i:])
    else:
        output.extend(arr1[j:])

    return output


print(merge_naive([0, 3, 4, 31], [4, 6, 30]))
print(merge_naive([4, 6, 30], [0, 3, 4, 31, 66, 99]))
print(merge_combine([4, 6, 30], []))
print(merge_native([0, 3, 4, 31], [4, 6, 30]))
print(merge_combine([0, 3, 4, 31], [4, 6, 30]))
print(merge_combine([4, 6, 30], [0, 3, 4, 31, 66, 99]))
print(merge_combine([4, 6, 30], []))