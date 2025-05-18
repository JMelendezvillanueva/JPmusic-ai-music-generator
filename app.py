import streamlit as st
import urllib.parse

st.set_page_config(page_title="AI Music Generator", layout="centered")

st.title("🎶 AI Music Generator")
st.markdown("Create epic AI-generated music using Meta’s **MusicGen** and Suno’s **Bark** via Google Colab.")

# Input fields
prompt = st.text_input("🎼 Music Prompt", "A symphonic battle between gods, metal guitars and choirs")
lyrics = st.text_area("📝 Optional Lyrics (for Bark)", "We rise from ash and fire,\nVoices echo higher...")

# URL encode inputs
encoded_prompt = urllib.parse.quote(prompt)
encoded_lyrics = urllib.parse.quote(lyrics)

# Link to your Colab notebook
colab_base_url = "https://colab.research.google.com/drive/1d2nUCXBfLZ0EOLoVzSfPNSu7TxbVmeTl"
colab_link = f"{colab_base_url}?prompt={encoded_prompt}&lyrics={encoded_lyrics}"

# Output
st.markdown("## 🔗 Launch Music Generator in Colab")
st.markdown(f"▶️ [Click here to generate your track]({colab_link})")

# Optional: embed player later
# st.audio("https://your-hosted-link.com/musicgen_output.wav", format="audio/wav")
