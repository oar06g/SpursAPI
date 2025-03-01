from dotenv import load_dotenv
import os

class Config:
  def __init__(self):
    load_dotenv()
    self.encryption_passowrd = os.getenv("ENCRYPTION_PASSWORD")
