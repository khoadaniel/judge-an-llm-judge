import json
from src import evaluate
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    context = "In a group of 30 people who can speak either English or German, 10 can speak both, and 25 can speak German."
    user_question = "How many speak only English?"

    list_results = []
    for i in range(100):
        print(f"===> Iteration {i+1}")
        list_results.append(evaluate(context, user_question))

    # Save the results to a JSON file
    with open("outputs/evaluation_results.json", "w") as json_file:
        json.dump(list_results, json_file, indent=4)
