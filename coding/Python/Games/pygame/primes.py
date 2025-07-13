def is_prime(n, primes):
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False
    return True

def prime_generator():
    primes = []
    n = 2
    while True:
        if is_prime(n, primes):
            primes.append(n)
            yield n
        n += 1

# Example usage
gen = prime_generator()
count = 0
try:
    while True:
        prime = next(gen)
        count += 1
        print(f"{count}. {prime}")
except KeyboardInterrupt:
    print(f"Prime number generation stopped after {count} primes.")