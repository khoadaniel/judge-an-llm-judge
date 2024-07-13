import json
import csv
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score

def compute_metrics(file_path: str):


    # Read the JSON file
    with open(file_path, "r") as file:
        data = json.load(file)

    # Extract the required fields
    extracted_data = []
    for entry in data:
        try:
            extracted_data.append({
                "teacher_grading": int(entry.get("teacher_grading", None)),
                "reviewer_feedback": int(entry.get("reviewer_feedback", None)),
                "human_grading": int(entry.get("human_grading", None))
            })
        except Exception as e:
            print(f"PLease check the evaluation file again. Error: {e}")
            print(f"Entry with the error: {entry}")
            continue



    # Turn the list into a pandas DataFrame
    df = pd.DataFrame(extracted_data)


    # Insert new column is_teacher_grading_correct: 1 if teacher_grading == human_grading, 0 otherwise
    df['is_teacher_grading_correct'] = df.apply(
        lambda row: 1 if row['teacher_grading'] == row['human_grading'] else 0, axis=1
    )

    # Insert new column is_reviewer_feedback_correct:
    df['is_reviewer_feedback_correct'] = df.apply(
        lambda row: 1 if (row['reviewer_feedback'] == 1 and row['teacher_grading'] == row['human_grading']) or
        (row['reviewer_feedback'] == 0 and row['teacher_grading'] != row['human_grading']) else 0, axis=1
    )

    # Confusion matrix
    # Let's copy the column "reviewer_feedback" to a new column "prediction"
    df['prediction'] = df['reviewer_feedback']
    # Let's copy the column "is_teacher_grading_correct" (yes, teacher not reviewer) to a new column "ground_truth"
    df['ground_truth'] = df['is_teacher_grading_correct']

    # Consider that a teacher's grading of zero (0) is a possitive case, while a grading of one (1) is a negative case
    cm = confusion_matrix(df['ground_truth'], df['prediction'])
    TP = cm[0, 0]  # True Positives
    FN = cm[0, 1]  # False Negatives
    FP = cm[1, 0]  # False Positives
    TN = cm[1, 1]  # True Negatives
    print(f"True Positives: {TP}; False Negatives: {FN}; False Positives: {FP}; True Negatives: {TN}")

    # Calculate Precision, Recall, and F1 Score with prediction=0 as the positive class
    precision = precision_score(df['ground_truth'], df['prediction'], pos_label=0)
    recall = recall_score(df['ground_truth'], df['prediction'], pos_label=0)
    f1 = f1_score(df['ground_truth'], df['prediction'], pos_label=0)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1}")

    
    # Calculate summary metrics
    accuracy_of_teacher = df['is_teacher_grading_correct'].mean()
    accuracy_of_reviewer = df['is_reviewer_feedback_correct'].mean()
    # Double check (recall): Out of all the cases where the teacher grading is incorrect, what proportion of them did the reviewer feedback catch?
    good_catch_by_reviewer = df[(df['is_reviewer_feedback_correct'] == 1) & (df['is_teacher_grading_correct'] == 0)].shape[0] / df[df['is_teacher_grading_correct'] == 0].shape[0]
    
                                                                                                            
    print(f"Accuracy of Teacher Grading: {accuracy_of_teacher}")
    print(f"Accuracy of Reviewer Feedback: {accuracy_of_reviewer}")
    print(f"Good Catch by Reviewer: {good_catch_by_reviewer}")


    # Save the DataFrame to a CSV file
    csv_file = 'outputs/metrics.csv'
    df.to_csv(csv_file, index=False)
    print(df)
