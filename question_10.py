def median(alist):
    sorded_list = sorted(alist)
    n = len(sorded_list)
    if n % 2 == 0:
        mid_left = sorded_list[n // 2 - 1]
        mid_right = sorded_list[n // 2]
        return (mid_left + mid_right) /2
    else :
        return sorded_list[n // 2]
    
numbers = [7, 3, 1, 5, 9, 10]
print("Median:", median(numbers))