# Program to find prime numbers between 501 and 2000
# using the Sieve of Eratosthenes algorithm

def sieve_primes(low, high):
    n = high
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Mark non-prime numbers
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for k in range(p * p, n + 1, p):
                is_prime[k] = False
        p += 1

    # Print primes in the given range
    print(f"Prime numbers between {low} and {high} are:")
    for i in range(low, high + 1):
        if is_prime[i]:
            print(i, end=" ")

# Driver code
sieve_primes(501, 2000)
