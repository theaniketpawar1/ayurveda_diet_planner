🌿 Ayurvedic Diet Planner (AI-powered) 📌 Project Description

This project is built for DevCreate BuildFest hackathon. It provides a personalized Ayurvedic diet recommendation system that detects a user’s dominant dosha (Vata, Pitta, Kapha) based on selected symptoms and generates a diet chart with precautions and suggestions using LLMs (Large Language Models) like Google Gemini / Grok AI.

The app is designed for normal users who may not know about Ayurvedic terms. They just need to select symptoms → the system will:

Detect their dosha imbalance (Vata / Pitta / Kapha). Generate a personalized diet chart (Breakfast, Lunch, Dinner with calories). Provide precautions, lifestyle tips, and recommendations. Allow chat interaction with the AI for further queries. 🚀 Features Symptom-based dosha detection. AI-powered diet chart generation using Gemini/Grok API. Daily precautions & lifestyle recommendations. Interactive chatbot with LLM. Streamlit-based UI with clean, user-friendly design. Visualizations for calorie distribution & diet breakdown. 🛠️ Tech Stack Frontend: Streamlit (Python) Backend: FastAPI AI Integration: Google Gemini API / Grok API Visualization: Matplotlib / Pandas Dataset (optional): Ayurvedic food dataset (CSV) 📂 Folder Structure submissions/ T123_AyurvedaAI/ code/ backend/ main.py symptoms.py utils.py streamlit_app.py requirements.txt README.md Team123_AyurvedaAI_Presentation.pdf

⚙️ Setup Instructions 1️⃣ Clone repo & navigate git clone https://github.com/theaniketpawar1/DevCreate-BuildFest.git cd DevCreate-BuildFest/submissions/T123_AyurvedaAI/code

2️⃣ Create virtual environment python -m venv venv source venv/bin/activate # (Linux/Mac) venv\Scripts\activate # (Windows)

3️⃣ Install dependencies pip install -r requirements.txt

4️⃣ Run Backend (FastAPI) uvicorn backend.main:app --reload --port 8000

5️⃣ Run Frontend (Streamlit) streamlit run streamlit_app.py

6️⃣ Open in Browser http://localhost:8501

📊 Example Output Detected Dosha: Pitta Diet Plan: Breakfast: Oatmeal with raisins + Sweet Apple Lunch: Basmati rice, Mung Dal soup, Steamed Veggies Dinner: Quinoa Khichdi + sautéed leafy greens Precautions: Avoid spicy/oily foods, practice cooling breathing, maintain regular sleep. 👨‍💻 Team Members Aniket Pawar [Other teammate names if applicable] 📽️ Demo

Screenshots and demo video links can be added here.

🏆 Hackathon Track Track: AI for Healthcare Problem Statement: Personalized Ayurvedic Diet Recommendation