import math


def calculate_triangle_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area


def main():
    # Prompt the user for input
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    # Calculate and print the area
    area = calculate_triangle_area(a, b, c)
    print(f"The area of the triangle is: {area:.2f}")


if __name__ == "__main__":
    main()
