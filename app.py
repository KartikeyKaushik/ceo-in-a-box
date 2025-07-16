import streamlit as st
import requests
import os
import random
from dotenv import load_dotenv
import streamlit.components.v1 as components

load_dotenv()

st.set_page_config(
    page_title="CEO-in-a-Box",
    page_icon="💼",
    layout="wide"
)

# ---------------- Animated Backgrou    nd ---------------- #
particles_html = """
<div id="particles-js"></div>
<script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
<script>
particlesJS("particles-js", {
  "particles": {
    "number": { "value": 100 },
    "color": { "value": "#ffffff" },
    "shape": { "type": "circle" },
    "opacity": { "value": 0.4 },
    "size": { "value": 3 },
    "line_linked": { "enable": true, "color": "#ffffff" },
    "move": { "enable": true, "speed": 2 }
  },
  "interactivity": {
    "events": { "onhover": { "enable": true, "mode": "repulse" } }
  }
});
</script>
<style>
#particles-js {
  position: fixed;
  width: 100%;
  height: 100%;
  z-index: -1;
  background: #0d0d0d;
}
</style>
"""
components.html(particles_html, height=0, width=0)

# ---------------- Tagline Rotation ---------------- #
taglines = [
    "From Idea to Identity — Instantly.",
    "Build Brands. Break Norms.",
    "Your Startup’s Co-Founder in Code.",
    "Launch Like a CEO. Think Like a Pro.",
    "AI-Powered Brilliance for Your Billion-Dollar Dream.",
    "Branding from the Future. Built for You.",
    "Not Just Smart — CEO Smart.",
    "Where Vision Meets Execution.",
    "Strategy, Styled and Simplified.",
    "Think Bold. Launch Faster. Scale Smarter.",
    "The Shortcut to a Smarter Startup.",
    "Crafted Strategy. Instant Execution.",
    "Every Founder’s Secret Weapon.",
    "One Click Closer to CEO Mode.",
    "Brand Strategy — Without the Agency Price Tag."
]
current_tagline = random.choice(taglines)

# ---------------- Custom CSS ---------------- #
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;800&display=swap');

    html, body {
        font-family: 'Space Grotesk', sans-serif;
        background-color: #000;
        color: #ffffff;
        overflow-x: hidden;
    }

    .stApp {
        background: transparent !important;
    }

    .main .block-container {
        padding: 3rem;
        background-color: rgba(20, 20, 30, 0.8);
        border-radius: 20px;
        box-shadow: 0 30px 100px rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(16px);
    }

    .stTextArea textarea {
        background: #111118;
        color: #fff;
        border-radius: 16px;
        font-size: 18px;
        padding: 1.4rem;
        border: 1px solid #444;
    }

    .stButton > button {
        background: linear-gradient(135deg, #00feba, #5b548a);
        color: #000;
        font-size: 20px;
        font-weight: 800;
        padding: 1rem 2.2rem;
        border: none;
        border-radius: 18px;
        transition: all 0.3s ease-in-out;
        cursor: pointer;
    }

    .stButton > button:hover {
        transform: scale(1.1);
        box-shadow: 0 0 25px rgba(0, 254, 186, 0.6);
    }

    h1.brand-title {
        font-size: 62px;
        font-weight: 800;
        letter-spacing: 2px;
        background: linear-gradient(90deg, #ffe259, #ffa751);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.3rem;
    }

    p.subtitle {
        font-size: 22px;
        text-align: center;
        color: #dddddd;
        margin-bottom: 30px;
    }

    .output-block {
        background: #1c1c2c;
        padding: 2rem;
        border-radius: 18px;
        border: 1px solid #555;
        font-size: 18px;
        line-height: 1.75;
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.05);
    }

    .creator-tag {
        font-size: 15px;
        text-align: right;
        margin-top: 30px;
        color: #aaa;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Hero Section ---------------- #
st.markdown(f"""
    <h1 class='brand-title'>CEO-in-a-Box</h1>
    <p class='subtitle'>{current_tagline}</p>
    <p style='text-align: center; font-size: 16px; color: #aaa;'>Crafted by <b>Kartikey Kaushik</b></p>
""", unsafe_allow_html=True)

api_key = os.getenv("OPENROUTER_API_KEY")

idea = st.text_area("💡 Describe Your Startup Idea", height=200, placeholder="e.g., A wellness AI that tracks student stress levels and suggests daily hacks")

col1, col2, col3 = st.columns(3)

with col1:
    tone = st.selectbox("🎨 Select Tone", [
        "Professional", "Playful", "Inspiring", "Minimalist", "Luxury", "Bold", "Gen-Z", "Futuristic"
    ])
with col2:
    industry = st.selectbox("📚 Select Industry", [
        "Health", "Education", "Finance", "Tech", "Fashion", "Food", "Travel", "Entertainment", "Fitness", "Real Estate"
    ])
with col3:
    location = st.selectbox("📍 Target Region", [
        "Global", "North America", "South America", "Europe", "Asia", "Africa", "Australia", "Middle East"
    ])

if st.button("✨ Generate My Brand Strategy"):
    if not api_key:
        st.error("API key not found! Add OPENROUTER_API_KEY to your .env file.")
    elif not idea.strip():
        st.warning("Please enter a startup idea.")
    else:
        with st.spinner("🧠 Generating your brand strategy masterpiece..."):
            prompt = f"""
You are a creative brand strategist. Based on the startup idea below, generate the following:

1. Brand Name (original & catchy)
2. One-line Tagline
3. Brand Story (50–100 words, emotional & inspiring)
4. Market Size Estimation
5. Three Revenue Models
6. Target Audience (detailed)
7. Top 3 competitors
8. Risks involved and solutions

Tone: {tone}
Industry: {industry}
Target Region: {location}

Startup Idea: {idea}
"""

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json={
                    "model": "mistralai/mistral-7b-instruct",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
            )

            if response.status_code == 200:
                result = response.json()
                output = result["choices"][0]["message"]["content"]
                st.markdown("### 🎯 Brand Strategy Output:")
                st.markdown(f"""
                <div class='output-block'>
                    {output.replace('\n', '<br>')}
                </div>
                <div class='creator-tag'>🚀 Built with ❤️ by <b>Kartikey Kaushik</b></div>
                """, unsafe_allow_html=True)
            else:
                st.error("Something went wrong: " + response.text)
