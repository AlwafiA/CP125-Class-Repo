# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id score per line)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
    # TODO: Implement this function
    passline = []
    f = open("labs/lab08/exercise1/data/scores.txt", "r")
    lines = f.readlines()
    print(lines)
    for line in lines:
        if line >= 80:
            passline.append(line)
    return passline
        



# Test your code here
result = filter_passing_scores("data/scores.txt", "data/passing.txt")
print(f"Passing students: {result}")
