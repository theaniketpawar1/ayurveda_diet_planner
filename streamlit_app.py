import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="🌿 Ayurvedic Diet Planner", layout="wide")

st.title("🌿 Ayurvedic Diet Planner")
st.write("Select your symptoms, and our Ayurvedic AI will detect your dosha and generate a personalized diet plan.")

name = st.text_input("👤 Name")
age = st.number_input("🎂 Age", 1, 100, 25)
gender = st.selectbox("⚧️ Gender", ["Male", "Female", "Other"])

symptoms = st.multiselect("🩺 Select Symptoms", [
    "Constipation", "Dry skin", "Anxiety", "Insomnia",
    "Acid reflux / Heartburn", "Irritability / Anger", "Excessive sweating", "Skin rashes",
    "Laziness / Lethargy", "Weight gain", "Congestion", "Water retention"
])

if st.button("✨ Generate Diet Plan"):
    try:
        resp = requests.post(f"{API_BASE}/diet-plan", json={
            "name": name, "age": age, "gender": gender, "symptoms": symptoms
        })
        if resp.status_code == 200:
            result = resp.json()
            st.subheader(f"✅ Dominant Dosha: {result['dosha']}")

            st.subheader("🍽️ Diet Plan")
            for meal in ["Breakfast", "Lunch", "Dinner"]:
                st.write(f"**{meal}**")
                st.table(result["plan"].get(meal, []))

            st.subheader("⚠️ Precautions")
            st.write(result["precautions"])
        else:
            st.error(f"Backend error: {resp.text}")
    except Exception as e:
        st.error(f"❌ Failed to connect: {e}")