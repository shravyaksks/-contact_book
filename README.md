```markdown
# 📒 Contact Book (Flask)

A simple web-based **Contact Book** built with Flask. This app allows you to add, search, and delete contacts, with data stored in JSON format.

---

## 📂 Project Structure
```
contact_book/
│
├── contact_app.py              # Main Flask application
├── data/
│   └── contacts.json           # Stores contact information
├── static/
│   └── style.css               # Styling for the app
├── templates/
│   ├── contacts_index.html     # Home page (list contacts)
│   ├── add_contact.html        # Add new contact
│   ├── search_contact.html     # Search contact
│   └── delete_contact.html     # Delete contact
```

---

## 🚀 Features
- Add new contacts with name and phone number
- Search for contacts by name
- Delete existing contacts
- Persistent storage in JSON file
- Clean UI with styled forms and tables

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/shravyaksks/contact_book.git
   cd contact_book
   ```

2. **Create a virtual environment (optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Run the application**
   ```bash
   python contact_app.py
   ```

5. Open your browser at:
   ```
   http://127.0.0.1:5000
   ```

---

## 📸 Screenshots
- **Home Page**: View all contacts.
- **Add Contact**: Add new entries.
- **Search Contact**: Find contacts by name.
- **Delete Contact**: Remove contacts easily.

---

## 🛠️ Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS (Jinja2 templates)
- **Data Storage**: JSON file

---

## 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss.

---

## 📜 License
This project is licensed under the MIT License.
```

---

👉 Save this as `README.md`, then commit and push:

```bash
git add README.md
git commit -m "Add README.md with project details"
git push
```
