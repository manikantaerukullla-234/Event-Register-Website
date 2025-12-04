from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def db():
    return sqlite3.connect("events.db")

@app.route("/")
def home():
    conn = db()
    events = conn.execute("SELECT * FROM events").fetchall()
    conn.close()
    return render_template("index.html", events=events)

@app.route("/register/<int:event_id>", methods=["GET", "POST"])
def register(event_id):
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        conn = db()
        conn.execute("INSERT INTO registrations (name, email, event_id) VALUES (?, ?, ?)",
                     (name, email, event_id))
        conn.commit()
        conn.close()

        return "Registration successful!"

    return render_template("register.html")
if __name__ == "__main__":
    app.run(debug=True)

