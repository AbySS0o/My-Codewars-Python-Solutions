from math import sin, pi


def area_of_inscribed_polygon(circle_radius, number_of_sides):
    # Area = 0.5 * n * R^2 * sin(2π/n);
    # n = number_of_sides, R = circle_radius;
    # Math module to calculate sin

    sinus = (sin(2 * pi)/number_of_sides)
    area = 0.5 * number_of_sides * circle_radius**2 * sinus
    return area

# lambda func solution :D

# from math import sin, pi
# area_of_inscribed_polygon = lambda r, n: 0.5 * n * r**2 * sin((pi*2)/n)
