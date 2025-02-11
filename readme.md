# Celebrity Search Project

This is a Flask-based web application that allows users to search for celebrities and get relevant information including:

- ✅ **Basic details** about the celebrity
- ✅ **Date of birth**
- ✅ **Major world events** around their birth year

## Technologies Used

- 🔹 **Cohere API** for generating responses
- 🔹 **Flask** for backend functionality
- 🔹 **HTML, CSS, and JavaScript** for the frontend

## Features

- 🔹 Simple and clean UI for searching celebrities
- 🔹 Fetches historical events based on the celebrity's birth year
- 🔹 Conversational memory using LangChain for improved responses

## Installation & Setup

Clone the repository:

```bash
git clone https://github.com/your-username/celebrity-search.git
cd celebrity-search
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up the Cohere API Key in your environment:

```bash
export COHERE_API_KEY="your_api_key"
```

_For Windows PowerShell:_

```powershell
$env:COHERE_API_KEY="your_api_key"
```

Run the Flask server:

```bash
python app.py
```

Open your browser and visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

```
/celebrity_search_project
├── app.py               # Flask backend
├── templates/
│   └── index.html       # Frontend UI
├── static/
│   └── styles.css       # Stylesheet
├── requirements.txt     # Dependencies
```

Feel free to fork this repository, make changes, and submit a pull request! 🚀
