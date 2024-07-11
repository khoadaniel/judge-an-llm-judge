from openai import OpenAI
from src.prompts import llm_app_prompt, llm_judge_prompt, supreme_llm_judge_prompt


openai_client = OpenAI()


# LLM-app
def trigger_llm_app(context: str, question: str):
    fmt_context_and_question = f"""Context: {context}\nQuestion: {question}"""
    messages = [
        llm_app_prompt,

        {"role": "user",
         "content": fmt_context_and_question}
    ]
    response = openai_client.chat.completions.create(messages=messages,
                                                     model="gpt-3.5-turbo")
    return response.choices[0].message.content


# LLm judge
def eval_llm_app(context: str, question: str, predicted_answer: str):
    fmt_input = f"""Context: {context}\nQuestion: {
        question}\nStudent's Answer: {predicted_answer}"""
    messages = [
        llm_judge_prompt,
        {"role": "user",
         "content": fmt_input}
    ]

    response = openai_client.chat.completions.create(messages=messages,
                                                     model="gpt-3.5-turbo")
    return response.choices[0].message.content


# Superior LLM judge
def eval_llm_judge(context: str, question: str, student_answer: str, teacher_grading: str):
    fmt_input = f"""Context: {context}\nQuestion: {question}\nStudent's Answer: {
        student_answer}\nTeacher's Grading: {teacher_grading}"""
    messages = [
        supreme_llm_judge_prompt,
        {"role": "user",
         "content": fmt_input}
    ]

    response = openai_client.chat.completions.create(messages=messages,
                                                     model="gpt-4")
    return response.choices[0].message.content


# Helper function to parse the outputs
def evaluate(context: str, question: str):
    student_answer = trigger_llm_app(context, question)
    teacher_grading = eval_llm_app(context, question, student_answer)
    reviewer_feedback = eval_llm_judge(
        context, question, student_answer, teacher_grading)

    print(f"\nStudent's Answer:\n {student_answer}")
    print(f"\nTeacher's grading:\n {teacher_grading}")
    print(f"\nReviewer's Feedback:\n {reviewer_feedback}")

    # create a dictionary to store the results
    try:
        results = {
            "student_answer": student_answer,
            "teacher_grading": teacher_grading.split(":")[1].strip(),
            "reviewer_feedback": reviewer_feedback.split(":")[1].strip(),
        }
    except:
        results = {
            "student_answer": None,
            "teacher_grading": None,
            "reviewer_feedback": None,
        }
        print("==> Reviewer feedback is not in the correct format.")
    return results
