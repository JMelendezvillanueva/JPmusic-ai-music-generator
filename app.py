import streamlit as st
import requests

st.set_page_config(page_title="🎶 AI Music Generator", layout="centered")

st.title("🎶 AI Music Generator")
st.markdown("Generate epic music using Meta’s **MusicGen** model, powered by your local backend via ngrok.")

# User input
prompt = st.text_input("🎼 Enter a music prompt", value="A cinematic metal battle with electric guitars and choirs")
duration = st.slider("🎧 Duration (seconds)", min_value=5, max_value=30, value=10)

# Action button
if st.button("🎵 Generate Music"):
    with st.spinner("Summoning your symphony..."):
        try:
            # ✅ Your current ngrok backend URL
            backend_url = "https://b7f8-24-74-214-254.ngrok-free.app/generate"

            response = requests.post(
                backend_url,
                json={"prompt": prompt, "duration": duration}
            )

            if response.status_code == 200:
                with open("output.wav", "wb") as f:
                    f.write(response.content)
                st.success("✅ Music generated!")
                st.audio("output.wav", format="audio/wav")
            else:
                st.error(f"❌ Backend error: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Connection failed: {e}")
