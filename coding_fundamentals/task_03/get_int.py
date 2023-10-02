min_val = int(input("Input min integer: "))
max_val = int(input("Input max integer: "))

count = 0
while True:
    user_num = int(input("Input a value between the above: "))
    count += 1

    if count >= 3:
        print(None)
        break

    if user_num in range(min_val, max_val + 1):
        print(user_num)
        break
    

