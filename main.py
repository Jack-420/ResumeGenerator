from pathlib import Path

from src import create_resume

create_resume(Path("inputs/example_resume_data.json"), Path("output"))

print("LaTeX file generated successfully.")
