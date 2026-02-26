import math

from line import Line
from intersection import get_intersection


def input_lines():
    print("--- Пряма 1 (Тип 2: Дві точки) ---")
    x1, y1 = map(float, input("Введіть x1 y1: ").split())
    x2, y2 = map(float, input("Введіть x2 y2: ").split())
    line1 = Line.from_two_points(x1, y1, x2, y2)

    print("\n--- Пряма 2 (Тип 4: Перетини) ---")
    a_int, b_int = map(float, input("Введіть a b: ").split())
    line2 = Line.from_intercepts(a_int, b_int)

    print("\n--- Пряма 3 (Тип 6: Точка та нормаль) ---")
    x0, y0 = map(float, input("Введіть x0 y0: ").split())
    norm_a, norm_b = map(float, input("Введіть нормаль a b: ").split())
    line3 = Line.from_point_normal(x0, y0, norm_a, norm_b)

    return [line1, line2, line3]


def calculate_intersections(lines):

    intersections = set()
    coincide_pairs = 0
    
    pairs = [(0, 1), (0, 2), (1, 2)]
    for i, j in pairs:
        res = get_intersection(lines[i], lines[j])
        if res == "COINCIDE":
            coincide_pairs += 1
        elif isinstance(res, tuple):
            intersections.add(res)

    return coincide_pairs, intersections


def print_intersections(coincide_pairs, intersections):
    # Output logic based on specification 
    if coincide_pairs > 0:
        print("Прямі співпадають")
    elif not intersections:
        print("Прямі не перетинаються")
    elif len(intersections) == 1:
        x, y = list(intersections)[0]
        print(f"Єдина точка перетину прямих (x0, y0), x0={x}, y0={y}")
    elif len(intersections) == 2:
        pts = sorted(list(intersections))
        print(f"Дві точки перетину прямих (x1,y1)={pts[0]}, (x2,y2)={pts[1]}")
    else:
        pts = sorted(list(intersections))
        print(f"Три точки перетину прямих (x1, y1), (x2, y2), (x3, y3)")
        for i, p in enumerate(pts, 1):
            print(f"x{i}={p[0]}, y{i}={p[1]}")

def print_error(e):
    print(f"Помилка: {e}")
    print("Рекомендовані дії: перевірте, чи не є точки однаковими та чи не дорівнюють відрізки/вектори нулю[cite: 44, 45].")


def main():
    try:
        lines = input_lines()
        concide_pairs, intersections = calculate_intersections(lines)    
        print_intersections(concide_pairs, intersections)            
    except Exception as e:
        print_error(e)
        


if __name__ == "__main__":
    main()