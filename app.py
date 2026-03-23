from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent
STORAGE_DIR = BASE_DIR / "storage"
DATA_FILE = STORAGE_DIR / "data.json"

app = Flask(__name__, template_folder="templates", static_folder="static")


def ensure_storage():
    STORAGE_DIR.mkdir(exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("{}", encoding="utf-8")


def load_data() -> dict:
    ensure_storage()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def save_message(username: str, message: str) -> None:
    data = load_data()
    timestamp = str(datetime.now())
    data[timestamp] = {
        "username": username,
        "message": message
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/message")
def message():
    return render_template("message.html")


@app.route("/message", methods=["POST"])
def message_post():
    username = request.form.get("username", "").strip()
    message = request.form.get("message", "").strip()

    if username and message:
        save_message(username, message)

    return redirect(url_for("read_messages"))


@app.route("/read")
def read_messages():
    data = load_data()
    return render_template("read.html", messages=data)


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404


if __name__ == "__main__":
    ensure_storage()
    app.run(host="0.0.0.0", port=3000, debug=True)