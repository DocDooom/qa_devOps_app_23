from datetime import datetime

# DD:HH:MM
# part two takes just raw numbers

def add_times(time_01: str, time_02: str) -> str:
    time_01_list = time_01.split(":")
    time_02_list = time_02.split(":")

    added_list = [int(a) + int(b) for a, b in zip(time_01_list, time_02_list)]
    return ":".join(map(str, added_list))


def time_diff(time_01: str, time_02: str) -> str:
    time_01_list = time_01.split(":")
    time_02_list = time_02.split(":")

    added_list = [int(a) - int(b) for a, b in zip(time_01_list, time_02_list)]
    return ":".join(map(str, added_list))

def convert_to_hours(min_str: str) -> str:
    t_list = []
    t_list.append(int(min_str) // 60)
    t_list.append(int(min_str) % 60)
    return ":".join(map(str, t_list))


def convert_to_minutes(mins: int) -> str:
    pass

def convert_min_to_time():
    pass

def convert_hours_to_time():
    pass

def convert_days_to_time():
    pass

print('''
Time Calc
1. Add 2 times
2. Find the difference between 2 times
3. Convert to Hours
4. Convert to Minutes
5. Convert Minutes to Time
6. Convert Hours to Time
7. Convert Days to Time
8. Exit
''')

selection = input(": ")

match selection:
    case "1":
        time_1 = input("Input a time DD:HH:MM: ")
        time_2 = input("Input another time DD:HH:MM: ")
        print(add_times(time_1, time_2))
    case "2":
        time_1 = input("Input a time DD:HH:MM: ")
        time_2 = input("Input another time DD:HH:MM: ")
        print(time_diff(time_1, time_2))
    case "3":
        hours = input("Input a time in minutes: ")
        print(convert_to_hours(hours))
    case "4":
        pass
    case "5":
        pass
    case "6":
        pass
    case "7":
        pass
    case "8":
        exit()