
def get_intersection(l1, l2):
    """Calculates intersection using Cramer's rule."""
    eps = 1e-8
    det = l1.A * l2.B - l2.A * l1.B
    
    if abs(det) < eps:
        # Check for coincidence using proportional coefficients [cite: 144]
        # Using cross-multiplication to avoid division by zero
        if abs(l1.A * l2.C - l2.A * l1.C) < eps and abs(l1.B * l2.C - l2.B * l1.C) < eps:
            return "COINCIDE"
        return "PARALLEL"
    
    x = -(l1.C * l2.B - l2.C * l1.B) / det
    y = -(l1.A * l2.C - l2.A * l1.C) / det
    return (round(x, 8), round(y, 8))