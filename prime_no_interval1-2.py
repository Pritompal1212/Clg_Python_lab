# display all prime numbers within an interval

def primes_in_interval(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:  # Primes are greater than 1
            for i in range(2, num):
                if num % i == 0:
                    break  # Not a prime number
            else:
                primes.append(num)  # Append if no divisors were found
    return primes

# Example usage
start = 10
end = 50

prime_numbers = primes_in_interval(start, end)
print(f"Prime numbers between {start} and {end}: {prime_numbers}")
