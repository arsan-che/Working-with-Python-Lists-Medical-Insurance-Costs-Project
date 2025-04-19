# List of names of individuals
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]

# List of corresponding insurance costs for each individual
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add a new individual 'Priscilla' and her insurance cost to the lists
names.append('Priscilla')
insurance_costs.append(8320.0)

# Combine insurance costs and names into a list of tuples using zip
medical_records = zip(insurance_costs, names)
list_of_medical_records = list(medical_records)

# Print the list of medical records
print(list_of_medical_records)

# Calculate and print the number of medical records
num_medical_records = len(list_of_medical_records)
print(f'There are {num_medical_records} medical records.')

# Select and print the first medical record
first_medical_record = list_of_medical_records[0]
print(first_medical_record)
print(f'Here is the first medical record: {first_medical_record}')

# Sort the medical records by insurance cost and print them
list_of_medical_records.sort()
print(f'Here are the medical records sorted by insurance cost: {list_of_medical_records}')

# Select and print the three cheapest insurance costs
cheapest_three = list_of_medical_records[:3]
print(f'Here are the three cheapest insurance costs in our medical records: {cheapest_three}')
