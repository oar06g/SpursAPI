def load_styles(filename: str) -> str:
  with open(filename, "r", encoding="UTF-8") as file:
    code  = file.read()
  return code 