from pydantic import BaseModel, field_validator

class UserSignup(BaseModel):
    username: str

    @field_validator('username')
    @classmethod
    def check_username_length(cls, v):
        # WRITE YOUR LOGIC HERE:
        # If the length of v is less than 5, raise a ValueError.
        # Hint: In Python, you get length using: len(v)
        print(f"--- The Guardian is checking the value: {v} ---") # Add this!
        if len(v) < 5:
             raise ValueError('Username is too short!')
             
        return v

# --- TEST IT BELOW ---
try:
    user = UserSignup(username="Gagan") # This should fail
except Exception as e:
    print(e)