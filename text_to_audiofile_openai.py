import os
from dotenv import load_dotenv
from openai import OpenAI
from pydub import AudioSegment

# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client with the API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Configurable chunk size
CHUNK_SIZE = 4096

# Function to split text into chunks
def split_text(text, chunk_size=CHUNK_SIZE):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Example text for demonstration
text = """
2
1 = 2
Allow Me to Enlighten You
If
Can you see where the mistake has occurred?
4/2 is the inverse operation of 2 x 2 = 4
Both of these scenarios are identical in every way.
Then
The only difference exists in dimension alone. If they ADD,
SUBTRACT and DIVIDE according to the same ratio then
it would naturally follow that
they must also MULTIPLY according to the same ratio,
plain and simple!
2/1 is the inverse operation of 1 x 1 = 2
If
What does your common sense tell you about
2/1 is inconsistent with 1 x 1 = 1
these two scenarios?
Although
What do they have in common 4/2 is consistent with 2 x 2 = 4
and what are their differences?
Then
it should follow that:
DIVISION 2² = 4 & 1² = 2
The number four is divided by two, twice.
and the truth is:
The number two is divided by one, twice.
Yet, the Math and Scientific community tells us that common
ADDITION
sense and logic are wrong in this case because of a product of an
2 + 2 = 4 And 1 + 1 = 2 arbitrary convention.
"""

# Split the extracted text into chunks
chunks = split_text(text)

# Print the number of chunks
print(f"Total chunks: {len(chunks)}")

# Directory to store individual chunk audio files
chunk_audio_dir = "chunk_audio"
os.makedirs(chunk_audio_dir, exist_ok=True)

# Synthesize audio for each chunk and save them as individual files
for j, chunk in enumerate(chunks):
    print(f"Synthesizing audio for chunk {j+1}/{len(chunks)}...")
    chunk_audio_path = os.path.join(chunk_audio_dir, f"chunk_{j+1}.mp3")
    response = client.audio.speech.create(
        model="tts-1-hd",
        voice="onyx",
        input=chunk,
        response_format="mp3"
    )
    response.stream_to_file(chunk_audio_path)

# Combine the audio files
combined_audio = AudioSegment.empty()
for j in range(len(chunks)):
    chunk_audio_path = os.path.join(chunk_audio_dir, f"chunk_{j+1}.mp3")
    audio_segment = AudioSegment.from_file(chunk_audio_path, format="mp3")
    combined_audio += audio_segment

# Save the combined audio to an MP3 file
output_path = "combined_output_text_audio.mp3"
combined_audio.export(output_path, format="mp3")
print(f"{output_path} saved successfully.")
