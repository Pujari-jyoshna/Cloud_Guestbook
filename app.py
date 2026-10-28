"""A beginner Flask guestbook that runs locally or in the cloud."""
import os

from flask import Flask, redirect, render_template_string, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
database_url = os.environ.get("DATABASE_URL", "sqlite:///guestbook.db")
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql+psycopg://", 1)
elif database_url.startswith("postgresql://"):
    database_url = database_url.replace("postgresql://", "postgresql+psycopg://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(300), nullable=False)


PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cloud Guestbook</title>
<style>
body {font-family:Arial,sans-serif;max-width:680px;margin:40px auto;padding:0 18px;color:#182230;background:#f4f7fb}
h1 {color:#174a7e} form,.message {background:white;padding:18px;margin:16px 0;border-radius:10px;box-shadow:0 2px 8px #00000012}
label {display:block;margin-top:12px;font-weight:bold} input,textarea {box-sizing:border-box;width:100%;padding:10px;margin-top:5px;font:inherit}
button {margin-top:14px;padding:10px 16px;color:white;background:#1769aa;border:0;border-radius:6px;cursor:pointer}
small {color:#526273}
</style></head><body>
<h1>Cloud Guestbook</h1><p>Write a message. It is saved in the app's database.</p>
<form method="post" action="{{ url_for('add_message') }}">
<label for="name">Your name</label><input id="name" name="name" maxlength="50" required>
<label for="text">Your message</label><textarea id="text" name="text" maxlength="300" rows="3" required></textarea>
<button type="submit">Post message</button></form>
<h2>Messages ({{ messages|length }})</h2>
{% for message in messages %}<article class="message"><strong>{{ message.name }}</strong><br><p>{{ message.text }}</p></article>
{% else %}<p>No messages yet. Add the first one!</p>{% endfor %}
<small>Beginner project: Flask web app + cloud hosting + PostgreSQL.</small>
</body></html>"""


@app.route("/")
def home():
    messages = Message.query.order_by(Message.id.desc()).all()
    return render_template_string(PAGE, messages=messages)


@app.route("/add", methods=["POST"])
def add_message():
    name = request.form.get("name", "").strip()
    text = request.form.get("text", "").strip()
    if name and text:
        db.session.add(Message(name=name[:50], text=text[:300]))
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/healthz")
def health():
    return {"status": "ok"}


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
