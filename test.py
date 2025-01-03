from melo.api import TTS

# Speed is adjustable
speed = 1.0

# CPU is sufficient for real-time inference.
# You can set it manually to 'cpu' or 'cuda' or 'cuda:0' or 'mps'
device = 'auto' # Will automatically use GPU if available

# English 
text = "Since 2023."
model = TTS(language='EN', device=device)
speaker_ids = model.hps.data.spk2id

# American accent
output_path = 'en-us.wav'
model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)

# British accent
output_path = 'en-br.wav'
model.tts_to_file(text, speaker_ids['EN-BR'], output_path, speed=speed)

# Indian accent
output_path = 'en-india.wav'
model.tts_to_file(text, speaker_ids['EN_INDIA'], output_path, speed=speed)

# Australian accent
output_path = 'en-au.wav'
model.tts_to_file(text, speaker_ids['EN-AU'], output_path, speed=speed)

# Default accent
output_path = 'en-default.wav'
model.tts_to_file(text, speaker_ids['EN-Default'], output_path, speed=speed)

# Japanese
text = "こんにちは."
model = TTS(language='JP', device=device)
speaker_ids = model.hps.data.spk2id
output_path = 'jp.wav'
model.tts_to_file(text, speaker_ids['JP'], output_path, speed=speed)

# KR
text = "안녕하세요."
model = TTS(language='KR', device=device)
speaker_ids = model.hps.data.spk2id
output_path = 'kr.wav'
model.tts_to_file(text, speaker_ids['KR'], output_path, speed=speed)

# ES
text = "Hola."
model = TTS(language='ES', device=device)
speaker_ids = model.hps.data.spk2id
output_path = 'es.wav'
model.tts_to_file(text, speaker_ids['ES'], output_path, speed=speed)

# FR
text = "Tu as mangé quoi aujourd'hui?"
model = TTS(language='FR', device=device)
speaker_ids = model.hps.data.spk2id
output_path = 'fr.wav'
model.tts_to_file(text, speaker_ids['FR'], output_path, speed=speed)
