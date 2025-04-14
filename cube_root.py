import math
import time

# ================== CUBE ROOT ==================
def cube_root(n, epsilon=1e-6):
    """Compute cube root with Newton-Raphson method"""
    if n == 0: 
        return (0, 0)
    
    negative = n < 0
    n = abs(n)
    guess = n / 3.0
    step = 0
    
    while True:
        step += 1
        new_guess = (2 * guess + n / (guess * guess)) / 3
        if abs(new_guess - guess) < epsilon: 
            break
        guess = new_guess
    
    return (-new_guess if negative else new_guess, step)

# ================== PRIME CHECK ==================
def is_prime(n):
    """Optimized prime check"""
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0: 
            return False
        i += w
        w = 6 - w
    return True

# ================== DEMO EXECUTION ==================
print("\n=== CUBE ROOT DEMO ===")
num = -27
root, steps = cube_root(num)
print(f"Cube root of {num} = {root:.2f} (took {steps} steps)")

print("\n=== PRIME CHECK DEMO ===")
print("Primes under 20:", [n for n in range(20) if is_prime(n)])
print("Sum of primes 3-1000:", sum(n for n in range(3, 1001) if is_prime(n)))

# ================== EGG DROP PROBLEM ==================
print("\n=== EGG DROP SOLUTION ===")
def egg_drop(floors=102, eggs=7):
    attempts = 0
    floor = 0
    increment = floors // eggs
    
    while eggs > 1 and floor <= floors:
        attempts += 1
        floor += increment
        print(f"Drop egg from floor {floor} (Attempt {attempts})")
        if floor >= 50:  # Assume break point is 50
            print("Egg broke! Reducing search range")
            eggs -= 1
            floor -= increment
            increment = 1
    
    while floor <= floors:
        attempts += 1
        floor += 1
        print(f"Final egg drop from floor {floor} (Attempt {attempts})")
        if floor >= 50:
            print(f"Critical floor found: {floor-1}")
            break

egg_drop()