import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"Environment variable '{name}' not found.")
    return value