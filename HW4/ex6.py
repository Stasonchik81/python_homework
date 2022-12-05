# quadratic_roots of the equation

def find_quadratic_roots (A: int, B: int, C: int) -> tuple:
    discr = B**2 - 4*A*C
    if discr < 0:
        return (None, None)
    elif discr > 0:
        return (round(((-B) - discr**0.5)/2*A, 2), round(((-B) + discr**0.5)/2*A, 2))
    else:
        return (-B/(2*A))

result = find_quadratic_roots(3, -15, 10)
print(result)