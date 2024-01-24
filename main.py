from pathlib import Path

from src import ResumeFormat, create_resume

create_resume(
    Path("inputs/example_resume_data.json"),
    Path("outputs/example_resume"),
    ResumeFormat.SINGLE_COLUMN_NOPHOTO,
)

print("Resume generated successfully.")
