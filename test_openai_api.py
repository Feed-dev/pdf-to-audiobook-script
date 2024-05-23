# Import necessary libraries
import os
from dotenv import load_dotenv
from openai import OpenAI
from pydub import AudioSegment
from pydub.playback import play

# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client with the API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Generate speech
response = client.audio.speech.create(
    model="tts-1-hd",
    voice="onyx",
    input="The quick brown fox jumps over the lazy dog.",
    response_format="mp3"
)

response.stream_to_file("output.mp3")
