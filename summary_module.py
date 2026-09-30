
import os
import google.generativeai as genai


def summarize_text(text, summary_length="medium"):
    """Summarize study material using Gemini AI."""

    if not text or not text.strip():
        return "Please enter some text to summarize."

    length_options = {
        "short": "Write a very short summary in 3-5 bullet points.",
        "medium": "Write a clear summary with the main ideas and key points.",
        "long": "Write a detailed summary with headings and important details."
    }

    summary_length = summary_length.lower().strip()

    if summary_length not in length_options:
        summary_length = "medium"

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
        You are EduGenie, an educational learning assistant.

        Summarize the following study material.

        Instructions:
        - Use simple English.
        - Preserve the important facts and meaning.
        - Do not add unsupported information.
        - Highlight important concepts and keywords.
        - Organize the result clearly.

        Summary style: {length_options[summary_length]}

        Study material:
        {text}
        """

        response = model.generate_content(prompt)

        if response.text:
            return response.text

        return "No summary was generated. Please try again."

    except Exception as error:
        return f"Unable to summarize the text: {error}"


if __name__ == "__main__":
    print("=== EduGenie Text Summarizer ===")

    study_text = input("Enter the text to summarize: ")
    length = input("Summary length (short/medium/long): ")

    result = summarize_text(study_text, length or "medium")

    print("\n=== Summary ===\n")
    print(result)