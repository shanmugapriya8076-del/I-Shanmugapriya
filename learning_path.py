
import os
import google.generativeai as genai


def explain_topic(topic, student_level="beginner"):
    """
    Explain a topic in simple language using Gemini AI.
    """

    if not topic or not topic.strip():
        return "Please enter a topic to explain."

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
        You are EduGenie, an AI learning assistant.

        Explain the following topic to a student.

        Topic: {topic}
        Student level: {student_level}

        Instructions:
        1. Use simple English.
        2. Explain the concept step by step.
        3. Give one clear example.
        4. Include important points.
        5. End with a short summary.
        """

        response = model.generate_content(prompt)

        if response.text:
            return response.text

        return "Sorry, no explanation was generated."

    except Exception as error:
        return f"Unable to generate explanation: {error}"