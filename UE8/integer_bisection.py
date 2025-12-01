def contains_zero(vec):
    left, right = 0, len(vec)-1

    while left <= right:
        mid = (left + right) // 2
        if vec[mid] == 0:
            return True
        elif vec[mid] > 0:
            right = mid - 1
        else:
            left = mid + 1

    return False

print(contains_zero([-3, -2, -1, 0, 1]))
print(contains_zero([5, 4, 3]))