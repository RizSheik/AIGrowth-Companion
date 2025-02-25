import streamlit as st
import random
import datetime

# Custom CSS for Styling
st.markdown("""
    <style>
        /* Background gradient */
        body {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: white;
        }
        /* Center Title */
        .main-title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            color: #f4a261;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
        }
        /* Subtitle */
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #e9c46a;
            margin-bottom: 30px;
        }
        /* Custom Card */
        .card {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 15px rgba(255, 255, 255, 0.2);
            margin-bottom: 20px;
        }
        /* Button Styling */
        .stButton>button {
            background: #f4a261;
            color: white;
            font-size: 1.2em;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: #e76f51;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🚀 AI Growth Companion</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Stay motivated, track progress, and develop a strong growth mindset!</p>", unsafe_allow_html=True)

# 🌟 AI-Generated Motivational Message
motivational_quotes = [
    "Every challenge is an opportunity to grow. 🌱",
    "Mistakes are proof that you are trying! 🚀",
    "Success comes from learning, not just achieving. 🎯",
    "A positive mindset leads to positive outcomes. 💡",
    "Embrace discomfort—it means you're learning! 🔥"
]
daily_message = random.choice(motivational_quotes)

st.markdown(f"<div class='card'><h3>💡 AI Motivational Boost</h3><p><strong>{daily_message}</strong></p></div>", unsafe_allow_html=True)

# 📈 Growth Tracker
st.markdown("<div class='card'><h3>📊 Your Growth Tracker</h3></div>", unsafe_allow_html=True)
today = datetime.date.today()
progress = st.slider("How do you feel about your growth today?", 0, 100, 50)
st.write(f"Your growth score for {today}: **{progress}%**")

# 🔥 AI Affirmation Generator
st.markdown("<div class='card'><h3>🔮 Personalized AI Affirmation</h3></div>", unsafe_allow_html=True)
user_name = st.text_input("Enter your name to receive a special message:")

if user_name:
    affirmations = [
        f"{user_name}, you have unlimited potential! 🚀",
        f"Every step you take, {user_name}, brings you closer to greatness. ✨",
        f"{user_name}, challenges make you stronger. Keep going! 💪",
        f"Believe in yourself, {user_name}, because I do! 🌟",
        f"{user_name}, you are creating your future, one step at a time. 🎯"
    ]
    st.info(random.choice(affirmations))

# 🏆 Personal Wins & Goals
st.markdown("<div class='card'><h3>🏆 Celebrate Your Wins & Set Goals</h3></div>", unsafe_allow_html=True)
win = st.text_input("What’s something positive you achieved today?")
goal = st.text_input("What’s your next growth goal?")

if win:
    st.success(f"🎉 Amazing! You accomplished: **{win}**")
if goal:
    st.info(f"🚀 Keep striving! Your next target is: **{goal}**")

# 📅 Daily Reflection
st.markdown("<div class='card'><h3>📝 Reflect & Grow</h3></div>", unsafe_allow_html=True)
reflection = st.text_area("Write your thoughts, learnings, or struggles here:")
if reflection:
    st.success("✨ Reflection is key to progress! Keep learning.")

st.write("---")
st.write("🚀 Keep going! Every day is a step toward greatness. 🌟")
st.write("**©️ Created by Rizwan - AI-Powered Growth Journey**")