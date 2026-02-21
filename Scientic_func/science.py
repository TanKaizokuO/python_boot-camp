import math


# Basic mathematical functions
def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(n)


def fibonacci(n):
    """Generate first n Fibonacci numbers."""
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence[:n]


# Physics functions
def kinetic_energy(mass, velocity):
    """Calculate kinetic energy: KE = 0.5 * m * v^2."""
    return 0.5 * mass * velocity**2


def potential_energy(mass, gravity, height):
    """Calculate potential energy: PE = m * g * h."""
    return mass * gravity * height


def distance(velocity, time, acceleration=0):
    """Calculate distance: d = v*t + 0.5*a*t^2."""
    return velocity * time + 0.5 * acceleration * time**2


# Statistics functions
def mean(data):
    """Calculate mean of a list."""
    return sum(data) / len(data) if data else 0


def variance(data):
    """Calculate variance of a list."""
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data) if data else 0


def standard_deviation(data):
    """Calculate standard deviation."""
    return math.sqrt(variance(data))
