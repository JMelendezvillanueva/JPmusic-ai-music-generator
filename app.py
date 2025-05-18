import streamlit as st

st.set_page_config(page_title="AI Music Generator", layout="centered")

st.title("🎶 AI Music Generator")
st.markdown("Generate epic music using Meta’s **MusicGen** and Suno’s **Bark**.")

# Inputs
prompt = st.text_input("🎼 Music Prompt", value="A symphonic battle between gods, metal guitars and choirs")
lyrics = st.text_area("📝 Optional Lyrics (for Bark)", value="We rise from ash and fire,\nVoices echo higher...")
duration = st.slider("🎧 Duration (seconds)", 5, 30, 10)

# Generate code to paste into Colab
st.markdown("## 🧪 Copy this into your Colab notebook:")

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

st.markdown("🔗 [Open the Colab Notebook](https://colab.research.google.com/drive/1d2nUCXBfLZ0EOLoVzSfPNSu7TxbVmeTl)")
