import json
import csv
import pandas as pd


def extract_metrics(file_path: str):

    # Read the JSON file
    with open(file_path, "r") as file:
        data = json.load(file)

    # Extract the required fields
    extracted_data = []
    for entry in data:
        extracted_data.append({
            "teacher_grading": entry.get("teacher_grading", None),
            "reviewer_feedback": entry.get("reviewer_feedback", None),
            "human_grading": entry.get("human_grading", None)
        })

    # Turn the list into a pandas DataFrame
    df = pd.DataFrame(extracted_data)

    # Insert new column accuracy_of_teacher_grading: 1 if teacher_grading == human_grading, 0 otherwise
    df['accuracy_of_teacher_grading'] = df.apply(
        lambda row: 1 if row['teacher_grading'] == row['human_grading'] else 0, axis=1
    )

    # Insert new column accuracy_of_reviewer_feedback
    df['accuracy_of_reviewer_feedback'] = df.apply(
        lambda row: 1 if (row['reviewer_feedback'] == '1' and row['teacher_grading'] == row['human_grading']) or
        (row['reviewer_feedback'] == '0' and row['teacher_grading'] != row['human_grading']) else 0, axis=1
    )

    # Save the DataFrame to a CSV file
    csv_file = 'processed_metrics.csv'
    df.to_csv(csv_file, index=False)
    print(df)
