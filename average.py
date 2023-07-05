# Ask the user to input five numbers separated by commas
numbers_input = input("Enter five numbers: ")

# Split the input string into a list of individual numbers
numbers_list = numbers_input.split(',')

# Convert the numbers from strings to floats
numbers = [float(num) for num in numbers_list]

# Calculate the average of the numbers
average = sum(numbers) / len(numbers)

# Print the average
print("The average of those numbers is:", average)
