from pathlib import Path

from src import create_resume

create_resume(Path("inputs/example_resume_data.json"), Path("outputs/resume"))

print("LaTeX file generated successfully.")
