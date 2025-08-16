''' Model initialization for the backend-processing '''
import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
import formats
import utils
import statistics

# Initialize and return the base model
def get_base_model():
    # Pull in the api key from env
    if not os.environ.get("OPENAI_API_KEY"):
        print("UHOH - NO OPENAI KEY FOUND")
    
    # Start up and return the model
    model = init_chat_model("gpt-4o-mini", model_provider="openai")
    return model

# Invoke the model to describe a given bytestring
def get_description_bytestring(model, bytestring):
    # Model prompt
    messages = [
        SystemMessage("Describe the image contents of the provided bytestring. Keep the response around 1-2 sentences."),
        HumanMessage(bytestring)
    ]
    
    # Return the JSON output of the model
    return model.with_structured_output(formats.model_description_response).invoke(messages)

# Use the model to describe the difference between two given bytestrings
def get_difference_bytestring(model, old_bytestring, new_bytestring):
    # Model prompt
    messages = [ 
        SystemMessage("Observe the difference between these two bytestrings, which represent images. Describe the difference among these images"),
        HumanMessage([old_bytestring, new_bytestring])
    ]
    
    # Return the JSON output of the model
    return model.with_structured_output(formats.model_difference_response).invoke(messages)

# !NOTE - This will stop early if two bytestrings are different sizes
# Mathematically determine the difference between two bytestrings
def evaluate_bytestring_difference(old_bytestring: str, new_bytestring: str) -> int:
    # Convert each bytestring to a vector
    old_vector = utils.bytestring_to_vector(bytestring=old_bytestring)
    new_vector = utils.bytestring_to_vector(bytestring=new_bytestring)
    # Compare each element
    result = []
    for new, old in zip(new_vector, old_vector):
        result.append(new - old)
    # Return the mean difference
    return statistics.mean(result)