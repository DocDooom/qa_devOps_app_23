user_in = int(input("Please input an integer: "))

result = 1
while user_in > 0:
    result *= user_in
    user_in -=1

print(result)
