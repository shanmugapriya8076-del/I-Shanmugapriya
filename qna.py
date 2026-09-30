
import os
import google.generativeai as genai


def answer_question(question, student_level="beginner"):
    """Answer a student's question using Gemini AI."""

    if not question or not question.strip():
        return "Please enter a question."

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return (
            "Gemini API key is not configured. "
            "Please set the GEMINI_API_KEY environment variable."
        )

    try:
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
        You are EduGenie, a friendly AI learning assistant.

        Student question: {question}
        Student level: {student_level}

        Instructions:
        1. Answer the question clearly.
        2. Use simple English suitable for the student's level.
        3. Explain the answer step by step.
        4. Give an example when useful.
        5. Highlight important points.
        6. If the question is unclear, ask for clarification.
        """

        response = model.generate_content(prompt)

        if response.text:
            return response.text

        return "Sorry, no answer was generated. Please try again."

    except Exception as error:
        return f"Unable to answer your question: {error}"


if __name__ == "__main__":
    question = input("Enter your question: ")
    level = input("Enter your level (beginner/intermediate/advanced): ")

    answer = answer_question(question, level or "beginner")

    print("\nEduGenie Answer:\n")
    print(answer)