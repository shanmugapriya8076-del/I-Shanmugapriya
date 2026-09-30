
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi import Request
from html import escape

from explanation_module import explain_topic
from learning_path import generate_learning_path

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>EduGenie AI</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #eef2ff;
                margin: 0;
                padding: 30px 15px;
                color: #20254a;
            }
            .container {
                max-width: 750px;
                margin: auto;
            }
            .card {
                background: white;
                padding: 25px;
                margin: 18px 0;
                border-radius: 16px;
                box-shadow: 0 4px 15px #0001;
            }
            h1 { color: #5145cd; text-align: center; }
            p { line-height: 1.6; }
            input, select, button {
                box-sizing: border-box;
                width: 100%;
                padding: 12px;
                margin: 8px 0;
                border-radius: 8px;
                border: 1px solid #ccd0e0;
                font-size: 16px;
            }
            button {
                background: #5145cd;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover { background: #3930a5; }
            .subtitle { text-align: center; }
        </style>
    </head>
    <body>
      <div class="container">
        <h1>🎓 EduGenie AI</h1>
        <p class="subtitle">Google Gemini Powered Learning Assistant</p>

        <div class="card">
          <h2>📚 Explain a Topic</h2>
          <form action="/explain" method="post">
            <input name="topic" placeholder="Enter a topic to learn"
                   required>
            <select name="level">
              <option value="beginner">Beginner</option>
              <option value="intermediate">Intermediate</option>
              <option value="advanced">Advanced</option>
            </select>
            <button type="submit">Explain Topic</button>
          </form>
        </div>

        <div class="card">
          <h2>🗺️ Create a Learning Path</h2>
          <form action="/learning-path" method="post">
            <input name="topic" placeholder="What do you want to learn?"
                   required>
            <select name="level">
              <option value="beginner">Beginner</option>
              <option value="intermediate">Intermediate</option>
              <option value="advanced">Advanced</option>
            </select>
            <button type="submit">Generate Learning Path</button>
          </form>
        </div>
      </div>
    </body>
    </html>
    """


def result_page(title, result):
    safe_title = escape(title)
    safe_result = escape(str(result))

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{safe_title} - EduGenie</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          background: #eef2ff;
          padding: 25px 15px;
          line-height: 1.7;
        }}
        main {{
          max-width: 800px;
          margin: auto;
          background: white;
          padding: 25px;
          border-radius: 14px;
        }}
        pre {{
          white-space: pre-wrap;
          overflow-wrap: anywhere;
          font-family: Arial, sans-serif;
        }}
        a {{ color: #5145cd; }}
      </style>
    </head>
    <body>
      <main>
        <h1>{safe_title}</h1>
        <pre>{safe_result}</pre>
        <a href="/">← Back to EduGenie</a>
      </main>
    </body>
    </html>
    """


@app.post("/explain", response_class=HTMLResponse)
def explain(topic: str = Form(...), level: str = Form("beginner")):
    result = explain_topic(topic, level)
    return result_page("Topic Explanation", result)


@app.post("/learning-path", response_class=HTMLResponse)
def learning_path(topic: str = Form(...), level: str = Form("beginner")):
    result = generate_learning_path(topic, level)
    return result_page("Your Learning Path", result)


@app.get("/health")
def health():
    return {
        "status": "running",
        "project": "EduGenie",
        "version": "1.0.0"
    }