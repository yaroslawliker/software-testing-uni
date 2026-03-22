import unittest
from line import Line, GeometryError
from intersection import get_intersection

class TestGeometryApp(unittest.TestCase):

    # --- VALID TEST CASES ---

    def test_conversion_type2_points(self):
        """Verify Type 2 conversion: Line through (0,0) and (1,1) [cite: 112, 135]"""
        # (y2-y1)x + (x1-x2)y + (y1x2 - y2x1) = 0
        # (1-0)x + (0-1)y + (0*1 - 1*0) = 1x - 1y + 0 = 0
        l = Line.from_two_points(0, 0, 1, 1)
        self.assertAlmostEqual(l.A, 1.0)
        self.assertAlmostEqual(l.B, -1.0)
        self.assertAlmostEqual(l.C, 0.0)

    def test_conversion_type4_intercepts(self):
        """Verify Type 4 conversion: Intercepts a=2, b=4 """
        # (1/a)x + (1/b)y - 1 = 0 => (1/2)x + (1/4)y - 1 = 0
        l = Line.from_intercepts(2, 4)
        self.assertAlmostEqual(l.A, 0.5)
        self.assertAlmostEqual(l.B, 0.25)
        self.assertAlmostEqual(l.C, -1.0)

    def test_conversion_type6_normal(self):
        """Verify Type 6 conversion: Point (1,2), normal vector (3,4) """
        # a(x-x0) + b(y-y0) = 3(x-1) + 4(y-2) = 3x + 4y - 11 = 0
        l = Line.from_point_normal(1, 2, 3, 4)
        self.assertAlmostEqual(l.A, 3.0)
        self.assertAlmostEqual(l.B, 4.0)
        self.assertAlmostEqual(l.C, -11.0)

    def test_triangle_intersection(self):
        """Test Case 1: Three distinct intersection points (Triangle) [cite: 27, 52]"""
        l1 = Line.from_two_points(0, 0, 10, 0)
        l2 = Line.from_intercepts(10, 10)
        l3 = Line.from_point_normal(5, 0, 1, 0)
        
        intersections = {get_intersection(l1, l2), get_intersection(l1, l3), get_intersection(l2, l3)}
        # Expected: (10,0), (5,0), (5,5)
        self.assertIn((10.0, 0.0), intersections)
        self.assertIn((5.0, 0.0), intersections)
        self.assertIn((5.0, 5.0), intersections)

    def test_single_point_intersection(self):
        """Test Case 2: All three lines meet at a single point [cite: 25, 46]"""
        l1 = Line.from_two_points(0, 0, 2, 2)
        l2 = Line.from_intercepts(2, 2)
        l3 = Line.from_point_normal(1, 1, 1, 0)
        
        res12 = get_intersection(l1, l2)
        res13 = get_intersection(l1, l3)
        res23 = get_intersection(l2, l3)
        
        self.assertEqual(res12, (1.0, 1.0))
        self.assertEqual(res13, (1.0, 1.0))
        self.assertEqual(res23, (1.0, 1.0))

    def test_parallel_lines(self):
        """Test Case 3: Lines are parallel and do not intersect [cite: 24, 142]"""
        # Let's use simpler parallel lines for clear testing
        l1 = Line.from_two_points(0, 0, 1, 0) # y=0
        l2 = Line.from_point_normal(0, 5, 0, 1) # y=5
        
        self.assertEqual(get_intersection(l1, l2), "PARALLEL")

    def test_coinciding_lines(self):
        """Test Case 4: Lines coincide [cite: 23, 144]"""
        l1 = Line.from_two_points(0, 2, 2, 0)
        l2 = Line.from_intercepts(2, 2)
        
        self.assertEqual(get_intersection(l1, l2), "COINCIDE")

    def test_boundary_values_max(self):
        """Test Case 6: Right boundary of range [133, 133] [cite: 35, 71]"""
        l1 = Line.from_two_points(133, 0, 133, 1) # x=133
        l2 = Line.from_intercepts(133, 133)       # x+y=133
        res = get_intersection(l1, l2)
        self.assertEqual(res, (133.0, 0.0))


    # --- INVALID TEST CASES ---

    def test_invalid_points(self):
        """Test Case 8: Error when two points are identical [cite: 43, 113]"""
        with self.assertRaises(GeometryError):
            Line.from_two_points(5, 5, 5, 5)

    def test_invalid_intercepts(self):
        """Test Case 9: Error when intercept is zero [cite: 121]"""
        with self.assertRaises(GeometryError):
            Line.from_intercepts(0, 5)

    def test_invalid_normal_vector(self):
        """Test Case 10: Error when normal vector is zero [cite: 126]"""
        with self.assertRaises(GeometryError):
            Line.from_point_normal(1, 1, 0, 0)

if __name__ == '__main__':
    unittest.main()