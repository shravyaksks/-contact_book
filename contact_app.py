from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)

DATA_FILE = "data/contacts.json"
os.makedirs("data", exist_ok=True)

# Load contacts from file
def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

@app.route("/")
def home():
    contacts = load_contacts()
    return render_template("contacts_index.html", contacts=contacts)

@app.route("/add", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        contacts = load_contacts()
        contacts.append({"name": name, "phone": phone})
        save_contacts(contacts)
        return redirect(url_for("home"))
    return render_template("add_contact.html")

@app.route("/search", methods=["GET", "POST"])
def search_contact():
    result = None
    if request.method == "POST":
        name = request.form["name"].lower()
        contacts = load_contacts()
        for c in contacts:
            if c["name"].lower() == name:
                result = c
                break
    return render_template("search_contact.html", result=result)

@app.route("/delete", methods=["GET", "POST"])
def delete_contact():
    message = None
    if request.method == "POST":
        name = request.form["name"].lower()
        contacts = load_contacts()
        for c in contacts:
            if c["name"].lower() == name:
                contacts.remove(c)
                save_contacts(contacts)
                message = f"Deleted {name}"
                break
        else:
            message = "Not found"
    return render_template("delete_contact.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)