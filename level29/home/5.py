
numbers = list(range(1, 11))


first_half = numbers[:5]


second_half = numbers[5:]


squares = [num ** 2 for num in numbers]

# Step 5: Print all three lists
print("First half:", first_half)
print("Second half:", second_half)
print("Squares:", squares)