# Invoice Extractor

Streamlit app that uses Google Gemini to extract structured information from invoice images (and PDFs where supported).

## Features

- Upload an invoice image and get key fields in a structured table
- Supports multi-language invoices (English, Hindi, Spanish, French, German, Chinese, Japanese)
- Simple, interactive UI built with Streamlit

## Project Structure

- `app.py`: Streamlit UI and Gemini inference
- `src/`: Local modules and constants
- `requirements.txt`: Python dependencies

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```bash
gemini_api_key=YOUR_API_KEY
```

## Run

```bash
streamlit run app.py
```

## Notes

- PDF support depends on your local Pillow build. If PDF upload fails, convert the PDF to an image first.

## Author

- Suraj (surajsingh8204@gamil.com)