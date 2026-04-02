import pandas as pd


def explore_data(filename):
    # 1. Load CSV into DataFrame
    df = pd.read_csv(filename)

    # 2. Calculate required statistics
    total_students = len(df)

    subjects = [col for col in ["Math", "Science", "English"] if col in df.columns]

    math_average = round(df["Math"].mean(), 1)

    highest_math_student = df.loc[df["Math"].idxmax(), "Name"]

    # 3. Return results dictionary
    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student,
    }


if __name__ == "__main__":
    result = explore_data("data/students.csv")
    print(result)
