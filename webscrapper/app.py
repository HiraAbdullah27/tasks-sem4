from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re
import csv
import os

app = Flask(__name__)
DB_FILE = "db2.csv"

def extract_emails_from_url(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/113.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, text)
        return sorted(set(emails))
    except requests.exceptions.RequestException as e:
        return [f"Error: {str(e)}"]

def save_to_csv(company, url, emails):
    file_exists = os.path.isfile(DB_FILE)
    with open(DB_FILE, "a", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Company", "URL", "Emails"])
        writer.writerow([company, url, ", ".join(emails)])

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        company = request.form.get("company", "").strip()
        url = request.form.get("url", "").strip()

        if not company or not url:
            results = [["⚠️ Missing input", "", ""]]
        else:
            emails = extract_emails_from_url(url)
            save_to_csv(company, url, emails)
            results = [[company, url, emails]]

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
