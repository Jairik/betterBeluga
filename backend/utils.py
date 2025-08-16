''' Helper functions to aid in modulating code '''

# Convert a given bytestring to a vector
def convert_bytestring_to_vector(b: str):
    try:
        # Split the bytestring by commas and convert each part to a float
        return [float(x) for x in b.decode('utf-8').split(',')]
    except Exception as e:
        raise ValueError(f"Error converting bytestring to vector: {e}")