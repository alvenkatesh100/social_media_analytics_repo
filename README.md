# 📊 Social Media Analytics Dashboard

A Django REST Framework–based application for analyzing social media posts.  
The app extracts post data, runs sentiment analysis, and provides engagement insights.

---

## 🚀 Features
- Sentiment analysis of social media posts (positive/negative/neutral).
- Engagement tracking (likes, shares, comments).
- REST API endpoints to fetch and analyze posts.
- Extendable to multiple platforms (Twitter, Instagram, LinkedIn, etc.).
- Simple dashboard UI (optional).

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework
- **Analytics:** TextBlob (sentiment analysis)
- **Database:** SQLite (default) / PostgreSQL
- **Frontend (optional):** React / any REST client
- **Language:** Python 3.x

---

## 📂 Project Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/social-media-analytics-dashboard.git
cd social-media-analytics-dashboard

### 2️⃣ Create & Activate Virtual Environment
# Create venv
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows - Command Prompt)
venv\Scripts\activate

# Activate (Windows - PowerShell)
venv\Scripts\Activate.ps1

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

### 5️⃣ Create Superuser 
python manage.py createsuperuser

### 6️⃣ Start the Server
python manage.py runserver


Now open: 👉 http://127.0.0.1:8000/api/