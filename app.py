from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os

from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("gemini_api_key"))

model=genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts =[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
        
                    

##initialize our streamlit app.

st.set_page_config(page_title="multilanguage Invoice Extractor")

st.header("Multilanguage Invoice Extractor")
input=st.text_input("Input Prompt:" ,key="input")
uploaded_file = st.file_uploader("Choose an invoice image", type=["jpg", "jpeg", "png","pdf"])  

image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Invoice.', use_column_width=True)

submit=st.button("Tell me about this invoice")

input_prompt="""You are an invoice extraction AI model. Your task is to extract key information from invoices, such as invoice number, date, total amount, vendor name, and line items.You are an expert in understanding invoices from different countries and formats based on that you can answer the questions.
The invoices can be in multiple languages including English,Hindi, Spanish, French, German, Chinese, and Japanese.
Please provide the extracted information in a structured tabular format it is mandatory  ."""

##if submit button is clicked
if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input,image_data,input_prompt)
    st.subheader("Extracted Invoice Information:")
    st.write(response)