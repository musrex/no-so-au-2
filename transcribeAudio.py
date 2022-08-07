import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'CloudDemo_QN_Service.json'
speech_client = speech.SpeechClient()

# Example 1. Load Local Media File
# File Size: < 10mbs, length < 1 minute

media_file_name_mp3 = 'sample_audio.mp3'
media_file_name_wav = 'sample_audio.wav'

with open(media_file_name_mp3, 'rb') as f1:
    byte_data_mp3 = f1.read()
audio_mp3 = speech.RecognitionAudio(content=byte_data_mp3)

with open(media_file_name_wav, 'rb') as f2:
    byte_data_wav = f2.read()
audio_wav = speech.RecognitionAudio(content=byte_data_wav)

## Step 2. Configure Media Files Output
config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='en-US'
)


config_wav = speech.RecognitionConfig(
    
    sample_rate_hertz=16000,
    enable_automatic_punctuation=True,
    language_code='en-US',
    audio_channel_count=1
)


## Step 3. Transcribing the Recognition Audio objects
response_standard_mp3 = speech_client.recognize(
    config=config_mp3,
    audio=audio_mp3
)

response_standard_wav = speech_client.recognize(
    config=config_wav,
    audio=audio_wav
)

print(response_standard_mp3)
print(response_standard_wav)


