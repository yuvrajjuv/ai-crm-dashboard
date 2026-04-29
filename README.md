🚀 AI CRM Dashboard

An AI-powered CRM dashboard built using React + FastAPI that helps track doctor interactions with smart tagging and timestamps.

---

🔥 Features

- ➕ Add doctor interactions
- 🤖 AI-based auto tagging:
  - 💰 Pricing Discussion
  - 🔁 Follow-up Required
  - ⚠️ Complaint
  - 📝 General
- ⏱ Timestamp for every interaction
- 🎨 Clean & professional UI
- ❌ Delete interaction (optional feature)
- ⚡ Fast & responsive

---

🛠 Tech Stack

Layer| Tech Used
Frontend| React.js
Backend| FastAPI (Python)
Styling| CSS

---

📂 Project Structure

ai-crm-dashboard/
│
├── backend/
│   ├── main.py
│   └── routes/
│       └── interaction_routes.py
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   └── App.css
│
└── README.md

---

⚡ How to Run Project

🔹 1. Run Backend

cd backend
uvicorn main:app --reload

👉 Backend runs at:
http://127.0.0.1:8000

---

🔹 2. Run Frontend

cd frontend
npm install
npm start

👉 Frontend runs at:
http://localhost:3000

---

🧠 AI Tag Logic (How it works)

Based on keywords in notes:

- "price", "cost" → 💰 Pricing Discussion
- "follow", "later" → 🔁 Follow-up
- "issue", "problem" → ⚠️ Complaint
- else → 📝 General

---

📸 Demo

👉 Add doctor name + notes
👉 Click "Add Interaction"
👉 See:

- Auto AI tag
- Timestamp
- Clean UI card

---

🎯 Future Improvements

- 🔍 Search & filter interactions
- 🗑 Delete from backend
- 🔐 Authentication (login/signup)
- 🗄 Database integration (MongoDB/PostgreSQL)
- 📊 Analytics dashboard

---

👨‍💻 Author

Your Name

---

⭐ Final Note

This project demonstrates:

- Full-stack development
- API integration
- Basic AI/NLP logic
- Clean UI/UX design

---