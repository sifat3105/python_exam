def find_largest_number(numbers):
    if not numbers:
        return None
    
    big_number = 0
    for number in numbers:
        if number > big_number:
            big_number = number
        
    return big_number


numbers = [10, 5, 20, 15, 30]
print(find_largest_number(numbers))
