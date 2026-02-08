# Convert Temperature to Fahrenheit

"""
Write a function ”convert temp” that takes one argument ”x” representing 
temperature in Celsius. The function should check if the ”x” is a number 
(integer or float). If ”x” is the number, the function should convert the 
temperature to Fahrenheit and print out the converted temperature 
(Note: F = 1.8 ∗ C + 32). In other case, the function should print 
”Argument x should be float or integer”.
"""

def convert_temp(x):
    # Check if x is a number (either int or float)
    if isinstance(x, (int, float)):
        # Convert Celsius to Fahrenheit
        fahrenheit = 1.8 * x + 32
        print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
    else:
        # Handle invalid input
        print("Argument x should be float or integer")

# O(1) - Time complexity
# O(1) - Space complexity

# Example usage:
convert_temp(25)    # Valid input
convert_temp("25")  # Invalid input
convert_temp(0.0)   # Valid input
