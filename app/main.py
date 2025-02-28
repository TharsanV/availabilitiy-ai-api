from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from app.openai_service import OpenAIService
from app.models import MessageRequest 

# Initialize FastAPI app
app = FastAPI()

system_message = """
Please generate a JSON object that contains available timeslots based on the following chat message. The output should only include the JSON in this format:

{
  "availabilityStartTime": "",
  "availabilityEndTime": ""
}

Do not include any other text, just the JSON.
"""

# Define a dependency that provides the OpenAIService
def get_openai_service() -> OpenAIService:
    return OpenAIService()  # You can customize initialization if needed

@app.post("/send_message")
async def process_message(request: MessageRequest, openai_service: OpenAIService = Depends(get_openai_service)):
    try:
        messages: List[Dict[str, str]] =  [
                {"role": "system", "content": system_message},
                {"role": "user", "content": request.message},
            ]
        
        # Use the OpenAIService to send the message and get a response
        response = openai_service.send_message(messages)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interacting with OpenAI API: {str(e)}")


# //type of message
# //availability
# //things to bring
# //potential locations
# //Experiences
# //REsponsibilities 

# async
# data balidation
# error handling
# Pydantic
# Extra Models