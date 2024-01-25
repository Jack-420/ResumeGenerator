from pathlib import Path

from src import ResumeTemplate, create_resume

create_resume(
    Path("inputs/example_resume_data.json"),
    Path("outputs/example_resume"),
    ResumeTemplate.SINGLE_COLUMN_NOPHOTO,
)

print("Resume generated successfully.")
