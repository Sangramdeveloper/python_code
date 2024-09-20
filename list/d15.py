def display_powers():
    # Define the range for numbers and powers
    numbers = range(1, 11)
    max_power = 2

    # Loop through each number
    for num in numbers:
        print(f"Powers of {num}:")
        # Calculate and print powers of the current number
        for power in range(1, max_power + 1):
            print(f"{num}^{power} = {num ** power}")
        print()  # Add a blank line for readability

if __name__ == "__main__":
    display_powers()
