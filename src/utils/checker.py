import json
from src.utils.variables import PATH_INFO_JSON_FILE

def check_first_session() -> bool:
  """Checks if this is the first session based on the presence of data in the JSON file."""
  try:
    with open(PATH_INFO_JSON_FILE, 'r') as f:
      data = json.load(f)
    
    required_keys = ["name", "token", "password", "passwauth"]
    return not all(key in data for key in required_keys)
  
  except (FileNotFoundError, json.JSONDecodeError):
    with open("config/info.json", 'w') as f: ...
    return True

