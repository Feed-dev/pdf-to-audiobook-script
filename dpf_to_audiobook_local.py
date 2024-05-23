import os
import pyaudio
import wave
import fitz  # PyMuPDF
import pyttsx3

# Function to play audio using PyAudio
def play_audio(file_path):
    with wave.open(file_path, 'rb') as wf:
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)
        stream.stop_stream()
        stream.close()
        p.terminate()

# Function to extract text from PDF using PyMuPDF
def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    return text

# Function to save extracted text to a .txt file
def save_text_to_file(text, txt_output_path):
    with open(txt_output_path, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"Text saved to {txt_output_path}")

# Function to synthesize speech using pyttsx3
def text_to_speech_pyttsx3(text, audio_output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, audio_output_path)
    engine.runAndWait()
    print("Audio generated successfully.")

# Main function to convert PDF to audiobook and save text to file
def pdf_to_audiobook(pdf_path, audio_output_path, txt_output_path):
    text = extract_text_from_pdf(pdf_path)
    save_text_to_file(text, txt_output_path)
    text_to_speech_pyttsx3(text, audio_output_path)
    play_audio(audio_output_path)

# Example usage
pdf_path = "OTOET_PREVIEW_062_October_03_2021.pdf"
audio_output_path = "OTOET_PREVIEW_062_October_03_2021.wav"
txt_output_path = "OTOET_PREVIEW_062_October_03_2021.txt"
pdf_to_audiobook(pdf_path, audio_output_path, txt_output_path)
