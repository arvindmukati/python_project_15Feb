import math


def volume_of_sphere(radius):
    return (4 / 3) * math.pi * radius * radius * radius


def volume_of_cylinder(radius, height):
    return math.pi * radius * radius * height


def volume_of_cuboid(length, breadth, height):
    return length * breadth * height


def volume_of_hemisphere(radius):
    return (2/3) * math.pi * radius * radius * radius
