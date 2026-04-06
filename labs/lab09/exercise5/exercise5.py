import pandas as pd

def high_performers(filename):
    """
    Identifies students who scored above 85 in all subjects.

    Parameters:
        filename (str): Path to the CSV file containing student data.

    Returns:
        dict: A dictionary with:
            - "count" (int): Number of high performers
            - "names" (set): Set of high-performing student names
    """
    # 1. Load CSV
    df = pd.read_csv(filename)

    # 2. Filter rows where ALL subject scores are above 85
    subject_cols = ["Math", "Science", "English"]
    mask = (df[subject_cols] > 85).all(axis=1)
    top_students = df[mask]

    # 3. Build and return result
    return {
        "count": len(top_students),
        "names": set(top_students["Name"])
    }


if __name__ == "__main__":
    result = high_performers("labs\lab09\data\students.csv")
    print(result)
