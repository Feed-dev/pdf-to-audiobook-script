﻿# PDF to Audiobook Script

This project contains Python scripts that convert PDF documents into audio content.

## Requirements

To run these scripts, you need to have the following Python packages installed:

- PyMuPDF
- pyttsx3
- python-dotenv
- openai
- PyAudio
- pdfplumber
- pydub

You can install these packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

- Create .env file for openai api key
- Depending on the script u have to provide text or pdf path in the script.
- When u use the script with chapters u have to set the pages manually.
- U can change the voice as per openai docs. https://platform.openai.com/docs/guides/text-to-speech
