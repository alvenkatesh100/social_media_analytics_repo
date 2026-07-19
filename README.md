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
```

### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

On Windows PowerShell:
```powershell
venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment
```bash
export DJANGO_SECRET_KEY=change-me
export DJANGO_DEBUG=1
export DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
export XQUIK_API_KEY=your_xquik_key
```

SQLite is the default local database. Set `DB_ENGINE`, `DB_NAME`, `DB_USER`,
`DB_PASSWORD`, `DB_HOST`, and `DB_PORT` to use another database.

### 5️⃣ Run Migrations
```bash
cd social_media_analytics
python manage.py migrate
```

### 6️⃣ Create Superuser
```bash
python manage.py createsuperuser
```

### 7️⃣ Start the Server
```bash
python manage.py runserver
```

Now open `http://127.0.0.1:8000/api/`.

## Xquik Import

Authenticated clients can import Xquik search results into the same
`SocialPost` table used by the analytics API:

```http
POST /api/posts/xquik/import/
Authorization: Bearer <token>
Content-Type: application/json

{"query": "nvidia", "limit": 10}
```

The endpoint stores imported rows with `platform` set to `xquik`, then returns
serialized posts with sentiment data.

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
