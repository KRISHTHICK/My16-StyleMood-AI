import streamlit as st
from PIL import Image
from io import BytesIO
from colorthief import ColorThief
import numpy as np
import json

st.set_page_config(page_title="👗 StyleMood AI", layout="centered")
st.title("👗 StyleMood AI – Outfit Mood & Occasion Detector")

# Load style mood rules
with open("style_rules.json", "r") as f:
    style_rules = json.load(f)

def get_dominant_color(image):
    img_bytes = BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    ct = ColorThief(img_bytes)
    return ct.get_color(quality=1)

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def mood_from_color(dominant_hex):
    best_match = None
    best_score = float('inf')

    def hex_dist(h1, h2):
        return sum((int(h1[i:i+2], 16) - int(h2[i:i+2], 16))**2 for i in (1, 3, 5))

    for rule in style_rules:
        for color in rule["colors"]:
            score = hex_dist(dominant_hex, color)
            if score < best_score:
                best_score = score
                best_match = rule
    return best_match

# Upload
uploaded = st.file_uploader("📸 Upload outfit image", type=["png", "jpg", "jpeg"])
if uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Your Outfit", use_column_width=True)

    color_rgb = get_dominant_color(image)
    color_hex = rgb_to_hex(color_rgb)
    st.markdown(f"🎨 Dominant Color Detected: `{color_hex}`")

    mood = mood_from_color(color_hex)
    st.markdown(f"### 🧠 Detected Mood: **{mood['mood']}**")
    st.success(f"💡 Suggestion: {mood['suggestions']}")
