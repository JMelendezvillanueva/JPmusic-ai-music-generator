import streamlit as st
import urllib.parse

st.set_page_config(page_title="AI Music Generator", layout="centered")

st.title("🎶 AI Music Generator")
st.markdown("Generate epic music using Meta’s **MusicGen** and Suno’s **Bark**.")

# Inputs
prompt = st.text_input("🎼 Music Prompt", value="A symphonic battle between gods, metal guitars and choirs")
lyrics = st.text_area("📝 Optional Lyrics (for Bark)", value="We rise from ash and fire,\nVoices echo higher...")
duration = st.slider("🎧 Duration (seconds)", 5, 30, 10)

# Encode inputs for URL
encoded_prompt = urllib.parse.quote(prompt)
encoded_lyrics = urllib.parse.quote(lyrics)

# ✅ Use template view to force Colab to honor query params
colab_base_url = "https://colab.research.google.com/drive/1d2nUCXBfLZ0EOLoVzSfPNSu7TxbVmeTl?usp=sharing&template=true"
colab_link = f"{colab_base_url}&prompt={encoded_prompt}&lyrics={encoded_lyrics}&duration={duration}"

# Display Colab Link
st.markdown("## 🔗 Open the Generator in Google Colab")
st.markdown(f"▶️ [Click here to generate your track in Colab]({colab_link})")

# Display copyable code as fallback
st.markdown("## 🧪 Or copy this into your Colab notebook:")
colab_code = f"""
from audiocraft.models import MusicGen
import torchaudio

prompt = \"\"\"{prompt}\"\"\"
duration = {duration}

model = MusicGen.get_pretrained('facebook/musicgen-small')
model.set_generation_params(duration=duration)
instrumental = model.generate([prompt])
torchaudio.save("musicgen_output.wav", instrumental[0].cpu(), 32000)
"""
st.code(colab_code, language="python")
