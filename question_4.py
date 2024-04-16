def prime_numbers(n):
    prime_num = []
    for number in range(2,n):
        is_prime = True
        for i in range (2, int(number **0.5)+1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_num.append(number)
    
    return prime_num

n = 20
print(prime_numbers(n))