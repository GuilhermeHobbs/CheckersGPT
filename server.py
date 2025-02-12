from fastapi import FastAPI
from pydantic import BaseModel
import torch

# Load your model
model = torch.load("your_model.pth")
model.eval()

app = FastAPI()

# Define request model
class InputData(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(data: InputData):
    prompt = data.prompt
    # Your model's inference logic here
    output = "HELLOOOO" #model.generate(prompt)  # Adjust based on your model's API
    return {"response": output}

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
