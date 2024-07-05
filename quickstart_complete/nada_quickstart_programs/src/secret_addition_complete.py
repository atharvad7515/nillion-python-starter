from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Define secret integers for party1 (rectangle dimensions)
    length = SecretInteger(Input(name="length", party=party1))
    width = SecretInteger(Input(name="width", party=party1))

    # Define secret integers for party2 (cylinder dimensions)
    radius = SecretInteger(Input(name="radius", party=party2))
    height = SecretInteger(Input(name="height", party=party2))

    # Function to calculate area of a rectangle
    def rectangle_area(length, width):
        return length * width

    # Function to calculate volume of a cylinder
    def cylinder_volume(radius, height):
        pi = 3.141592653589793
        return pi * (radius ** 2) * height

    # Perform calculations
    rect_area = rectangle_area(length, width)
    cyl_volume = cylinder_volume(radius, height)

    # Return outputs
    return [
        Output(rect_area, "rect_area_output", party1),
        Output(cyl_volume, "cyl_volume_output", party2)
    ]
