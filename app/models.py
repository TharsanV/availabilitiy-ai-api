from pydantic import BaseModel

# Create a Pydantic model to define the request body format
class MessageRequest(BaseModel):
    author: str
    message: str