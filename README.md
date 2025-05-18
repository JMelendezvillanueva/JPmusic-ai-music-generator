# 🎶 JPmusic AI Music Generator

A real-time generative AI music app using Meta's MusicGen and a custom Streamlit frontend.

## 🔗 Live App
[Visit the Streamlit app](https://jpmusic-ai-music-generator-jnrgiccm2ifnghbe2psw46.streamlit.app/)

## 🧠 How It Works
- 🧾 Type a music prompt in the Streamlit web app
- 🚀 Streamlit sends it to your Google Colab backend
- 🎵 MusicGen generates a custom `.wav` track
- 🔊 Listen or download your generated song in seconds

## 🛠 Tech Stack
- Meta's [MusicGen](https://github.com/facebookresearch/audiocraft)
- Google Colab + Flask + ngrok
- Streamlit frontend
- Hosted on Streamlit Cloud

## 🚀 To Use It Yourself
1. Open and run all cells in `colab_backend.ipynb`
2. Copy your ngrok URL (e.g., `https://xxxx.ngrok-free.app`)
3. Paste that into `app.py` (replacing the existing backend URL)
4. Push `app.py` to GitHub
5. Streamlit Cloud auto-redeploys your frontend

---

Made with 🔥 by [@JMelendezvillanueva](https://github.com/JMelendezvillanueva)
