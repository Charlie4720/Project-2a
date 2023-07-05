# Prompt the user to enter five numbers
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the average of the numbers
average = sum(numbers) / len(numbers)

# Display the average to 7 decimal places
formatted_average = "{:.7f}".format(average)
print("Average:", formatted_average)
