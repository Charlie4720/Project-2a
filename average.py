# Get five numbers from the user
numbers = input("Enter five numbers separated by spaces: ").split()

# Convert the input into a list of floats
numbers = [float(num) for num in numbers]

# Calculate the average
average = sum(numbers) / len(numbers)

# Print the average
print("The average is:", average)
