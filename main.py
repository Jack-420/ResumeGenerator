from pathlib import Path

from src import create_resume

create_resume(Path("inputs/example_resume_data.json"), Path("outputs/example_resume"))

print("Resume generated successfully.")
