import math

def solution(a: float, b: float, c: float):
    """
    Solves a quadratic equation of the form: a * x^2 + b * x + c = 0.
    Returns the roots in ascending order or None if no real roots exist.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0 for a quadratic equation.")
    
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return tuple(sorted((root1, root2)))

# Example usage
if __name__ == "__main__":
    print(solution(1, 6, 5))  # Output: (-5, -1)
    print(solution(1, 4, 4))  # Output: (-2,)
    print(solution(1, 6, 45)) # Output: None
