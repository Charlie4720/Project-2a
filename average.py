# Prompt the user to enter 5 numbers
numbers = []
for i in range(5):
    num = float(input("Enter number {}: ".format(i+1)))
    numbers.append(num)

# Calculate the average
average = sum(numbers) / len(numbers)

# Print the average to 1 decimal place
print("The average is:", round(average, 1))
