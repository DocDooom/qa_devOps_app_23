num_1 = float(input("Please enter a number: "))
num_2 = float(input("Please enter another number:"))

print('''
What operation would you like to carry out:
1. Add +
2. Subtract -
3. Multiply *
4. Divide /
5. To the power p
''', end="")

selection = input(": ")

match selection:
    case "1":
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    case "2":
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    case "3":
        print(f"{num_1} * {num_2} = {num_1 * num_2}")
    case "4":
        print(f"{num_1} / {num_2} = {num_1 / num_2}")
    case "p":
        print(f"{num_1} ** {num_2} = {num_1 ** num_2}")