''' FastAPI responses for the frontend '''
from fastapi import FastAPI
from typing import Any, Dict
import processing

# Initialization
app = FastAPI()
model = processing.get_base_model()

# Test base path
@app.get("/")
def root():
    return {"Hello": "World"}

# Path to describe the contents of a bytestring
@app.post("/describeBytestring")
def getDescription(byteString: str) -> Dict[str, Any]:
    return processing.get_description_bytestring(model=model, bytestring=byteString)

# Path to define differences between two bytestrings
@app.post("/describeBytestringDifferences")
def getDifference(old_bytestring: str, new_byteString: str) -> Dict[str, Any]:
    return processing.get_difference_bytestring(model=model, old_bytestring=old_bytestring, new_bytestring=new_byteString)

# Path to mathematically describe the difference between two bytestrings
@app.post("/evaluateDifferences")
def evalDifference(old_bytestring: str, new_byteString: str):
    return processing.evaluate_bytestring_difference(old_bytestring=old_bytestring, new_bytestring=new_byteString)