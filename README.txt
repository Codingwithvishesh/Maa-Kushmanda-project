# Maa Kushmanda Live Drawing (Day 221 / 365)

Yeh project Python aur OpenCV ka use karke Maa Kushmanda ki image ko step-by-step live sketch aur draw karne ke liye banaya gaya hai. Isme Maa Durga aur baki details black color mein draw hoti hain, jabki niche diye gaye lion (sher) ko orange color diya jata hai[cite: 1].

## Features
- OpenCV ke Canny Edge Detection ka use karke precise sketching.
- Lion ke liye alag se **Orange color** (`#FF6500` / BGR format) aur baaki drawing ke liye **Black color**.
- Full-screen / large window support live drawing animation dekhne ke liye[cite: 1].

## Requirements
Is project ko chalane ke liye aapko yeh libraries chahiye hongi (jo `requirements.txt` mein di gayi hain)[cite: 1]:
- `opencv-python`[cite: 1]
- `numpy`[cite: 1]

## Installation & Setup
1. Sabse pehle terminal ya command prompt mein apni project directory par jayein[cite: 1].
2. Required libraries install karne ke liye yeh command run karein[cite: 1]:
   ```bash
   pip install -r requirements.txt

   python maa_kushmanda_draw.py
