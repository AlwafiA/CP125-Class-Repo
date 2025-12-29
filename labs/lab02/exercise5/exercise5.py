def is_valid_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c >a) :
        return True
    else : 
        return False





"""Situation: A geometry app needs a function to verify if three given line segments can physically form a triangle.

Rule: A triangle is valid only if the sum of any two sides is greater than the third side:

side1 + side2 > side3
side1 + side3 > side2
side2 + side3 > side1
Task: Write a function is_valid_triangle(a, b, c) that returns True if valid, False otherwise.

"""