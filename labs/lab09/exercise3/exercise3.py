import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):
    # 1. Load CSV
    df = pd.read_csv(filename)

    # 2. Extract Math column
    math_scores = df["Math"]

    # 3. Create line chart
    plt.plot(df.index, math_scores)
    plt.xlabel("Student Index")
    plt.ylabel("Math Score")
    plt.title("Math Score Trends")

    # 4. Show the chart
    plt.show()

    # 5. Return number of students
    return len(df)


if __name__ == "__main__":
    count = show_math_trend("labs\lab09\data\students.csv")
    print(count)
