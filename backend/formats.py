''' Defines the classes for formatting the LLM responses '''
from typing import Optional
from typing_extensions import Annotated, TypedDict

# JSON response schema for a bytestring description
class model_description_response(TypedDict):
    ''' Response layout from the model '''
    description: Annotated[str, ..., "The description of the provided bytestring"]

# JSON response schema for a bytestring comparison
class model_difference_response(TypedDict):
    ''' Reponse layout from the model '''
    difference: Annotated[str, ..., "The difference among the two images"]
    percent_difference: Annotated[Optional[int], None, "The percent difference between the two images"]
