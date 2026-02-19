from typing import List
from pydantic import BaseModel

class Job(BaseModel):
    company: str
    title: str
    years: int

class Resume(BaseModel):
    name: str
    work_history: List[Job]  # A list of other Pydantic models!

# This is how you handle complex JSON from an AI
data = {
    "name": "Gagan",
    "work_history": [
        {"company": "Verizon", "title": "Engineer", "years": 3},
        {"company": "Cigna", "title": "Lead", "years": 2}
    ]
}

parsed_resume = Resume(**data)
print(parsed_resume.work_history[0].company) # Output: Verizon