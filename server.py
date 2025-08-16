''' Backend-processing for Better Beluga  '''
import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

# Check for the API key - production ready checks (jk will fix later)
if not os.environ.get("OPENAI_API_KEY"):
    print("UHOH - NO OPENAI KEY FOUND")
    
# Start up the model
model = init_chat_model("gpt-4o-mini", model_provider="openai")

