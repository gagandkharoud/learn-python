import asyncio
from pydantic import BaseModel
from typing import List

# 1. THE SCHEMA (The Blueprint)
class Experience(BaseModel):
    company: str
    role: str
    years: int

class Resume(BaseModel):
    name: str
    skills: List[str]
    experience: List[Experience]

# 2. THE ASYNC "AI" CALL (The Simulation)
async def mock_ai_extract_data(pdf_text: str):
    print("⏳ AI is parsing PDF text...")
    await asyncio.sleep(2) # Simulate network latency
    
    # This is what a real AI would return
    return {
        "name": "Gagan Kharoud",
        "skills": ["React", "Python", "FastAPI"],
        "experience": [
            {"company": "Urban Logic Solutions", "role": "Lead Developer", "years": 2},
            {"company": "Previous Corp", "role": "Software Engineer", "years": 5}
        ]
    }

# 3. THE MAIN ENGINE
async def main():
    # In a real app, we'd read the PDF here
    # For now, let's just use a string
    raw_pdf_content = "This is some text from a resume PDF..."
    
    # Await the AI extraction
    raw_json = await mock_ai_extract_data(raw_pdf_content)
    
    try:
        # VALIDATE the data with Pydantic
        validated_resume = Resume(**raw_json)
        
        print("\n✅ EXTRACTION SUCCESSFUL")
        print(f"Name: {validated_resume.name}")
        print(f"Top Skill: {validated_resume.skills[0]}")
        print(f"Total Experience count: {len(validated_resume.experience)}")
        
    except Exception as e:
        print(f"❌ VALIDATION ERROR: {e}")

if __name__ == "__main__":
    asyncio.run(main())