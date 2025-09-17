num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is NOT a Prime Number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):   # √num পর্যন্ত check
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is NOT a Prime Number")
