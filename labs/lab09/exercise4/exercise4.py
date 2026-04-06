"""import pandas as pd
import matplotlib.pyplot as plt


def show_science_distribution(filename):
    # Load data
    df = pd.read_csv(filename)

    # Plot histogram of Science scores
    plt.hist(df['Science'], bins=10)

    plt.xlabel("Science Score")
    plt.ylabel("Frequency")
    plt.title("Science Score Distribution")

    plt.show()

count = show_science_distribution("labs\lab09\data\students.csv")
print(count)"""


import pandas as pd
import matplotlib.pyplot as plt

def show_science_distribution(filename):
    # Load data
    df = pd.read_csv(filename)

    # Plot histogram of Science scores
    plt.hist(df['Science'], bins=10)

    plt.xlabel("Science Score")
    plt.ylabel("Frequency")
    plt.title("Science Score Distribution")

    plt.show()

    # --- THE FIX IS HERE ---
    # Count the number of rows (students) and return it
    student_count = len(df)
    return student_count

# This will now print the number of students instead of 'None'
count = show_science_distribution("labs\lab09\data\students.csv")
print(count)
