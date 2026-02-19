from pydantic import BaseModel, EmailStr, Field

# 1. Define the 'Shape' of your data
class Lead(BaseModel):
    name: str
    # Note: EmailStr is a special type that validates email format automatically!
    email: str 
    # Budget must be an integer and greater than 500
    budget: int = Field(gt=500)
    description: str

# 2. Test with GOOD data
try:
    good_data = {"name": "Gagan", "email": "gagan@example.com", "budget": 2000}
    new_lead = Lead(**good_data) # The ** is like the JS spread operator ...
    print(f"Lead Validated: {new_lead.name}")

# 3. Test with BAD data
    bad_data = {"name": "Gagan", "email": "not-an-email", "budget": 100}
    wrong_lead = Lead(**bad_data)
except Exception as e:
    print(f"\nVALIDATION FAILED:\n{e}")