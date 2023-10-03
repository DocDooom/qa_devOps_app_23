while True:
    exam_1 = input("exam 1: ")
    try:
        exam_1 = float(exam_1)
    except:
        print("Not a valid number please try again")
        continue
    exam_2 = input("exam 2: ")
    try:
        exam_2 = float(exam_2)
    except:
        print("Not a valid number please try again")
        continue
    exam_3 = input("exam 3: ")
    try:
        exam_3 = float(exam_3)
    except:
        print("Not a valid number please try again")
        continue

    calc_avg = (exam_1 + exam_2 + exam_3) / 3

    print(f"Average mark is {round(calc_avg, 2)}")

    if calc_avg < 65:
        print("FAIL")
    else:
        print("PASS")
    break

