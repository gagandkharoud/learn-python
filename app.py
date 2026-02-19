import os
import io
import json
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader
from openai import OpenAI
from dotenv import load_dotenv

# --- 1. SETUP & CREDENTIALS ---
load_dotenv() # Reads your .env file
app = FastAPI()

# Initialize the OpenAI client with your key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# This is the "Security Guard"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # This tells Python: "It's okay to talk to React"
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. THE AI HELPER FUNCTION ---
def ask_openai_to_parse(resume_text: str):
    # This sends the messy text to the 'Chef' (OpenAI)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional recruiter. Extract data into JSON."},
            {"role": "user", "content": f"Extract the Name, Email, and Top 3 Skills from this text: {resume_text}"}
        ],
        response_format={ "type": "json_object" }
    )
    # Returns the JSON string from the AI
    return response.choices[0].message.content

@app.post("/upload-resume")
async def process_resume(file: UploadFile = File(...)):
    # NEW STEP: Read the actual data from the file
    content = await file.read() 
    
    # 1. Wrap the bytes in a "Virtual File"
    pdf_stream = io.BytesIO(content)
    
    # 2. Hand that virtual file to the PDF Reader
    reader = PdfReader(pdf_stream)
    
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    
    # C. NEW: Send the text to the AI function we built above
    ai_json_string = ask_openai_to_parse(text)
    
    # Let's see how big the file is (in bytes)
    file_size = len(content)
    
    # D. Convert the AI's string into a real Python object (dictionary)
    ai_data = json.loads(ai_json_string)
    
    return {
        "filename": file.filename,
        "size_in_bytes": file_size,
        "ai_analysis": ai_data # This goes back to React!
    }