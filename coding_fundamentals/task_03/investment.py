print("INVESTMENT CALC")

initial_in = float(input("Initial Investement: "))
target_val = float(input("Target Value: "))
interest_rate = float(input("Interest Rate: "))

ret_total = initial_in

years = 0

while True:
    ret_val = (interest_rate / 100) * ret_total
    ret_total += ret_val
    years += 1

    if ret_total > target_val:
        break

print(f"It will take {years} to reach value")