import os
import logging
import pdfplumber
from dotenv import load_dotenv
from openai import OpenAI
from pydub import AudioSegment
import shutil

# Load environment variables from the .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the OpenAI client with the API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Configurable chunk size
CHUNK_SIZE = 4096


# Function to extract text from a range of pages in a PDF
def extract_text_from_pdf(pdf_path, start_page, end_page):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page_number in range(start_page - 1, end_page):  # Adjust for zero-based index
                page = pdf.pages[page_number]
                text += page.extract_text()
        return text
    except Exception as e:
        logging.error(f"Error extracting text from PDF: {e}")
        raise


# Function to split text into chunks
def split_text(text, chunk_size=CHUNK_SIZE):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks


# Path to the PDF file
pdf_path = "OTOET_PREVIEW_062_October_03_2021.pdf"

# Define chapter ranges (start_page, end_page)
chapter_ranges = [
    (9, 12),  # Chapter 1
    (13, 24),  # Chapter 2
    (25, 32)  # Chapter 3
    # Add more chapters as needed
]

# Directory to store individual chunk audio files
chunk_audio_dir = "chunk_audio"
os.makedirs(chunk_audio_dir, exist_ok=True)

# Iterate over each chapter range
for i, (start_page, end_page) in enumerate(chapter_ranges):
    print(f"Processing Chapter {i + 1} (Pages {start_page} to {end_page})...")

    # Extract text for the chapter
    text = extract_text_from_pdf(pdf_path, start_page, end_page)

    # Split the extracted text into chunks
    chunks = split_text(text)

    # Print the number of chunks
    print(f"Total chunks for Chapter {i + 1}: {len(chunks)}")

    # Synthesize audio for each chunk and save them as individual files
    for j, chunk in enumerate(chunks):
        print(f"Synthesizing audio for Chapter {i + 1}, chunk {j + 1}/{len(chunks)}...")
        chunk_audio_path = os.path.join(chunk_audio_dir, f"chapter_{i + 1}_chunk_{j + 1}.mp3")
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice="onyx",
            input=chunk,
            response_format="mp3"
        )
        response.stream_to_file(chunk_audio_path)

    # Combine the audio files for the chapter
    combined_audio = AudioSegment.empty()
    for j in range(len(chunks)):
        chunk_audio_path = os.path.join(chunk_audio_dir, f"chapter_{i + 1}_chunk_{j + 1}.mp3")
        audio_segment = AudioSegment.from_file(chunk_audio_path, format="mp3")
        combined_audio += audio_segment

    # Save the combined audio for the chapter to an MP3 file
    output_path = f"chapter_{i + 1}_output.mp3"
    combined_audio.export(output_path, format="mp3")
    print(f"{output_path} saved successfully.")

# Clean up the directory with chunk audio files
shutil.rmtree(chunk_audio_dir)
