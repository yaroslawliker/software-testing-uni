class GeometryError(Exception):
    pass

class Line:
    def __init__(self, a, b, c):
        # Check for invalid line coefficients A^2 + B^2 != 0 [cite: 104]
        if abs(a) < 1e-8 and abs(b) < 1e-8:
            raise GeometryError("Коефіцієнти A і B не можуть бути обидва нулем.")
        self.A = float(a)
        self.B = float(b)
        self.C = float(c)

    @classmethod
    def from_two_points(cls, x1, y1, x2, y2):
        """Type 2: Line through two points[cite: 112, 135]."""
        if abs(x1 - x2) < 1e-8 and abs(y1 - y2) < 1e-8:
            raise GeometryError("Точки не можуть бути однаковими.")
        A = y2 - y1
        B = x1 - x2
        C = y1 * x2 - y2 * x1
        return cls(A, B, C)

    @classmethod
    def from_intercepts(cls, a, b):
        """Type 4: Intercept form x/a + y/b = 1."""
        if abs(a) < 1e-8 or abs(b) < 1e-8:
            raise GeometryError("Значення a і b не можуть бути нулем.")
        # Transform to (1/a)x + (1/b)y - 1 = 0
        return cls(1/a, 1/b, -1)

    @classmethod
    def from_point_normal(cls, x0, y0, a, b):
        """Type 6: Point and normal vector a(x-x0) + b(y-y0) = 0[cite: 127]."""
        # A(x) + B(y) + (-A*x0 - B*y0) = 0
        return cls(a, b, -(a*x0 + b*y0))