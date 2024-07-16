# Judge an LLM Judge


![LLM-judge judging LLM-judge](img/continuous_improvement_of_llm_judge.png)


## Introduction
This repository introduces a low-abstraction (no libraries) implementation of using an LLM-judge to evaluate another LLM-judge, a concept referred to as "LLM-judge judging LLM-judge".

This implementation focuses on the high-level concept without delving too deeply into the details. 
No LLM evaluation libraries. or platforms (e.g., LangChain, LangSmith, LangFuse, etc.) were used. The code implementation has low abstraction, allowing readers to easily follow the workflow without getting lost in the intricate details of the setup.

## Research Question
Can "the evaluation of an LLM application by an LLM judge" be audited by another LLM judge for continous improvement?

## Experiment Design
An LLM Application is evaluated by an LLM Judge, whose judgment is afterward reviewed by a Supreme LLM Judge. Disagreements or anomalies are subsequently reviewed by a human.

We will assign roles for the components in the evaluation setup to make it easier to follow. Referring to LLM-judge and Supreme LLM-judge became confusing in the next part, so we will now call:

> - The LLM Application as The Student 
> - The LLM Judge as The Teacher (who grades the answers from The Student 
> - The Supreme LLM Judge as The Reviewer (who reviews the evaluation from the The Teacher for The Student).

<br>

#### The question we asked the LLM application:
In a group of 30 people who can speak either English or German, 10 can speak both, and 25 can speak German.
How many speak only English?

I ran this evaluation cycle 100 times (using the same question) to examine the accuracy of the judges.


## The metrics
We define that a positive case is when the evaluation of the Teacher is wrong.

- `recall_of_reviewer`: measures the ability of the Reviewer to identify all the positive cases. It indicates how effectively the Reviewer can capture these mistakes from the Teacher.

- `precision_of_reviewer`: is defined as the proportion of the Reviewer's identified positive cases that are actually positive.

<br>

```
reviewer_precision: 0.43
reviewer_recall: 0.70
```

> The Supreme LLM Judge can identify 70% of the instances where the LLM Judge made incorrect evaluations. By analyzing these identified cases, we can understand why the LLM Judge was confused and improve our LLM Application's evaluation process.

Below are examples where the Reviewer successfully identified the Teacher's grading errors. By looking into these examples, we can try to study why the LLM Judge did not perform well.

```
{
        "student_answer": "1. We know that there are 10 people who can speak both English and German.\n2. There are 25 people who can speak German.\n3. To find out how many speak only English, we need to subtract the number of people who can speak both English and German from the total number of people who can speak German.\n4. So, the number of people who speak only English is 25 (people who speak German) - 10 (people who speak both) = 15 people.\n5. Therefore, there are 15 people who speak only English in the group of 30 people.",
        "teacher_grading": "1",
        "reviewer_feedback": "0",
        "human_grading": "0"
    },
    {
        "student_answer": "To find out how many people speak only English, we first calculate the total number of people who can speak English by subtracting the number of people who can speak both English and German (10) from the total number of people who can speak German (25). This is because those 10 people are counted twice - once in the English-speaking group and once in the German-speaking group.\n\nTotal number of people who can speak English = Total number of people who can speak German - Number of people who can speak both English and German\nTotal number of people who can speak English = 25 - 10\nTotal number of people who can speak English = 15\n\nTherefore, there are 15 people who speak only English.",
        "teacher_grading": "1",
        "reviewer_feedback": "0",
        "human_grading": "0"
    },
    {
        "student_answer": "Given that 10 people can speak both English and German, and 25 people can speak German, it means that 25 - 10 = 15 people speak only German.\nSince there are 30 people in total and we have now found the number of people who speak only German, the number of people who speak only English is 30 - 15 - 10 = 5.\nTherefore, 5 people speak only English.",
        "teacher_grading": "0",
        "reviewer_feedback": "0",
        "human_grading": "1"
    },
    {
        "student_answer": "To find out how many people speak only English, we can start by calculating the total number of people who can speak English. \n\nFrom the information provided, we know that there are 10 people who can speak both English and German. Since there are a total of 30 people in the group, and 25 of them can speak German, the remaining 5 people must be the ones who speak only English.\n\nTherefore, the number of people who speak only English is 5.",
        "teacher_grading": "0",
        "reviewer_feedback": "0",
        "human_grading": "1"
    },
    {
        "student_answer": "To find out how many people speak only English, we will first subtract the total number of German speakers from the total number of people in the group:\n\nTotal number of people = 30\nNumber of German speakers = 25\n\nTherefore, the number of people who speak only English is:\n30 - 25 = 5\n\nSo, there are 5 people in the group who speak only English.",
        "teacher_grading": "0",
        "reviewer_feedback": "0",
        "human_grading": "1"
    },
```

<br>

#### About the human evaluator:
- Yes, I (the Author) am the human evaluator!
- In the context of this experiment, the human will grade the student's answers as correct if the reasoning is sound, even if it is lengthy and contains redundant calculations.
- Please note that this human_gradingis against the Student's answers.



## Try it out
Run the following commands to start the evaluation of the LLM judge:

```bash
python -m venv .venv
pytho
python evaluation.py
```


