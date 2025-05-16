# My16-StyleMood-AI
GenAI

Here’s a **new AI fashion project topic** with **full code**, **README**, and steps to run in **VS Code** or **Streamlit Cloud/GitHub**:

---

## 👗 **StyleMood AI – Outfit Mood & Occasion Detector**

### 🎯 Overview:

**StyleMood AI** lets users upload an outfit image and detects the *mood* (e.g., casual, formal, sporty) and *occasion* (e.g., party, work, gym). The AI model uses color psychology and visual cues to suggest matching occasions and moods.

---

### ✅ Features:

* 📸 Upload an outfit photo
* 🧠 AI detects mood & occasion using color and patterns
* 🎯 Shows confidence score and visual interpretation
* 📝 Suggests styling tips and accessories
* 💬 Option to get style tips using a local LLM agent

---

## 🗂 Project Structure:

```
StyleMood-AI/
├── app.py
├── style_rules.json
├── requirements.txt
└── README.md
```

---

### 📦 `requirements.txt`

```txt
streamlit
Pillow
colorthief
numpy
```

---

### 📁 `style_rules.json`

```json
[
  {
    "mood": "Casual",
    "colors": ["#f5f5dc", "#a9a9a9", "#deb887"],
    "suggestions": "Perfect for a casual hangout or cafe visit. Pair with sneakers."
  },
  {
    "mood": "Formal",
    "colors": ["#000000", "#2f4f4f", "#708090"],
    "suggestions": "Great for business meetings or formal dinners. Add a blazer or heels."
  },
  {
    "mood": "Sporty",
    "colors": ["#ff4500", "#32cd32", "#4682b4"],
    "suggestions": "Best for gym, workouts or jog. Wear running shoes or sports watch."
  }
]
```

---

### 🧠 `app.py`

```python
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
```

---

### 📝 `README.md`

````markdown
# 👗 StyleMood AI

An AI-based outfit analyzer that detects your mood and suitable occasion based on your outfit image.

## 🎯 Features
- Upload outfit image
- Detect dominant color
- Predict mood and occasion
- Get fashion suggestions

## 📦 Requirements
```bash
pip install -r requirements.txt
````

## 🚀 How to Run Locally

```bash
git clone https://github.com/your-username/StyleMood-AI.git
cd StyleMood-AI
streamlit run app.py
```

## 🌐 Deploy Online

* Deploy on Streamlit Cloud for free: [https://streamlit.io/cloud](https://streamlit.io/cloud)

## 🧠 Future Features

* Add texture and pattern detection
* Integrate LLM for natural language styling tips

```

---

Would you like a **GitHub-ready** version or another **project idea**?
```
