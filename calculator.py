#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Jan 20 2022
# This program uses a function to calculate
# either the surface area of a cube, ther surface
# area of a rectangular prism or the volume of
# a cone (user's choice).
import math


# calculate sa of cube
def calc_cube(side):
    sa_cube = 6 * side ** 2
    return sa_cube


# calculate the sa of rectangular prism
def calc_prism(length, width, height):
    sa_prism = 2 * (length * width + length * height + height * width)
    return sa_prism


# calculate the volume of a cone
def calc_cone(radius, height):
    volume_cone = math.pi * (radius ** 2) * height / 3
    return volume_cone


def main():
    # get input
    print("What would you like to calculate?")
    print("Enter 1 for the surface area of a cube.")
    print("Enter 2 for the surface area of a rectangular prism")
    print("Enter 3 for the volume of a cone.")
    user_choice = input("Enter your choice: ")

    # choose function
    # for cube
    if user_choice == "1":
        # get side length
        side_string = input("Enter the side length of the cube(cm): ")
        # error checking
        try:
            side_input = float(side_string)
            # call function
            answer = calc_cube(side_input)
            # display results
            print("The surface area is {} cm squared.". format(answer))
        except Exception:
            print("Invalid input")
    # for rectangular prism
    elif user_choice == "2":
        # get width, length and height of rectangular prism
        length_string = input("Enter the length of the prism(cm): ")
        width_string = input("Enter the width of the prism(cm): ")
        height_string = input("Enter the height of the prism(cm): ")
        # error checking
        try:
            length_input = float(length_string)
            width_input = float(width_string)
            height_input = float(height_string)
            # call function
            answer = calc_prism(length_input, width_input, height_input)
            # display results
            print("The surface area is {} cm squared.". format(answer))
        except Exception:
            print("Invalid input(s).")
    # for cone
    elif user_choice == "3":
        # get radius and height
        radius_string = input("Enter the radius of the cone(cm): ")
        height_string_cone = input("Enter the height of the cone(cm): ")
        # error checking
        try:
            radius_input = float(radius_string)
            height_input_cone = float(height_string_cone)
            # call function
            answer = calc_cone(radius_input, height_input_cone)
            # display results
            print("The volume is {} cm cubed.". format(answer))
        except Exception:
            print("Invalid input(s).")
    # error checking
    else:
        print("Invalid input.")


if __name__ == "__main__":
    main()
