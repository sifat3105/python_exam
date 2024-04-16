def find_duplicate_number(numbers):
    alist = set()
    duplicates = set()
    for num in numbers:
        if num in alist:
            duplicates.add(num)
        else:
            alist.add(num)
    return list(duplicates)

numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 5]
print(find_duplicate_number(numbers))
