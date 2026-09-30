
import os
import google.generativeai as genai


def generate_quiz(topic, number_of_questions=5, student_level="beginner"):
    """Generate a multiple-choice quiz using Gemini AI."""

    if not topic or not topic.strip():
        return "Please enter a topic for the quiz."

    try:
        number_of_questions = int(number_of_questions)
        if not 1 <= number_of_questions <= 20:
            return "Please choose between 1 and 20 questions."
    except (TypeError, ValueError):
        return "The number of questions must be a valid integer."

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
        You are EduGenie, an educational quiz assistant.

        Topic: {topic}
        Student level: {student_level}
        Number of questions: {number_of_questions}

        Create exactly {number_of_questions} multiple-choice questions.

        For each question, provide:
        1. The question
        2. Four options labelled A, B, C, D
        3. The correct answer
        4. A short explanation

        Use clear, simple English.
        Keep questions appropriate for the student's level.
        Number each question.
        """

        response = model.generate_content(prompt)

        if response.text:
            return response.text

        return "No quiz was generated. Please try again."

    except Exception as error:
        return f"Unable to generate quiz: {error}"


if __name__ == "__main__":
    topic = input("Enter a quiz topic: ")
    level = input("Enter your level (beginner/intermediate/advanced): ")
    count = input("How many questions? (1-20): ")

    quiz = generate_quiz(topic, count or 5, level or "beginner")

    print("\nEduGenie Quiz\n")
    print(quiz)