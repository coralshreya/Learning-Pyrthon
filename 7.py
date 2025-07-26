print("Prime numbers between 20 and 50 are:")

for num in range(20, 51):  # 51 to include 50
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

