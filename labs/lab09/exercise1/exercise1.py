import os
import pandas as pd


def explore_data(filename):
    if not os.path.isabs(filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.normpath(os.path.join(base_dir, filename))

    df = pd.read_csv(filename)

    total_students = len(df)
    subjects = [col for col in ["Math", "Science", "English"] if col in df.columns]
    math_average = float(round(df["Math"].mean(), 1))
    highest_math_student = df.loc[df["Math"].idxmax(), "Name"]

    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student,
    }