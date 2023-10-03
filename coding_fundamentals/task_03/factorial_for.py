user_input = int(input("Number: "))

count = 1
for x in range(user_input, 0, -1):
    count *= x

print(count)
