import math

def calculate_area(shape, *args):
    shape = shape.lower()
    
    formulas = {
        "c": lambda r: math.pi * r**2 if r > 0 else None,  # Circle
        "s": lambda a: a**2 if a > 0 else None,           # Square
        "r": lambda l, w: l * w if l > 0 and w > 0 else None,  # Rectangle
        "t": lambda b, h: 0.5 * b * h if b > 0 and h > 0 else None  # Triangle
    }

    area = formulas.get(shape, lambda *args: None)(*args)
    
    return f"Area: {area:.2f}" if area is not None else "Invalid shape or parameters"

# Test the Function
print(calculate_area("c", 8))
print(calculate_area("s", 7))
print(calculate_area("r", 2, 12))
print(calculate_area("t", 4, 8))
print(calculate_area("c", -5))   # Invalid case
print(calculate_area("x", 5))    # Invalid shape
