import math

print('''
Pythagoras Calc:
1. Find A given B & C
2. Find B given A & C
3. Find C given A & B
''', end="")

input_seleciton = input(": ")

match input_seleciton:
    case "1":
        len_b = float(input("What is len B: "))
        len_c = float(input("What is len C: "))
        a_sqrd = len_c**2 - len_b**2
        print(math.sqrt(a_sqrd))
    case "2":
        len_a = float(input("What is len A: "))
        len_c = float(input("What is len C: "))
        b_sqrd = len_c**2 - len_a**2
        print(math.sqrt(b_sqrd))
    case "3":
        len_a = float(input("What is len A: "))
        len_b = float(input("What is len B: "))
        c_sqrd = len_a**2 + len_b**2
        print(math.sqrt(c_sqrd))