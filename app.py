import streamlit as st
import requests

st.set_page_config(page_title="🎶 AI Music Generator", layout="centered")

st.title("🎶 AI Music Generator")
st.markdown("Generate epic music using Meta’s **MusicGen** model, powered by your Colab backend.")

# User Inputs
prompt = st.text_input("🎼 Music Prompt", value="A cinematic metal battle with electric guitars and choir")
duration = st.slider("⏱️ Duration (seconds)", min_value=5, max_value=30, value=10)

# Optional: future Bark integration
lyrics = st.text_area("📝 (Optional) Lyrics for future Bark vocal input", value="We rise from ash and fire,\nVoices echo higher...")

# Action
if st.button("🎵 Generate Music"):
    with st.spinner("Summoning Colab magic..."):
        try:
            # ⛓️ Replace this with your actual ngrok URL from Colab
            NGROK_BACKEND_URL = "https://6ab1-34-125-250-202.ngrok-free.app/generate"  # ← CHANGE THIS

            response = requests.post(
                NGROK_BACKEND_URL,
                json={"prompt": prompt, "duration": duration}
            )

            if response.status_code == 200:
                with open("output.wav", "wb") as f:
                    f.write(response.content)
                st.success("✅ Music generated!")
                st.audio("output.wav", format="audio/wav")
            else:
                st.error("❌ Error: Backend failed to generate music.")
        except Exception as e:
            st.error(f"Connection error: {e}")
