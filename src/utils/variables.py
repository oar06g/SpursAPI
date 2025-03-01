import os
from dotenv import load_dotenv
load_dotenv()

# Paths
PATH_INFO_JSON_FILE = os.path.join("config", "info.json")
PATH_DARK_MOD_STYLE = os.path.join("assets", "themes", "darkmod.css")

# Passwords
ENCRYPTION_PASSWORD = os.getenv("ENCRYPTION_PASSWORD")
