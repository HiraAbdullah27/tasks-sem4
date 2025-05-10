from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
API_TOKEN = os.getenv("HF_API_KEY")

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()  # Raise error for unauthorized or failed requests
    return response.json()

@app.route("/", methods=["GET", "POST"])
def index():
    story_output = ""
    if request.method == "POST":
        story_input = request.form.get("story_input", "").strip()
        genre = request.form.get("genre", "")
        tone = request.form.get("tone", "")
        setting = request.form.get("setting", "")
        characters = request.form.get("characters", "")

        if not story_input:
            story_output = "⚠️ Please provide a story starter!"
        else:
            prompt = (
                f"Write a {tone} {genre} story set in {setting}, involving {characters}. "
                f"Start the story with: {story_input}"
            )
            try:
                response = query({"inputs": prompt})
                story_output = response[0]["generated_text"]
            except requests.exceptions.RequestException as e:
                story_output = f"❌ Error: {str(e)}"

    return render_template("index.html", story_output=story_output)

if __name__ == "__main__":
    app.run(debug=True)
