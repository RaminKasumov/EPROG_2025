def remove_number_from_list(numbers, n):
    if n in numbers:
        numbers.remove(n)
    return numbers

print(remove_number_from_list([1, 2, 3, 4, 5], 2))