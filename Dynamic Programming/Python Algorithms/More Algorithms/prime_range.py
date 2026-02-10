# Prime Range

"""
Write a function ”prime range” that takes single argument ”x”. 
The function should find and print all prime numbers in range from 1 to ”x”. 
The function should return the list of all found prime numbers.
"""

def prime_range(x: int) -> list[int]:
    # Check if x is an integer greater than or equal to 2
    if not isinstance(x, int) or x < 2:
        print("Argument x should be an integer greater than or equal to 2")
        return []

    def is_prime(n):
        """Helper function to check if a number is prime."""
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Find all prime numbers in the range 1 to x
    primes = [num for num in range(2, x + 1) if is_prime(num)]

    # Print all prime numbers
    print(f"Prime numbers in range 1 to {x}: {primes}")

    # Return the list of primes
    return primes

# O(n * (1/2)) - Time complexity
# O(n) - Space complexity

# Example usage:
prime_list = prime_range(20)
print("List of primes:", prime_list)
