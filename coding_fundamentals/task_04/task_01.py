print("Chapter 04 Lab")

ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,
81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
print(ages)

ages_len = len(ages)
print(ages_len)

ages = [age + 1 for age in ages]

print(ages)

filtered_ages = [age for age in ages if 16<=age<=65]
print("FILTERED AGES")
print(filtered_ages)
print(len(filtered_ages))

filtered_ages.sort()

print(filtered_ages)

print(len([age for age in filtered_ages if 16<=age<=25]))

proportion = (sum(1 for age in filtered_ages if 16<=age<=25)) / len(filtered_ages)

print(f"{(proportion * 100):.2f}%")