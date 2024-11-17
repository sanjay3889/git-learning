def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage:
start_range = 10
end_range = 50
prime_numbers = find_primes_in_range(start_range, end_range)
print(f"Prime numbers between {start_range} and {end_range}: {prime_numbers}")
