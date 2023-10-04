import csv

file_path = 'carsale.csv'

# Create a list to store monthly sums
monthly_sums = [0] * 8

total_man = []

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        if not row:
            continue  # Skip empty rows
            
        company_name = row[0]
        monthly_data = next(csv_reader)  # Read the next row for monthly data
        
        # Convert strings to integers
        monthly_data = [int(i) for i in monthly_data]

        # Add up the monthly data to monthly_sums
        monthly_sums = [sum(x) for x in zip(monthly_sums, monthly_data)]

        total_man.append((company_name, sum(monthly_data)))

# Print the results
print("====================================================")

print(*monthly_sums, sep="\n")
print("Total: ", sum(monthly_sums))

print("====================================================")


for company, total in total_man:
    print(company)
    print(total)

print("====================================================")