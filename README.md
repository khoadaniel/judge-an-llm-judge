# Judge an LLM Judge


![LLM-judge judging LLM-judge](img/continuous_improvement_of_llm_judge.png)


## Introduction
This repository introduces a low-abstraction (no libraries) implementation of using an LLM-judge to evaluate another LLM-judge, a concept referred to as "LLM-judge judging LLM-judge".

This implementation focuses on the high-level concept without delving too deeply into the details. 
No LLM evaluation libraries. or platforms (e.g., LangChain, LangSmith, LangFuse, etc.) were used. The evaluation was simply parsed locally for the final conclusion. The code implementation has low abstraction, allowing readers to easily follow the workflow without getting lost in the intricate details of the setup.

## The experiment
We will assign roles for the components in the evaluation setup to make it easier to follow. Referring to LLM-judge and Supreme LLM-judge became confusing in the next part, so we will now call:

> - The LLM Application as The Student 
> - The LLM Judge as The Teacher (who grades the answers from The Student 
> - The Supreme LLM Judge as The Reviewer (who reviews the evaluation from the The Teacher for The Student).

## The metrics
We define that a positive case is when the evaluation of the Teacher is wrong.

- `recall_of_reviewer`: Recall measures the ability of the Reviewer to identify all the positive cases, where a positive case is an incorrect evaluation made by the Teacher. It indicates how effectively the Reviewer can capture these mistakes. The higher the recall, the more comprehensive the Reviewer is at detecting the Teacher's errors. Essentially, it reflects the Reviewer's thoroughness in identifying all instances of incorrect evaluations.

- `precision_of_reviewer`: Precision is defined as the proportion of the Reviewer's identified positive cases that are actually positive. In this context, a positive case is when the evaluation by the Teacher is incorrect. Precision measures the accuracy of the Reviewer in identifying these incorrect evaluations. It tells us how many of the cases flagged by the Reviewer as incorrect are genuinely incorrect. High precision indicates that the Reviewer is good at identifying actual mistakes in the Teacher's evaluations without many false positives.

## Try it out
Run the following commands to start the evaluation of the LLM judge:

```bash
python -m venv .venv
pytho
python evaluation.py
```


