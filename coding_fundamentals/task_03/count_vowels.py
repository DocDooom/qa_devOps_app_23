count_string = input("Please input a word: ")

count = 0
vowels = set("aeiouAEIOU")

for char in count_string:
    if char in vowels:
        count += 1

print(count)