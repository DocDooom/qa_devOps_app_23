import csv

# Replace 'filename.csv' with the actual name of your file
file_path = 'carsale.csv'

# Create a list to store monthly sums
monthly_sums = [0] * 8  # Assuming 8 months of data; adjust as needed

with open(file_path, mode ='r') as file:
    csv_reader = csv.reader(file)

    monthly_sums = [0,0,0,0,0,0,0,0]
    total_man = []
    
    for row in csv_reader:
        if not row:
            continue  # Skip empty rows
            
        company_name = row[0]
        monthly_data = next(csv_reader)  # Read the next row for monthly data
        monthly_data = [int(i) for i in monthly_data]
        print(company_name)
        print(monthly_data)

        monthly_sums[0] += monthly_data[0]
        monthly_sums[1] += monthly_data[1]
        monthly_sums[2] += monthly_data[2]
        monthly_sums[3] += monthly_data[3]
        monthly_sums[4] += monthly_data[4]
        monthly_sums[5] += monthly_data[5]
        monthly_sums[6] += monthly_data[6]
        monthly_sums[7] += monthly_data[7]

        total_man.append(company_name)
        total_man.append(sum(monthly_data))



print(*monthly_sums, sep="\n")
print("Total: ", sum(monthly_sums))

print(*total_man, sep="\n")



        


