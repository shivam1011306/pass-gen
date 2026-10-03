# Password Generator Mini Project

## Technologies
- Programming language: Python
- Web framework: Flask
- Frontend: HTML + CSS + JavaScript
- Database: SQLite
- Editor: VS Code / PyCharm / any text editor

## Features
1. Generate random passwords from 4–64 characters.
2. Choose uppercase, lowercase, numbers and symbols.
3. Password strength indicator.
4. Copy password to clipboard.
5. Store the last generated passwords in SQLite.
6. View recent password history.

## How to run

### 1. Create a virtual environment
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Flask
```bash
pip install -r requirements.txt
```

### 3. Run the project
```bash
python app.py
```

### 4. Open in browser
Go to:
`http://127.0.0.1:5000`

The `passwords.db` SQLite database is created automatically.
