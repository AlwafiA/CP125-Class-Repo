import os
import pandas as pd


def compare_averages(filename):
    if not os.path.isabs(filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.normpath(os.path.join(base_dir, filename))

    df = pd.read_csv(filename)

    subjects = ["Math", "Science", "English"]
    averages = {subject: float(round(df[subject].mean(), 1)) for subject in subjects}

    best_subject = max(averages, key=averages.get)
    worst_subject = min(averages, key=averages.get)

    return {
        **averages,
        "best_subject": best_subject,
        "worst_subject": worst_subject,
    }
