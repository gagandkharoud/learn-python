from pydantic import BaseModel
from typing import List

# 1. The Small Piece: What is a single "Project"?
class Project(BaseModel):
    title: str
    tech_stack: List[str]  # This is a list of strings

class SocialMedia(BaseModel):
    platform: str
    url: str
    
# 2. The Big Piece: The whole "Company"
class Company(BaseModel):
    name: str
    portfolio: List[Project] # A list of Project objects!
    socials: List[SocialMedia]


# --- LET'S USE IT ---

# This data looks exactly like a JS Object / JSON
my_business_data = {
    "name": "Urban Logic Solutions",
    "portfolio": [
        {"title": "AI Agent", "tech_stack": ["Python", "FastAPI"]},
        {"title": "React Modal", "tech_stack": ["TypeScript", "Next.js"]}
    ],
    "socials": [
        {"platform" : "Linkedin", "url": "google.com"}
    ]
}

# We "feed" the data to the Company blueprint
my_company = Company(**my_business_data)

# Now we can access it with dots, just like JS
print(f"Company: {my_company.name}")
print(f"First Project: {my_company.portfolio[0].title}")
print(f"Spcials: {my_company.socials[0].platform}")