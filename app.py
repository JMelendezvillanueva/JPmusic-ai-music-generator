import streamlit as st
from urllib.parse import quote

st.set_page_config(page_title="AI Music Generator", layout="centered")

st.title("🎶 AI Music Generator")
st.markdown("Create epic AI-generated music using Meta’s **MusicGen** and Suno’s **Bark** via Google Colab.")

# Input fields
prompt = st.text_input("🎼 Music Prompt", "A symphonic battle between gods, metal guitars and choirs")
lyrics = st.text_area("📝 Optional Lyrics (for Bark)", "We rise from ash and fire,\nVoices echo higher...")

# URL encode inputs
encoded_prompt = quote(prompt)
encoded_lyrics = quote(lyrics)

# Link to Colab notebook
colab_url = (
    f"https://colab.research.google.com/drive/1d2nUCXBfLZ0EOLoVzSfPNSu7TxbVmeTl"
    f"?prompt={encoded_prompt}&lyrics={encoded_lyrics}"
)

st.markdown("### 🔗 Launch Music Generator in Colab")
st.markdown(f"[▶️ Click here to generate your track]({colab_url})")

# Optional audio preview (future feature)
# st.audio("https://your-public-music-link.com/musicgen_output.wav", format="audio/wav")
