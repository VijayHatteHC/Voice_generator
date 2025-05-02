# voicebot/utils.py
from bark import generate_audio as bark_generate_audio
from bark.generation import preload_models


# Preload models only once
print("preloading bark models")
preload_models(force_reload=False)
def generate_audio(text):
    return bark_generate_audio(text, history_prompt="v2/en_speaker_6")
